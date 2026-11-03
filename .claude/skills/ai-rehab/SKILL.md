---
name: ai-rehab
description: Removes AI-writing tells from pasted text, files, or drafts while keeping facts, voice, and warmth. Use for 'rehab this', 'clean this up', 'make it sound human', or 'remove the AI'.
license: Free to use from The Uncommon Business. Do not resell. See LICENSE.
metadata:
  version: "1.0.1"
  audience: "student"
  author: "The Uncommon Business"
---

# AI Rehab

AI Rehab takes writing that sounds like AI and gives it back sounding like the person who is sending it. It keeps the writer's facts, meaning, voice, warmth, and courtesy, and it shows a short report card with real counts.

The people who use it run small businesses. They paste drafts they are about to send to clients, followers, and customers, so a changed price, a dropped condition, or an invented promise costs them far more than a stiff sentence does. That is why accuracy outranks sounding natural everywhere in this skill.

## When to use it

- **Rehab:** the user shares content (pasted text, a file, or a screenshot) and asks to rehab it, clean it up, make it sound human, or remove the AI. "Use ai-rehab" also starts it.
- **Guard:** when the user's instructions ask for AI Rehab on everything you write for them, write new content (posts, emails, captions, pages) the rehabbed way from the start and add a one-line card. Ordinary chat replies get no card.
- **Skip:** "skip rehab" skips it for that message.

## Order of priority

When two goals pull against each other, the higher one wins:

1. The writer's facts and meaning.
2. The writer's voice, including warmth, courtesy, and rhythm.
3. The reader and the channel (LinkedIn, email, caption, sales page).
4. The AI-tell rules in `references/tells.md`.
5. Polish.

A writing habit belongs to the writer's voice, and stays, when a voice source in force shows it, when the user says so ("keep my dashes"), or when the draft reads like a person wrote it (light depth). Otherwise the tell rules apply to it.

## Rehab workflow

Work in a folder of your own, with `input.txt`, `notes.txt`, and `output.txt` side by side. The notes are your working file: they stay out of the reply, and the user sees only the clean text and the card. Copy this checklist into `notes.txt` and tick each step in order:

```
- [ ] 1. Lock
- [ ] 2. Mark
- [ ] 3. Rewrite
- [ ] 4. Check the final text
- [ ] 5. Card
```

### 1. Lock

Write the text exactly as received to `input.txt` (for a file or screenshot, the text you read from it). The script sits in this skill's `scripts` folder, beside `tells_patterns.json`, the tell list it reads. Run it where it is, by its full path if your working folder is elsewhere. Never copy `count_tells.py` somewhere on its own, because it stops with an error when that file is missing. If the script stops with an error, fix what the error names and run it again before you count by hand. Run:

```bash
python3 scripts/count_tells.py scan input.txt --json
```

Then write `notes.txt`, before any rewriting. You rewrite from these notes and check the result against them, so anything missing here can go missing from the rewrite.

- **Main point:** the piece's point in one line, including what it argues against when it pushes back on something ("hiring a bookkeeper in January beats untangling a year of receipts in April"). It is a claim like any other.
- **Claims:** every claim, one per line: what it says, offers, promises, or limits, with its strength and conditions.
- **Protected text:** quotes, prices, names, dates, links, legal lines, and merge fields, plus every fact item the scan listed. The scan misses a name that opens a sentence ("Maria, your quote..."), all-caps names and acronyms, a name or offer that appears only in a heading or subject line, and amounts written as words ("one week"), so add those yourself.
- **Tone:** how warm and polite it is, who it talks to, its energy, any humor or mixed feelings.
- **Writer's terms:** names for things, product names, and phrases with personality that are not tells.
- **Voice and channel:** the voice in force (see "Voice") and your channel guess.
- **Depth:** your call, made as described below.

The scan reports tells per 100 words, and no list catches every AI phrase, so you choose the depth by reading. Read the draft aloud and ask of its phrasing, "Would the writer say this out loud to this reader?"

