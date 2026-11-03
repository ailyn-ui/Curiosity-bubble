#!/usr/bin/env python3
"""AI Rehab counter: finds AI-writing tells, fact items, and warmth signals.

Usage:
  python3 count_tells.py scan FILE [--json]
  python3 count_tells.py compare BEFORE AFTER [--json]

Standard library only; runs on Python 3.8+. Every count it prints is "counted by script".
The script finds candidates; the assistant judges each one in context, and the writer's voice wins.
"""

import argparse
import collections
import difflib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATTERNS_FILE = os.path.join(HERE, "tells_patterns.json")
SOURCE = "counted by script"

# Curly quotes and apostrophes become straight ones before matching. Each swap is one
# character for one character, so match offsets still point at the original text.
STRAIGHTEN = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'})

# A "short" sentence for the staccato check has at most this many words. Basis: the
# staccato examples in The Uncommon Business's Anti-AI Writing Rules ("We slowed down. We listened.")
# run 2-3 words, and slogan triads like "Fast. Simple. Effective." run 1 word.
STACCATO_MAX_WORDS = 4
# Three short sentences in a row is the pattern both sources name ("Clean. Efficient. Safe.").
STACCATO_RUN = 3

MEANING_WORDS = ["not", "no", "never", "only", "unless", "until", "if", "must", "free",
                 "guaranteed", "guarantee", "up to", "at least", "at most", "before", "after",
                 "every", "all", "none", "except", "without", "limited", "minimum", "maximum"]

# Words that change a number's claim only when a number follows ("over 20 years", not "over coffee").
NUMBER_QUALIFIERS = ["over", "more than", "less than", "under", "nearly", "almost", "about",
                     "around", "approximately", "roughly"]

# Warmth is care and courtesy toward the reader (owner decision, 2026-10-03). Excitement
# ("thrilled to", exclamation marks) is not counted, and no phrase sits inside another, so one
# courtesy counts once. Words inside a tell the script finds are not counted either: the catalog
# calls "I hope this helps" a chatbot line, so cutting it is not a loss of warmth.
WARM_PHRASES = ["please", "thank you", "thanks", "appreciate", "would you", "could you",
                "happy to", "glad to", "love to", "i hope", "if it works", "feel free", "let me know",
                "no rush"]
PRONOUNS = ["i", "i'm", "i'd", "i've", "i'll", "me", "my", "we", "we're", "we'll", "we've",
            "us", "our", "you", "you're", "you'll", "you've", "you'd", "your", "yours"]

# Words that often open a sentence and are not part of a name ("Ask Callan Faulkner").
SENTENCE_STARTERS = set("""a an and ask but call come check get give go how i if in join let meet
our please read see so the then this those these to try visit we what when where why with you
your book email find grab hear hi hey hello dear as at on for from by after before while since
my thanks also plus now today every each all both here there it she he they its their her his""".split())

# A line counts as a Title Case heading (skipped for name tracking) when it has at least
# 5 words, no closing punctuation, and at least 60% of its words capitalized.
# Word floor basis: the longest business name in our test pieces runs 4 words ("Harbor & Vine
# Events"), and a 4-word line like "Talk to Ana Ruiz" must keep its name, so headings start at 5.
# Share basis: Title Case leaves only short joining words (to, of, the, and) lowercase, about a
# fifth to a third of a headline's words; ordinary sentences capitalize far fewer than 60%.
HEADING_MIN_WORDS = 5
HEADING_CAPS_SHARE = 0.6

