# The ideas memo format

The exact output contract for the weekly memo, plus the structure of the two standing notes. The memo is a document with real markdown tables. Every section must stand alone: a reader who jumps straight to the short-form table knows what to make and why.

## Writing rules (non-negotiable)

- **Plain spoken language**, short sentences, like texting a smart friend. Every idea must pass the say-it-out-loud test.
- **No em dashes.** Periods, commas, colons.
- **No analyst jargon**: salience, narrative, paradigm, discourse, reframe as a noun, "X is being challenged by Y". No academic hedging.
- **Banned AI frames**, at most once in the whole memo if truly needed: "X is not Y, it's Z", "You don't need X, you need Y", "Stop X. Start Y", "Most people think X".
- Never coin a shorthand for a finding and refer back to it. Name the actual thing every time.
- Post ids never appear in prose. Receipts render as data lines.
- Titles and claims get no colons and no headline punctuation.
- Never diagnose, dismiss, or redefine a medical or mental-health condition for a hook.
- Never reuse a run of 8 or more words from any receipt post.
- Idea = one literal 8 to 20 word claim a cold reader understands. "Talk about pricing" is not an idea.
- Honest when thin: label evidence-light rows, say which lane came up short, still reach ten short-form rows.

## The memo (markdown)

Note title: `Weekly ideas — YYYY-MM-DD`. Section order is fixed.

```markdown
# Weekly ideas — {date}

**This week in one line:** {the read, under 30 words}

## Last week's picks graded

| Pick                              | What you posted                         | Result                    | Grade               |
| --------------------------------- | --------------------------------------- | ------------------------- | ------------------- |
| {row number and claim, truncated} | {title or first words, or "not posted"} | {N.N}x baseline · {reach} | {one honest phrase} |

{First run: the single line "First run, nothing to grade yet." instead of the table.}

## What is moving

### 1. {finding claim, one arguable sentence}

`{new | building | saturating}` · first seen {date} {· early signal, if unconfirmed}

{2 to 3 sentences: what is happening and why it is popping, under 60 words}

- @{handle} ({platform}) · {N.N}x baseline · {reach} · "{hook, verbatim, short}" · {why it popped, one line}
- @{handle} ({platform}) · {N.N}x baseline · {reach} · "{hook}" · {note}

### 2. {up to three findings total}

## Your scoreboard

| Post                   | Multiple vs baseline | Reach            | Read                                           | Top question or pushback                 |
| ---------------------- | -------------------- | ---------------- | ---------------------------------------------- | ---------------------------------------- |
| {title or first words} | {N.N}x               | {views or likes} | {pillar · format · hook shape, under 10 words} | {what the replies asked, or "none seen"} |

{One line: which pillar, format, and hook shape carried the month. Performance read only.}

## From your library

- **{item title}** ({capture | highlight | note | idea bank}) · {pillar} · "{short verbatim excerpt}" · {agrees with winner X | clashes with winner X | never published} · could become: {one-line claim}
  {three to six lines}

## Short-form ideas

| #   | Idea                 | Pillar   | From            | Platform and format | Openers                             |
| --- | -------------------- | -------- | --------------- | ------------------- | ----------------------------------- |
| 1   | {8 to 20 word claim} | {pillar} | {source · rule} | {platform · format} | {2 first lines, separated by " / "} |
| ... | at least 10 rows     |          |                 |                     |                                     |

## Long-form ideas

| #   | Working title           | Claim it builds                  | Beats                              | Feeds                                                     | From            |
| --- | ----------------------- | -------------------------------- | ---------------------------------- | --------------------------------------------------------- | --------------- |
| 1   | {plain title, no colon} | {the one claim the piece proves} | {3 to 5 beats, separated by " → "} | {short-form rows it can be cut into, e.g. "rows 2, 5, 8"} | {source · rule} |
| ... | 3 to 5 rows             |                                  |                                    |                                                           |                 |

## Experiment

{One thing worth testing that the data suggests but does not prove. What to try, and what would count as it working.}

## Stop doing

{One thing the scoreboard says is not working, said kindly and plainly. Omit the section if nothing qualifies.}

## Watchlist

- {creator, pattern, or topic} ({kind}) · {why it is worth watching next week, one line}
  {2 to 4 entries. Never the user's own accounts or their radar creators.}

---

{One line: calls used, which lanes fed the memo, anything that came up dry or partial.}
```