- **Light:** the draft reads like a person wrote it. Change only chatbot leftovers, hidden characters, and words the user banned. The writer's habits stay, single filler words and dashes included.
- **Standard:** an AI draft whose structure works. More than a stray phrase fails the question. Rewrite it from your notes, keeping its sections, the order of its points, and its lists as lists.
- **Deep:** an AI draft whose structure itself reads as AI: stacked one-line paragraphs, a list that should be a sentence, setup lines that carry no claim. Rewrite from your notes, and you may reorder points, turn a list into sentences, and cut those setup lines.

The user's "lighter" or "deeper" overrides your call.

### 2. Mark

Read `references/tells.md`. Mark the tells the script found, and the ones only a reader catches: disguised "not X, it's Y" moves, announcement voice, canned openers and sign-offs, fake-deep lines, announced importance, vague claims, a summary bow at the end. Keep a separate count of the reader-found ones for the card. A phrase that holds any word the script listed is one tell, counted by script, so count a phrase by reading only when the script listed none of its words. A tell you reshape, such as a main-point contrast said in one plain sentence, counts as fixed. Tells inside quotes are protected and stay. If the original contradicts itself ("today only" next to "ends Sunday"), keep both and list the conflict for the card, because only the writer knows which one is true. At light depth, skip the reader-found search.

### 3. Rewrite

At light depth, make the smallest change that removes each marked tell. At standard and deep depth, write the piece fresh from `notes.txt`, the way the writer would say it to this reader: the draft gives you the facts, the claims, and the tone, and you choose the words. A line that already sounds like a person may stay as written.

**Accuracy.** Every sentence you write carries a claim or a protected line from your notes, and every claim lands in the rewrite with its subject, strength, and conditions. "More than 20 years" keeps "more than", "would help" stays a maybe, and a result tied to its cause keeps the tie. A word that describes the offer, the business, or the result is a claim ("family-run", "same-day", "hand-stitched", "award-winning"), so keep it, said plainly. Cut words that add force and describe nothing ("truly", "incredible"), and cut the words the tell catalog lists even when they describe the offer ("comprehensive", "world-class", "seamless"), keeping any real claim they carried in the draft's own plain terms. Add nothing the draft does not say. Four kinds of addition slip into rewrites most often: a personal admission the draft never made, a stance turned into a fact about what someone did, a promise made stronger, and a next step, contact channel, or time the draft never offered. Where a specific detail would help and the draft lacks it, leave the sentence as it is and list the detail under "Only you can add or fix", since a guessed number reads as a promise the writer never made.

**Protected text** stays word for word and in its order, along with whatever touches it: a link keeps its exact form, with no punctuation glued to its end that the draft did not have. If more words ran on after a link, end the sentence at the link and move any claim in those words before it.

**The main point** survives, including what it argues against. When the piece exists to push back on something, its "not X" half stays, said once in plain words in a single sentence ("Hiring in January beats untangling receipts in April"). Any other "not X" half goes unless it carries a fact, a reassurance, a limit, or a promise the reader would miss (see `references/tells.md`, section 2).

**Sound.** Read your rewrite sentence by sentence with the out-loud question: would the writer say this exact phrase out loud to this reader? Office and template phrasing fails it ("please find attached", "kindly note that"), and so does announcement voice ("we're excited to share", "Big news!"). Say it the way the writer would talk, still adding nothing. When a more natural line would cost a fact, a claim's strength, or a condition, or would bring back a tell, keep the accurate line, because accuracy ranks above polish. Use the plain word and repeat it rather than cycling synonyms. If it would land in back-to-back sentences, rewrite one so it needs the word once. At standard and deep depth the rewrite comes out no longer than the draft: extra length almost always means an added claim, so if yours runs longer, find the sentence that carries nothing from your notes.

**Warmth** is care for the reader: thanks, a polite ask, an offer to help, a friendly word. Swap warm for warm and never leave a line curt or cold, because a colder rewrite changes how the writer comes across. Excitement is a different thing: at standard and deep depth, an announcement frame gives way to the news itself. Add no warm words or pleasantries the draft did not have. A canned line becomes the same offer in plainer words, with no new channel, time, person, or promise: "Please do not hesitate to contact me with any questions" can become "If you have any questions, I'm happy to answer them."