# A capitalized word may carry capitalized hyphen parts: "Tune-Up" is one word, "Austin-based" is not.
CAP_WORD = r"[A-Z][a-z]+(?:-[A-Z][a-z]+)*"
NAME_RX = re.compile(r"\b" + CAP_WORD + r"(?:(?:[ \t]+(?:&|of|de|la|van|von))?[ \t]+" + CAP_WORD + r")+\b")
PROPER_RX = re.compile(r"\b[A-Z][a-z]+[A-Za-z]*(?:-[A-Z][a-z]+)*\b")
# Small words a Title Case line capitalizes. They are never part of a name, so "Your Visit With
# Maria Lopez" yields "Maria Lopez", not one long name.
TITLE_WORDS = set("""a an and or but nor of in on at to for from by with into onto over about
the your our my his her their its is are was be we you us it this that these those""".split())
# A one-word sign-off name: a capitalized word alone on the line after a line ending in a
# comma ("Best,\nMaya"). "Thanks!" or "Cheers," on that line is not a name.
SIGN_OFF_RX = re.compile(r"(?m)(?<=,\n)[ \t]*([A-Z][a-z]+)[ \t]*$")

# Time zones and number words count as facts: "1pm CT" and "four weeks" must not change
# silently. "one" is left out because rewrites swap it with "a" without changing meaning.
ZONES = r"(?:CT|ET|PT|MT|CST|CDT|EST|EDT|PST|PDT|MST|MDT|GMT|UTC|BST|CET|AEST)"
NUMBER_WORDS = (r"(?:two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|"
                r"fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|"
                r"eighty|ninety|hundred|thousand|million|dozen|half)")
QUALIFIED_NUMBER = r"\s+(?=[$€£]?\d|" + NUMBER_WORDS + r"\b)"
MONTHS = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|"
          r"Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)")
WEEKDAYS = r"(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"

FACT_PATTERNS = [
    ("quote", re.compile(r'"[^"\n]+"')),
    ("url", re.compile(r"https?://[^\s<>\"]+[^\s<>\".,;:!?)]")),
    ("email", re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")),
    ("money", re.compile(r"[$€£]\s?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:\s?(?:k|K|m|M|million|billion)\b)?")),
    ("percent", re.compile(r"\b\d+(?:\.\d+)?\s?%")),
    ("time", re.compile(r"\b\d{1,2}(?::\d{2})?\s?(?:am|pm|AM|PM)(?:\s?" + ZONES + r")?\b")),
    ("zone", re.compile(r"\b" + ZONES + r"\b")),
    ("number_word", re.compile(r"\b" + NUMBER_WORDS + r"\b", re.IGNORECASE)),
    ("date", re.compile(r"\b" + MONTHS + r"\.?\s+\d{1,2}(?:st|nd|rd|th)?(?:,\s*\d{4})?\b")),
    ("date", re.compile(r"\b\d{1,2}/\d{1,2}(?:/\d{2,4})?\b")),
    ("weekday", re.compile(r"\b" + WEEKDAYS + r"\b")),
    ("phone", re.compile(r"(?<!\w)\+?\d[\d ().-]{7,}\d\b")),
    ("handle", re.compile(r"(?<!\w)@\w+")),
]
NUMBER_RX = re.compile(r"\b(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\b")


def load_patterns(path=PATTERNS_FILE):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    compiled = []
    for cat in data["categories"]:
        flags = 0
        for ch in cat.get("flags", ""):
            flags |= {"i": re.IGNORECASE, "m": re.MULTILINE}[ch]
        if cat["kind"] == "words":
            flags |= re.IGNORECASE
            regexes = [re.compile(r"(?<![\w'-])" + re.escape(item).replace(r"\ ", r"\s+") + r"(?![\w'-])", flags)
                       for item in cat["items"]]
        else:
            regexes = [re.compile(item, flags) for item in cat["items"]]
        compiled.append({"id": cat["id"], "label": cat["label"],
                         "house_style": bool(cat.get("house_style")), "regexes": regexes})
    return compiled


def quote_spans(text):
    return [m.span() for m in re.finditer(r'"[^"\n]+"', text)]


def inside(pos, spans):
    return any(a <= pos < b for a, b in spans)


def split_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if re.search(r"\w", p)]


def word_list(text):
    return re.findall(r"[\w'$%.,:/@#-]+", text)


LIST_LINE = re.compile(r"^\s*(?:[-*\u2022#>]|\d+[.)]|[^\w\s\"'(])")


