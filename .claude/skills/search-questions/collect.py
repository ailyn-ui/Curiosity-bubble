"""Collect Google and YouTube search suggestions for a seed phrase.

Usage:
  python3 -I collect.py "brand strategy" [--source google|youtube|both]
                       [--lang en] [--country ch] [--out file.json] [--pause 0.4]

Asks the public suggestion service (the list that appears as you type) for the
seed combined with question words, prepositions, comparisons and a-z, and saves
every suggestion with the query that produced it. Prints BLOCKED and exits 2 if
the service can't be reached.
"""
import argparse, json, os, ssl, sys, time, urllib.parse, urllib.request
from datetime import date

QUESTIONS = ["how", "how to", "what", "what is", "why", "why is", "can", "can i",
             "is", "are", "do i need", "should i", "where", "when", "which", "who", "will"]
PREPOSITIONS = ["for", "with", "without", "to", "near", "like", "vs", "or", "and", "versus"]
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
ENDPOINT = "https://suggestqueries.google.com/complete/search"


def context():
    cafile = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")
    if not cafile and os.path.exists("/root/.ccr/ca-bundle.crt"):
        cafile = "/root/.ccr/ca-bundle.crt"
    return ssl.create_default_context(cafile=cafile) if cafile else ssl.create_default_context()


def suggest(q, source, lang, country, ctx):
    params = {"client": "firefox", "hl": lang, "gl": country, "q": q}
    if source == "youtube":
        params["ds"] = "yt"
    url = ENDPOINT + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "search-questions-skill"})
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        raw = r.read().decode(r.headers.get_content_charset() or "utf-8", "replace")
    data = json.loads(raw)
    return [s for s in data[1] if isinstance(s, str)]


def queries(seed):
    yield ("seed", seed)
    for w in QUESTIONS:
        yield ("question", f"{w} {seed}")
    for p in PREPOSITIONS:
        yield ("preposition", f"{seed} {p}")
    for l in LETTERS:
        yield ("letter", f"{seed} {l}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("seed")
    ap.add_argument("--source", choices=["google", "youtube", "both"], default="both")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--country", default="ch")
    ap.add_argument("--out")
    ap.add_argument("--pause", type=float, default=0.4)
    a = ap.parse_args()

    ctx = context()
    sources = ["google", "youtube"] if a.source == "both" else [a.source]
    seen, rows = set(), []
    for src in sources:
        for kind, q in queries(a.seed):
            try:
                found = suggest(q, src, a.lang, a.country, ctx)
            except Exception as e:  # network refusal, proxy 403, timeout
                if not rows:
                    print(f"BLOCKED: could not reach suggestqueries.google.com ({e})")
                    sys.exit(2)
                print(f"skip {src} '{q}': {e}", file=sys.stderr)
                continue
            for s in found:
                key = (src, s.lower())
                if key in seen:
                    continue
                seen.add(key)
                rows.append({"source": src, "kind": kind, "query": q, "suggestion": s})
            time.sleep(a.pause)

    result = {"seed": a.seed, "lang": a.lang, "country": a.country, "date": date.today().isoformat(),
              "count": len(rows), "suggestions": rows}
    if a.out:
        os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=1)
        print(f"saved {len(rows)} suggestions to {a.out}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
