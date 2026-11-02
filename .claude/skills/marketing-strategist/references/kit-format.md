# The Promotion Kit format

The exact output contract. One editable Eden note, titled `Promotion Kit: <offer>`, on the "Promotion" board. Sections in this order, always, so weekly runs can find and replace the right block. Write note bodies without blank lines between blocks; Eden's editor spaces blocks itself.

## Writing rules (non-negotiable)

- One reader, singular. Every line addresses one person who has the problem.
- Plain spoken language, short sentences, in the user's voice at its most direct, taken from their own posts. A promotion that could sit under any account in the niche is a failed promotion.
- Facts over adjectives. Cut amazing, revolutionary, game-changing, and the banned list: delve, tapestry, unleash, unlock, leverage, robust, journey, landscape, navigate, foster, harness, vibrant, dynamic, holistic, paradigm.
- No em dashes. Periods, commas, colons.
- Banned AI frames, at most once in the whole kit if truly needed: "X is not Y, it's Z", "You don't need X, you need Y", "Stop X. Start Y", "Most people think X".
- Never reuse a run of 8 or more words from any ad or post read this run.
- Found and inferred stay separate. Inferred lines end with "(suggestion)". Claims the user must be able to prove end with "(prove this)".
- No fabricated testimonials, statistics, results, reviews, or screenshots. No income or health promises. Urgency and scarcity literally true or cut.
- Price after value, anchored once. Guarantee in the reader's terms.

## The note

```markdown
# Promotion Kit: {offer name}

{One line: who it is for, the result with number and timeframe, the price. Then the date built and the date of the last weekly run.}

## Inputs

- Offer Blueprint: {note title, or "from conversation"}. Big idea: {…}. Mechanism: {…}. Outcome: {…}. Guarantee: {…}. Price: {…}.
- Brand strategy: {note title, or "none"}. Audience: {…}. Worldview: {…}. Pillars: {…}.
- Best posts read: {N posts from @handle on platform; the two topics that already earn saves and replies}.
- Proof on hand: {list}. Proof gaps: {list, each marked (prove this)}.

## Diagnosis

- Awareness: {stage}. {One line on why, from the inputs.}
- Sophistication: level {N}, {name}. Found: {what the ads and top posts showed, with counts}. Inferred: {what you conclude}. {Or: "Unresearched; inferred from the inputs alone."}
- Escalation move: {the one thing this market still responds to: named mechanism, stronger proof, easier version, identity}.
- Congruence line: {the one promise every promotion points at and the page must say above the fold}.
- Rejected angles: {from the settings note, or "none yet"}.

## Social promotions

{Thirty entries, one per day, numbered. Group by week with a "Week 1" heading and a one-line angle plan for the week.}

### Week 1: {five angles in order}

**1. {Day, date} · {format} · {angle} · {lead type} · {where it runs}**
{The promotion, ready to paste. Reply plugs are one or two lines and name the post they go under ("under today's post about …"). Inside-the-newsletter plugs are two to five lines and name where in the piece they sit. Standalone, story, objection, and proof posts are complete.}
Congruence: {what the page must say for this one to work, only when it differs from the kit's congruence line}.
**2. …**

## Email promotions

{"Launch sequence, {N} emails, opens {date}, closes {date}" or "Evergreen sequence, {N} emails over {N} days from sign-up".}

### Email 1 of {N}: {the job: the open, the mechanism, the proof, the fit, the stakes, the close, last call}

- Lead: {type}. Send: {day or offset}. Link: {the one link}. Call to action: {one}.
- Subject A ({family}): {…}
- Subject B ({different family}): {…}
  {The email body. First line is a different sentence from both subjects.}

### Email 2 of {N}: …

## Landing page brief

{For a page writer. It is a brief, never the page.}

- Reader: awareness {stage}, market level {N}.
- Lead type and opening hook: {the lead}; {the winning hook, verbatim}.
- Big idea: {…}. Mechanism: {…}. Guarantee: {…}. Price framing: {anchor and the outcome it is framed against}.
- Proof available: {list}. Proof gaps: {list, (prove this)}.
- For: {…}. Not for: {…}.
- The one call to action: {…}.
- Congruence line: {…}.

## Promotion log

| Date   | #   | Format   | Angle   | Lead   | Where                    | Response |
| ------ | --- | -------- | ------- | ------ | ------------------------ | -------- |
| {date} | 1   | {format} | {angle} | {lead} | {platform or newsletter} |          |

{One row per promotion written. Response stays blank until the user fills it or reports it. "Saved as draft" goes in the Where column when a promo went to the scheduler.}
```

## Rotation rules the note must visibly obey

- Five distinct angles in every week block: problem, mechanism, proof, story or identity, offer. Never the same angle twice inside a week.
- Most days a reply plug or an inside-the-newsletter plug. Standalone promos two or three times a week. A story promo, an objection post, and a proof post appear at least once each in the month.
- One lead per piece, named in the entry header.
- Every entry runs somewhere specific: a platform, "newsletter", or "under post about …".

## Weekly runs edit in place

The weekly run does not create a new note. It replaces the coming week's block under "Social promotions" (or appends a "Week N" block when the month has run out), appends rows to the Promotion log, and updates the "last weekly run" date in the first line. Everything else stays unless the diagnosis changed, and a changed diagnosis is a correction run, which rewrites the promotions that depended on it.

## Styled delivery

The kit is a document. In order of preference:

1. **HTML artifact or file**: `assets/promotion-kit-template.html`. Fill the `{{…}}` slots, repeat the marked day and email blocks, keep the design.
2. **Markdown**: the template above, exactly.

In both cases the markdown version is what gets saved to the Eden note; the HTML is a view of it. In chat, close with three lines only: the diagnosis in one sentence, the first promotion to run and when, and the one-line drafts offer.