def prose_lines(text):
    """Lines that read as prose: not list items, headings, or quote marks, and ending a
    sentence. Lists and headings are short by design and are not staccato."""
    keep = []
    for line in text.split("\n"):
        if LIST_LINE.match(line) or not re.search(r"[.!?][\"')]?\s*$", line):
            keep.append("")
        else:
            keep.append(line)
    return "\n".join(keep)


def staccato_runs(text):
    """Runs of STACCATO_RUN or more consecutive short sentences in prose lines, each given as
    the list of its first STACCATO_RUN sentences."""
    runs, streak = [], []
    unquoted = re.sub(r'"[^"\n]+"', lambda m: " " * len(m.group(0)), text)
    for sentence in split_sentences(prose_lines(unquoted)):
        if len(re.findall(r"\w[\w'-]*", sentence)) <= STACCATO_MAX_WORDS:
            streak.append(sentence)
            if len(streak) == STACCATO_RUN:
                runs.append(list(streak))
        else:
            streak = []
    return runs


def tell_matches(text, patterns):
    """(category, match) for each catalog match, one per span within a category. An emoji
    bullet counts only inside a list: the next or previous non-blank line starts with one too."""
    found = []
    for cat in patterns:
        taken = []
        for rx in cat["regexes"]:
            for m in rx.finditer(text):
                start, end = m.span()
                if any(a < end and start < b for a, b in taken):
                    continue
                taken.append((start, end))
                found.append((cat, m))
    bullet_lines = {text.count("\n", 0, m.start()) for cat, m in found if cat["id"] == "emoji_bullet"}
    filled = [i for i, line in enumerate(text.split("\n")) if line.strip()]

    def in_list(line):
        k = filled.index(line)
        return (k > 0 and filled[k - 1] in bullet_lines) or (k + 1 < len(filled) and filled[k + 1] in bullet_lines)

    return [(cat, m) for cat, m in found
            if cat["id"] != "emoji_bullet" or in_list(text.count("\n", 0, m.start()))]


def find_tells(text, patterns):
    spans = quote_spans(text)
    hits = []
    for cat, m in tell_matches(text, patterns):
        start = m.start()
        hits.append({"category": cat["id"], "label": cat["label"], "match": m.group(0),
                     "line": text.count("\n", 0, start) + 1,
                     "protected": inside(start, spans),
                     "house_style": cat["house_style"]})
    for run in staccato_runs(text):
        start = max(text.find(run[0]), 0)
        hits.append({"category": "staccato", "label": "Three short sentences in a row", "match": " ".join(run),
                     "line": text.count("\n", 0, start) + 1, "protected": False, "house_style": False})
    return hits


def blank(s, a, b):
    return s[:a] + " " * (b - a) + s[b:]


def at_sentence_start(s, pos):
    """A word is mid-sentence only when a letter, digit, comma, or closing mark comes right
    before it. Anything else (start of text, end of a sentence, a line break, a bullet or emoji)
    means it starts a sentence or a list item. After a closing quote, the mark before the
    quote decides: 'she said "I love it." The team' starts a new sentence."""
    before = s[:pos].rstrip(" \t")
    if before and before[-1] in "\"'\u201d\u2019":
        inner = before.rstrip("\"'\u201d\u2019")
        return not inner or inner[-1] in ".!?\n"
    return not (before and (before[-1].isalnum() or before[-1] in ",;&)/"))


def mask_headings(s):
    out, pos = [], 0
    for line in s.split("\n"):
        words = line.split()
        caps = [w for w in words if w[:1].isupper()]
        is_heading = (len(words) >= HEADING_MIN_WORDS and not re.search(r"[.!?]\s*$", line)
                      and len(caps) >= HEADING_CAPS_SHARE * len(words))
        out.append(" " * len(line) if is_heading else line)
    return "\n".join(out)