## Table contracts

**Short-form ideas** (at least 10 rows):

- Rows 1 to 3 evolve the creator's own winners, one evolve rule each, named in From.
- At least two rows come from library seeds when seeds exist, named by item title in From.
- Every finding feeds at least one row through its structure. The From cell names the finding and the borrowed structure in plain words ("finding 2 · specific moment, failed assumption, earned rule").
- Reruns: at most 2 of 10, each labeled "rerun" in From, never counted toward the ten new ideas.
- Vary hook shapes and pillars across the table. Two rows with the same opener shape and the same pillar means one gets cut.
- Openers: two first-line options in the creator's own vocabulary, ready to paste.
- Evidence-light rows say so in From ("own winner · inference").

**Long-form ideas** (3 to 5 rows):

- At least one direct sequel to the creator's biggest long-form winner, one rung down the ladder (rule 2).
- At least one built from a library item.
- Beats are the spine of the piece, 3 to 5 moves, each a few words.
- Feeds names the short-form rows the piece can be cut into afterward, so the week compounds.

**From column** (both tables): the source and the rule, always. Formats: "winner: {post, first words} {N.N}x · rule {n}, {what changed}", "finding {n} · {structure borrowed}", "library: {item title} · rule 11 with winner {x}", "rerun · winner {post} {N.N}x, {age}".

## The Brand throughline note (standing, under 800 words)

```markdown
# Brand throughline

**Throughline:** {one sentence}

## Who it is for

{2 to 4 lines}

## Enemy and promise

{what they are against, what they promise, 2 to 4 lines}

## Pillars

### {Pillar name}

- Recurring claims: {2 to 4 claims in the creator's words}
- The angle that is theirs: {one line}
  {2 to 5 pillars}

## Proven formats and hook shapes

- {format or hook shape} · {evidence in one phrase, e.g. "3 of top 10 lifetime"}

## Vocabulary

- **{named concept}**: {one-line meaning}

## Topic ledger

| Topic | Angles published | Depth reached (rung) | Last touched |
| ----- | ---------------- | -------------------- | ------------ |

{capped at 30 topics; retire the weakest when full}

## Do not do

- {one line each}

## Change log

- {YYYY-MM-DD}: {one line}
```

## The Strategist settings note (standing)

```markdown
# Strategist settings

- Workspace: {name}
- Own accounts: {platform @handle, resolved}
- Topics: {2 to 5}
- Radar creators: {0 to 8, platform @handle}
- Where ideas live: {board or tag name, or "whole library"}
- Cadence: {what they told you, or "unset"}
- Setup date: {YYYY-MM-DD}
- Routine: {none | claude.ai scheduled task, {when} | Claude Code cron, {when}}
- Last run: {YYYY-MM-DD}
- Last lifetime read: {YYYY-MM-DD}

## Used library items (newest 40)

- {YYYY-MM-DD} · {item title} · {memo date it fed}
```

## Styled delivery

The memo is a document, not a chat message. In order of preference:

1. **HTML artifact / file**: `assets/ideas-memo-template.html`. Replace the `{{...}}` slots and repeat the marked row and finding blocks. Keep its design; one accent is already chosen.
2. **Markdown**: the template above, exactly. Real tables, bold labels.

In both cases, ALSO save the markdown to the Eden note (that is next week's memory). In chat, after delivering, close with three lines: the surest bet, where it is saved, and "Tell me the row numbers you want and I'll draft them." On the first delivery only, add the one-line routine offer.