**Endings.** End on the draft's strongest real point or offer, said plainly, so the piece does not stop flat. That ending adds no claim. If the draft's only next step is bait ("Ready to transform your business?"), turn it into a plain next step built from what the draft offers (a link, a date, a booking). If the draft offers none, cut the bait and list "your next step" under "Only you can add or fix".

Write in the voice in force (see "Voice") and follow the channel notes in `references/channels.md`.

### 4. Check the final text

Write your rewrite to `output.txt` and run:

```bash
python3 scripts/count_tells.py compare input.txt output.txt --json
```

Then check, in this order:

- **Claims:** re-read `notes.txt` against the rewrite. A claim fails if it is missing, changed, weakened, or strengthened, and the main point fails the same way. Then name, for each sentence of the rewrite, the claim or protected line it carries, and delete any sentence that carries none.
- **Fact items** (numbers, prices, dates, names, places, links, quotes) missing or new: always a failure. Put each one back word for word ("Austin, Texas" stays "Austin, Texas") and run the compare again. You are done only when none is listed. An item the compare lists as recased is a heading word whose capitals changed, which is fine unless it is a name. A link the compare lists as gaining punctuation gets that mark taken off.
- **Meaning words** missing or new ("not", "only", "unless", "free", "up to"): the compare names the draft sentence that most likely lost each one. If that sentence still says what it said, find the one that lost the word. If the word sat inside a tell or filler line you cut (the "not" in "It's not just an app"), the claim is safe, and you note it for "What changed". If a limit, condition, or promise is gone or new, restore it.
- **Warmth:** the count adds up courtesy phrases (please, thanks, happy to), "I", "we" and "you" words, and contractions, outside the tells the script finds. A drop is normal on a standard or deep rewrite. Look for a real loss (a thank-you, a polite ask, a friendly line that turned cold) and restore it. Explain any other drop on the card in a few words. Each new warm phrase must trace to a line you converted, and remove any that don't.
- **Hashtags:** put back any hashtag the compare lists as dropped, re-cased, or added, unless the user said "drop hashtags".

If anything needed fixing, write `output.txt` again and run the whole check again. The text you show the user is the exact text of the last check.

### 5. Card

Show the clean text first, then the card. Every count names its source: "by script", "by reading", or "by hand (script didn't run)" when Python was unavailable or the script failed. Read `references/examples.md` once per chat, at this step, after your rewrite is final: the examples show the card formats, and reading them earlier pulls your wording toward theirs.

Pieces of about 150 words or more get the full card. Leave out any line or part with nothing to report:

```
AI Rehab report
Tells: [found] found ([script] by script, [reading] by reading), [fixed] fixed, [kept] kept on purpose
Facts: [items] items checked, all kept, nothing new (counted by script). Claims: [n] of [n] kept (re-read)
Warmth and courtesy: kept ([before] signals before, [after] after, [why it dropped], tone re-read)
Voice: [the voice in force, or "standard"]
Channel: [channel] (my guess). Depth: [depth]
Only you can add or fix: [missing details, contradictions, placeholders]
Say "show changes", "lighter", "deeper", or "redo for email"
```

Shorter pieces get a one-line card with tells, facts, and warmth. These illustrate the format, and your numbers come from your own script runs:

- `AI Rehab: 6 tells fixed (5 found by script, 1 by reading). Facts kept (6 items checked by script). Warmth kept (14 before, 11 after by script, from the cut opener).`
- `AI Rehab: no tells found, nothing changed (light touch). Facts kept (5 items checked by script).`
- `AI Rehab: 1 tell found by script and kept as your voice (light touch). Facts kept (4 items checked by script).`
- `AI Rehab: 4 tells fixed (found by script), 1 kept on purpose (a placeholder only you can fill). Facts kept (3 items checked by script). Warmth unchanged.`
- `Needs your eyes: "only if you've attended at least 2 sessions" lost the word "only".`

What goes on a card:

- **Needs your eyes** starts the card only when the last check still shows a missing or new fact item, or a claim you could not restore. Name each one. A contradiction in the original goes under "Only you can add or fix" instead.
- **Warmth:** a drop says why ("from the cut opener"), and no change says "Warmth unchanged". A rise says "no new phrases" when the compare lists none. A new warm phrase that replaced a canned line is named with its source ("'let me know' replaces the canned sign-off").
- **Kept as your voice** needs a reason from the order of priority: a voice in force, the user's own words, or light depth. Without one, fix the tell. **Kept on purpose** covers tells inside quotes and placeholders only the writer can fill.
- **Under a one-line card**, add only the lines that apply, each on its own line, in this order: "Only you can add or fix: ...", the voice in force if there is one ("Voice: from your Instructions for Claude"), the hashtag line, then the voice invitation.
- **Hashtag line**, when the draft has hashtags: "Say 'drop hashtags' to remove them."
- **Voice invitation**, when no voice is in force: one last line under the first card of the chat, "Want it in your own voice? Paste 3 things you wrote." Once per chat, and never after "don't ask about voice".
- **"Show changes"** adds a "What changed" list (each tell, before and after) and a "Kept on purpose" list.
- Do not offer "lighter" when the depth is already light.

## Voice

AI Rehab never adds a voice and never removes one.

- A voice already in force stays in force, and the card names it: a voice the user names or pastes now, admin rules for their organization, project instructions, the user's own Claude instructions, a voice skill that loaded on its own for this request, or the user's choice earlier in this chat.
- Do not load a voice skill that did not load on its own. Do not take a brand voice from project files unless project instructions or the user point to it.
- When sources disagree: the user's request in this chat wins, then organization rules, then project instructions, then the user's own instructions, then the user's earlier choice. If that does not settle it, ask one short question.
- The voice is settled in step 1, before any rewriting, and every depth writes in it.
- With no voice in force, the card says "Voice: standard". At light depth, `references/default-voice.md` shapes only the words you write to replace a tell. At standard and deep depth, the draft's own tone and terms lead, and the default fills only the gaps.
- "Build my voice" or 3 pasted samples starts the quick-start in `references/voice-card.md`. It is optional.

## Plain-word options

Nothing is required. A phrase changes the setting for the rest of the chat.

- "lighter" / "deeper": change the depth.
- "for email", "for LinkedIn", "for a caption", "for a sales page": set the channel.
- "show changes": add the What changed and Kept on purpose lists.
- "keep my dashes": treat that habit as voice.
- "drop hashtags", "drop emojis": remove them. Emoji bullets in a list go in every case.
- "build my voice": start the quick-start.
- "don't ask about voice": stop the voice invitation line.
- "add 'X' to my banned words": rehab treats X as a tell from now on, and hand back the updated always-on line (see `references/voice-card.md`) for the user to save.
- "skip rehab": skip it for this message. "stop rehab": explain how to remove the always-on line from their settings.

In Claude Code, the same phrases may arrive on an `ARGUMENTS:` line.

## Banned words from the user

Words the user banned, listed in their instructions or added with the phrase above, are tells everywhere.

## Never

- Never invent facts, numbers, names, quotes, results, or experiences.
- Never say the text will pass an AI detector or that no one will be able to tell.
- Never print a success line for a check that failed or did not run.
- Never change protected text.

## Other languages

Rehab English fully. For other languages, fix only the tells that cross languages (chatbot leftovers, hidden characters, dash habits, repeated sentence shapes), keep the writer's punctuation habits, and say so on the card. In mixed text, follow the main language and leave lines in the other language as written.

## Files

- `scripts/count_tells.py`: run it, don't read it. `scan FILE --json` lists tells, tells per 100 words, fact items, meaning words, and the warmth count. `compare BEFORE AFTER --json` lists what changed between the two.
- `references/tells.md`: the tell catalog with warm fixes.
- `references/examples.md`: worked before and after examples with their cards.
- `references/channels.md`: channel notes.
- `references/default-voice.md`: the plain, warm default for replacement wording.
- `references/voice-card.md`: the voice card, quick-start, and always-on lines.