def name_runs(s, text):
    """(start, end) of each name of two or more capitalized words in s, split at capitalized
    title words ("With", "Your"; a lowercase "of" still joins "Bank of America"). A first word that
    only starts the sentence ("Ask Callan Faulkner") is left out. Lone words are left for the
    single-word pass."""
    spans = []
    for m in NAME_RX.finditer(s):
        tokens = [(t.start() + m.start(), t.group(0)) for t in re.finditer(r"\S+", m.group(0))]
        if at_sentence_start(text, m.start()) and tokens[0][1].lower() in SENTENCE_STARTERS:
            tokens = tokens[1:]
        run = []
        for tok in tokens + [(None, None)]:
            if tok[1] is not None and not (tok[1][0].isupper() and tok[1].lower() in TITLE_WORDS):
                run.append(tok)
                continue
            if len(run) >= 2:
                spans.append((run[0][0], run[-1][0] + len(run[-1][1])))
            run = []
    return spans


def fact_items(text):
    """Fact items in order of appearance. Each matched span is blanked out so a price is not
    also counted as a bare number, and a name is not counted again word by word."""
    work = text
    found = []
    for kind, rx in FACT_PATTERNS:
        for m in rx.finditer(work):
            item = m.group(0).strip()
            found.append((m.start(), item.lower() if kind == "number_word" else item))
        work = rx.sub(lambda m: " " * len(m.group(0)), work)
    names = mask_headings(work)
    for a, b in name_runs(names, text):
        found.append((a, text[a:b]))
        names = blank(names, a, b)
        work = blank(work, a, b)
    # A heading or subject line in Title Case can't show which capitals are names, so its words
    # are skipped above. A name there that the body also uses is listed, so changing it in the
    # heading is caught; headline words ("A Fresh Look at Spring") stay off the list.
    body = mask_headings(text)
    headings = "\n".join(" " * len(w) if w == n else w
                         for w, n in zip(work.split("\n"), mask_headings(work).split("\n")))
    for a, b in name_runs(headings, text):
        if re.search(r"(?<!\w)" + re.escape(text[a:b]) + r"(?!\w)", body):
            found.append((a, text[a:b]))
            work = blank(work, a, b)
    for m in SIGN_OFF_RX.finditer(names):
        if m.group(1).lower() in SENTENCE_STARTERS or m.group(1).lower() in TITLE_WORDS:
            continue
        found.append((m.start(1), m.group(1)))
        names = blank(names, m.start(1), m.end(1))
        work = blank(work, m.start(1), m.end(1))
    for m in PROPER_RX.finditer(names):
        if not at_sentence_start(text, m.start()) and m.group(0).lower() not in TITLE_WORDS:
            found.append((m.start(), m.group(0)))
            work = blank(work, m.start(), m.end())
    for m in NUMBER_RX.finditer(work):
        found.append((m.start(), m.group(0)))
    return [item for _, item in sorted(found)]


def meaning_words(text):
    low = text.lower()
    counts = collections.Counter()
    counts["not"] += len(re.findall(r"\b\w+n't\b", low))
    for w in MEANING_WORDS:
        rx = r"(?<![\w'])" + re.escape(w).replace(r"\ ", r"\s+") + r"(?![\w'])"
        counts[w] += len(re.findall(rx, low))
    for w in NUMBER_QUALIFIERS:
        rx = r"(?<![\w'])" + re.escape(w).replace(r"\ ", r"\s+") + QUALIFIED_NUMBER
        counts[w] += len(re.findall(rx, low))
    return +counts


def warmth(text, patterns=None):
    """Care and courtesy signals: courtesy phrases, "I/we/you" words, and contractions, counted
    outside the tells the script finds."""
    text = text.translate(STRAIGHTEN)
    for _, m in tell_matches(text, patterns or load_patterns()):
        text = blank(text, m.start(), m.end())
    low = text.lower()
    phrases = collections.Counter()
    for p in WARM_PHRASES:
        n = len(re.findall(r"(?<![\w'])" + re.escape(p) + r"(?![\w'])", low))
        if n:
            phrases[p] = n
    pronouns = sum(len(re.findall(r"(?<![\w'])" + re.escape(p) + r"(?![\w'])", low)) for p in PRONOUNS)
    contractions = len(re.findall(r"\b\w+'(?:s|re|ve|ll|d|m|t)\b", low))
    total = sum(phrases.values()) + pronouns + contractions
    return total, phrases


