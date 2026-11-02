# The outline format

The exact output contract. The deliverable is one editable Eden note. A writer who opens only this note, with no memory of the chat, can draft the piece beat by beat.

## Writing rules (non-negotiable)

- Every sample line, hook, and reframe is written in the writer's voice: the register and vocabulary from their answers. Never a guru tone. Sample lines illustrate; they are never the draft.
- Plain spoken language. Short words, short sentences. No em dashes: use periods, commas, colons.
- Never draft the piece. A beat carries a job, a claim, evidence, and a budget, never paragraphs of prose.
- Never invent statistics, studies, quotes, results, or stories. Every specific in the outline traces to the interview, a saved item they gave you, or a piece retrieved this session.
- Never carry another creator's numbers, names, story, or phrasing into a title, hook, or beat. Skeletons only.
- Banned in your own prose: "X, not Y" and "not X, it's Y" constructions; "It's not about X"; delve, tapestry, unleash, unlock, leverage, robust, journey, landscape, navigate, foster, harness, vibrant, dynamic, holistic, paradigm.
- The market signal names only pieces you actually retrieved. No research, no signal: say so in one line.
- The note is editable. Placeholders in square brackets name the exact detail the writer fills: `[the number of unread articles that morning]`, never `[insert detail]`.

## Note title

`Long-Form Outline: [working title]`

The working title is the primary package's title (script) or the piece's working name (newsletter). Update the note title with `eden_rename_note` if the package changes.

## Section order

Every outline note carries these sections, in this order, with these headings.

```markdown
# Long-Form Outline: {working title}

{Format · platform · target length or runtime · date}

## Package

**Primary:** {title or subject line} · {family}
{Newsletter: the paired opening line. Script: thumbnail direction + what the first five seconds must confirm.}
**Alternatives:** {two more, each with its family and one line on the different expectation it tests}
**Market signal:** {lane searched · observed families · recurring promises · saturated · open lanes. Only retrieved pieces. Or: "no research this session, families from the craft reference."}

## Opening contract

This piece helps {reader} move from {starting state} to {promised change} through {mechanism}, supported by {proof}.

## The reframe

{Most people think X. Actually Y. Two to four lines in the writer's voice, from the interview.}

## Prewriting card

| Field                  | Answer |
| ---------------------- | ------ |
| Working topic          |        |
| Reader                 |        |
| Current belief         |        |
| Needed belief          |        |
| Central claim          |        |
| Evidence               |        |
| Application            |        |
| Primary call to action |        |

## Route

**Chosen:** {route name}: {why, one line}
**Also considered:** {route two}: {one line on why it lost} · {route three}: {one line}

## Beat-by-beat outline

### Beat 1: {beat name} ({budget: words or % of runtime and minutes})

- **Job:** {what this beat does to the reader's understanding}
- **Reader question:** {the question it answers}
- **Claim:** {the new claim or change in understanding}
- **Evidence:** {the specific story, example, number, or case from the interview}
- **Re-hook:** {the loop it opens or the transition it makes}
- **Flags:** {specificity bomb placeholder in brackets · vulnerability moment · named method introduced here, when they apply}

### Beat 2: ...

## Re-hook map

| Loop                                 | Opens in | Closes in |
| ------------------------------------ | -------- | --------- |
| {the question the reader is holding} | Beat {n} | Beat {n}  |

## Ending

{Open question, resonant image, or identity reframe: which one, and the sample line in their voice.}
{Primary call to action, after the resolution, one line.}

## Emotional arc

{Beat by beat: the register. Recognized → uncomfortable → hopeful, named per beat.}

## Differentiation note

{Two or three things that would never appear in the generic version of this piece.}

## Budget

{Newsletter: total words and the per-beat split. Script: total runtime, the per-beat share and minutes at 140 to 160 words a minute.}

## Adaptation (only when both formats were asked for)

{What changes for the second format: package, budgets, retention language, opening.}
```

## Beat rules

- Every beat has a distinct job. Two beats doing the same job get combined.
- Every open loop in the re-hook map closes somewhere. A loop with no closing beat is a bug.
- Flags live inside the beats where they land. Specificity bombs are placeholders naming the exact detail. The vulnerability moment sits where the writer said they still struggle. The named method (if any) is introduced once and then used by name.
- The ending never thanks the reader. The primary call to action follows the resolution.
- Budgets sum to the target. Newsletter: 1,200 to 2,000 words unless the writer set another target. Script: the runtime they named.

## Styled delivery

In order of preference:

1. **HTML artifact / file**: use `assets/outline-template.html`. Fill the `{{...}}` slots and repeat the marked beat block once per beat. Keep its design; do not restyle it.
2. **Markdown**: the section order above, exactly.

In every case, ALSO save the markdown version to the Eden note `Long-Form Outline: [working title]` on the "Long-form outlines" board. The note is the deliverable; the artifact is a nicer view of it. In chat, after delivering, close with three lines only: the one beat you would draft first and why; the offer to adjust structure, add or cut beats, or refine sample lines; and the reminder that they can open a new chat, paste the outline, and draft from it beat by beat.