def multiset_diff(a, b):
    """Items in a that b lacks, keeping a's order and repeats."""
    remaining = collections.Counter(b)
    out = []
    for item in a:
        if remaining[item] > 0:
            remaining[item] -= 1
        else:
            out.append(item)
    return out


def meaning_context(before, after, words):
    """Pair each missing meaning word with the input sentence that lost it: the sentence
    whose closest match in the output has fewer of that word. The reader then judges whether
    a claim changed or a filler line was cut."""
    out_sentences = split_sentences(after)
    credit = [meaning_words(o) for o in out_sentences]
    pairs = []
    for sentence in split_sentences(before):
        have = meaning_words(sentence)
        if not have:
            continue
        scores = [difflib.SequenceMatcher(None, sentence, o).ratio() for o in out_sentences]
        best = max(range(len(scores)), key=scores.__getitem__) if scores else None
        pairs.append((scores[best] if scores else 0, sentence, have, best))
    # Closest pairs claim first, and each output word backs one draft sentence only, so two
    # draft sentences cannot both lean on the same "not".
    losses = []
    for _, sentence, have, best in sorted(pairs, key=lambda p: -p[0]):
        for w, n in have.items():
            kept = min(n, credit[best].get(w, 0)) if best is not None else 0
            if kept:
                credit[best][w] -= kept
            losses += [(w, sentence)] * (n - kept)
    out, taken = [], set()
    for w in words:
        for j, (lw, sentence) in enumerate(losses):
            if lw == w and j not in taken:
                taken.add(j)
                out.append({"word": w, "sentence": sentence})
                break
    return out


def raw_count(text, item):
    flags = re.IGNORECASE if item.islower() else 0
    return len(re.findall(r"(?<!\w)" + re.escape(item) + r"(?!\w)", text, flags))


# Only plain words can be recased: links, emails, quotes, handles, and anything with a digit keep
# their exact form (a link's path is case-sensitive).
WORD_ITEM = re.compile(r"^[A-Za-z][A-Za-z'&-]*(?: [A-Za-z&][A-Za-z'&-]*)*$")


def heading_like(line):
    """A line that ends without sentence punctuation and capitalizes most of its words: a heading
    or a subject line, where sentence-casing changes capitals and nothing else."""
    words = line.split()
    caps = [w for w in words if w[:1].isupper()]
    return bool(words) and not re.search(r"[.!?,;:]\s*$", line) and len(caps) >= HEADING_CAPS_SHARE * len(words)


def only_on_kept_headings(item, text_a, text_b):
    """Every line of text_a holding the item is a heading, and text_b still has each of those
    lines with only capitals changed. "Spring Roof Check" -> "Spring roof check" qualifies; "Call
    Mark today" -> "Please mark the date" does not."""
    rx = re.compile(r"(?<!\w)" + re.escape(item) + r"(?!\w)")
    lines = [line.strip() for line in text_a.split("\n") if rx.search(line)]
    kept = {line.strip().lower() for line in text_b.split("\n")}
    return bool(lines) and all(heading_like(line) and line.lower() in kept for line in lines)


def split_recased(items, text_a, text_b):
    """(changed, recased): a plain-word item that sits only on heading lines of text_a, and that
    text_b still has as often once capitals are ignored, was recased ("Spring Roof Check" to
    "Spring roof check"), not lost or added. A name inside a sentence never counts as recased:
    "We met May" becoming "we may meet" is a lost name."""
    changed, recased = [], []
    for item in items:
        rx = r"(?<!\w)" + re.escape(item) + r"(?!\w)"
        if (WORD_ITEM.match(item) and only_on_kept_headings(item, text_a, text_b)
                and len(re.findall(rx, text_b, re.IGNORECASE)) >= len(re.findall(rx, text_a, re.IGNORECASE))):
            recased.append(item)
        else:
            changed.append(item)
    return changed, recased


# A link with punctuation right after it. Step 3 forbids adding punctuation the draft did not
# have there: some mail apps take the mark into the link.
GLUED_LINK_RX = re.compile(r"(https?://[^\s<>\"]+[^\s<>\".,;:!?)])([.,;:!?])")


def glued_links(text):
    return [m.group(1) + m.group(2) for m in GLUED_LINK_RX.finditer(text)]


def confirm_diff(items, text_a, text_b):
    """Keep only items that text_b really has fewer of than text_a, counted in the raw text.
    Names at a sentence start are not extracted, so moving a name there must not look like a loss."""
    out, seen = [], collections.Counter()
    for item in items:
        if seen[item] < raw_count(text_a, item) - raw_count(text_b, item):
            seen[item] += 1
            out.append(item)
    return out


def scan(text, patterns=None):
    patterns = patterns or load_patterns()
    text = text.translate(STRAIGHTEN)
    hits = find_tells(text, patterns)
    open_hits = [h for h in hits if not h["protected"]]
    by_cat = collections.Counter(h["category"] for h in open_hits)
    warm_total, warm_phrases = warmth(text, patterns)
    return {
        "source": SOURCE,
        "words": len(word_list(text)),
        "sentences": len(split_sentences(text)),
        "tells_total": len(open_hits),
        "tells_per_100_words": round(100.0 * len(open_hits) / max(len(word_list(text)), 1), 1),
        "tells_by_category": dict(by_cat),
        "protected_tells": len(hits) - len(open_hits),
        "tells": open_hits,
        "facts": fact_items(text),
        "meaning_words": dict(meaning_words(text)),
        "warmth": warm_total,
        "warm_phrases": dict(warm_phrases),
    }


# A hashtag starts with a letter and follows no word character: "#FallGlow", but not "#1" or "C#".
HASHTAG_RX = re.compile(r"(?<![\w&#])#[A-Za-z][A-Za-z0-9_]*")


def compare(before, after, patterns=None):
    patterns = patterns or load_patterns()
    a, b = scan(before, patterns), scan(after, patterns)
    sa, sb = before.translate(STRAIGHTEN), after.translate(STRAIGHTEN)
    a_mean = [w for w, n in a["meaning_words"].items() for _ in range(n)]
    b_mean = [w for w, n in b["meaning_words"].items() for _ in range(n)]
    new_warm = [p for p, n in b["warm_phrases"].items() if n > a["warm_phrases"].get(p, 0)]
    aw = word_list(before.translate(STRAIGHTEN))
    bw = word_list(after.translate(STRAIGHTEN))
    matched = sum(block.size for block in difflib.SequenceMatcher(None, aw, bw, autojunk=False).get_matching_blocks())
    longest = max(len(aw), len(bw)) or 1
    missing, recased_old = split_recased(confirm_diff(multiset_diff(a["facts"], b["facts"]), sa, sb), sa, sb)
    # Repeating a name or number the draft already has is not new: only items absent
    # from the draft's raw text count (an early test flagged a repeated "The Bootcamp" as new).
    new, recased_new = split_recased(
        [i for i in confirm_diff(multiset_diff(b["facts"], a["facts"]), sb, sa) if not raw_count(sa, i)], sb, sa)
    return {
        "source": SOURCE,
        "tells_before": a["tells_total"],
        "tells_after": b["tells_total"],
        "tells_before_by_category": a["tells_by_category"],
        "tells_left": b["tells"],
        "protected_tells_after": b["protected_tells"],
        "facts_before": len(a["facts"]),
        "facts_missing": missing,
        "facts_new": new,
        "facts_recased": recased_old + recased_new,
        "links_punctuation_added": multiset_diff(glued_links(sb), glued_links(sa)),
        "meaning_missing": multiset_diff(a_mean, b_mean),
        "meaning_missing_context": meaning_context(sa, sb, multiset_diff(a_mean, b_mean)),
        "meaning_new": multiset_diff(b_mean, a_mean),
        "warmth_before": a["warmth"],
        "warmth_after": b["warmth"],
        "new_warm_phrases": new_warm,
        "hashtags_missing": multiset_diff(HASHTAG_RX.findall(sa), HASHTAG_RX.findall(sb)),
        "hashtags_new": multiset_diff(HASHTAG_RX.findall(sb), HASHTAG_RX.findall(sa)),
        "changed_word_ratio": round(1 - matched / longest, 3),
    }


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except (OSError, UnicodeDecodeError) as e:
        sys.stderr.write("error: cannot read %s (%s)\n" % (path, e))
        sys.exit(2)


def print_compare(r):
    print("Tells: %d found, %d left (%s)" % (r["tells_before"], r["tells_after"], SOURCE))
    if r["facts_missing"] or r["facts_new"] or r["meaning_missing"] or r["meaning_new"]:
        print("CHECK THESE (fact items always need restoring; meaning words need a decision)")
        for label, key in (("missing fact", "facts_missing"), ("new fact", "facts_new"),
                           ("missing word", "meaning_missing"), ("new word", "meaning_new")):
            for item in r[key]:
                print("  %s: %s" % (label, item))
        for c in r["meaning_missing_context"]:
            print("  '%s' most likely from: %s" % (c["word"], c["sentence"]))
    else:
        print("Facts: %d kept, nothing new (%s)" % (r["facts_before"], SOURCE))
    for item in r["facts_recased"]:
        print("  recased (a heading word whose capitals changed; make sure it is not a name): %s" % item)
    for item in r["links_punctuation_added"]:
        print("  LINK GAINED PUNCTUATION (take it off, end the sentence another way): %s" % item)
    if r["hashtags_missing"] or r["hashtags_new"]:
        print("HASHTAGS CHANGED (keep them as written unless the user said \"drop hashtags\")")
        for label, key in (("missing hashtag", "hashtags_missing"), ("new hashtag", "hashtags_new")):
            for item in r[key]:
                print("  %s: %s" % (label, item))
    print("Warmth signals: %d before, %d after" % (r["warmth_before"], r["warmth_after"]))
    if r["new_warm_phrases"]:
        print("  new warm phrases (each must trace to a converted line): %s" % ", ".join(r["new_warm_phrases"]))
    print("Changed words: %.0f%%" % (r["changed_word_ratio"] * 100))
    for h in r["tells_left"]:
        print("  left: line %d %s: %s" % (h["line"], h["category"], h["match"]))


def print_scan(r):
    print("Tells: %d found (%s); %d inside protected quotes" % (r["tells_total"], SOURCE, r["protected_tells"]))
    print("Density: %.1f tells per 100 words" % r["tells_per_100_words"])
    for cat, n in sorted(r["tells_by_category"].items()):
        print("  %s: %d" % (cat, n))
    print("Facts: %d items; warmth signals: %d" % (len(r["facts"]), r["warmth"]))


def main(argv=None):
    ap = argparse.ArgumentParser(prog="count_tells.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan")
    s.add_argument("file")
    s.add_argument("--json", action="store_true")
    c = sub.add_parser("compare")
    c.add_argument("before")
    c.add_argument("after")
    c.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    try:
        patterns = load_patterns()
    except (OSError, ValueError, KeyError) as e:
        sys.stderr.write("error: cannot read the tell catalog %s (%s)\n" % (PATTERNS_FILE, e))
        sys.stderr.write("Run count_tells.py from the skill's scripts folder, where tells_patterns.json "
                         "sits beside it, not from a copy made somewhere else.\n")
        return 2
    if args.cmd == "scan":
        r = scan(read(args.file), patterns)
        if args.json:
            print(json.dumps(r, indent=1, ensure_ascii=False))
        else:
            print_scan(r)
    else:
        r = compare(read(args.before), read(args.after), patterns)
        if args.json:
            print(json.dumps(r, indent=1, ensure_ascii=False))
        else:
            print_compare(r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
