# Interview, stress test, routes, packaging research

The step-by-step method, with the gates, budgets, and tool names. The skill summary is not enough; this is the method. Every stage ends at a gate: present, ask, wait. Never carry the writer past a gate they have not answered.

## Budgets for one outline

- **Research calls: at most 8 per outline** (title studies, social searches, full post reads). Workspace reads (settings note, ideas memo, the writer's saved items) and note writes sit outside this number.
- Retry a failed call once. After a second failure, say what is missing and build from the craft reference.
- Spend calls on different questions, never on rewording one query.
- If your environment can run parallel tool calls or subagents, run the packaging lanes at once. Otherwise run them one at a time inside the same budget.

## Stage 0: home base

1. Resolve the workspace (`eden_list_workspaces` if more than one; record the choice in the settings note).
2. `eden_search_workspace_items` for a board named **"Long-form outlines"**.
3. **First session** (no board): before the interview, ask in one message which formats they publish (newsletter or article, YouTube script, or both), which platforms carry them (Substack, a blog, YouTube, X articles, LinkedIn newsletter), and whether they prefer the deep dive or the quick pass by default. Then `eden_create_board` "Long-form outlines" and `eden_create_note` on it titled **"Outliner settings"** with the answers.
4. **Every later session**: read "Outliner settings" with `eden_get_note_markdown`. Read the titles of past outline notes on the board so you never propose an angle they already outlined. Update the settings note with `eden_update_note` (pass the `contentHash` you were given as `baseContentHash`) when the writer changes a preference.
5. **Starting material.** If the workspace has a note titled **"Weekly ideas"** on a board named **"Content Strategist"** (the Weekly Content Strategist workflow writes it), offer to start from one of its long-form rows. Read it with `eden_get_note_markdown`. An older "Weekly strategy" memo on a "Weekly strategy" board works the same way.

## Stage 1: the source map

Sort whatever the writer brings into four lanes without announcing them:

- **The writer's position**: what they believe, their draft, their notes.
- **Subject evidence**: proof the claim is true (experience, cases, data).
- **Structural references**: pieces they want to learn from.
- **Market evidence**: what performs in the niche.

Rules:

- If they gave a link, read it in full before asking anything: `eden_read_social_post` for a post, article, or video (transcript included when available). If they name a saved Eden item, find it with `eden_search_workspace_items` or `eden_find_workspace_items`, then read it with `eden_read_card` (a saved card) or `eden_get_note_markdown` (a note).
- Never let market success stand in for subject proof. A topic that performs is a packaging fact, never evidence the writer's claim is true.
- Ask which format if it is not obvious: newsletter or article, or YouTube script. Both from one idea means build once and add an adaptation block at the end.

**Gate 1**: confirm the format and what they brought in two lines. Wait.

## Stage 2: the interview

Offer two depths and let them choose (default from the settings note):

**Deep dive**: one question at a time, probe for specificity, in this order.

1. Core topic, and what got them thinking about it.
2. What most people get wrong about it (most people think X, but actually Y).
3. The specific personal moment that proves it: numbers, places, ages, sensations.
4. Who the reader is, and the shame or frustration they secretly carry.
5. What they want the reader to feel afterward.
6. The metaphor or image that makes it click.
7. What they are still uncertain about.

**Quick pass**: four questions in one message, then infer the rest and show every inference for correction.

1. What problem or situation is this about?
2. What do people get wrong, and where does the default advice fall short?
3. What is the better way to think about it?
4. What real moment proves it?

**Arrived with a draft or transcript**: skip to extraction. Read it in full and locate the strongest transformation, argument, mechanism, conflict, proof, story, and unexpected moment. The opening topic of a draft is often the weakest angle in it; say so when true.

Probe vague answers. "It changed everything" gets "what did Tuesday look like before, and after?" Ask for the number, the place, the sentence someone said.

Close the stage by filling the **prewriting card** and reading it back:

| Field                  | What goes here                       |
| ---------------------- | ------------------------------------ |
| Working topic          | one line                             |
| Reader                 | who, and what they secretly carry    |
| Current belief         | what the reader thinks now           |
| Needed belief          | what they must believe by the end    |
| Central claim          | one sentence                         |
| Evidence               | the specific moments, cases, numbers |
| Application            | what the reader does with it         |
| Primary call to action | the one ask after the resolution     |

**Gate 2**: read the card back, ask what to revise. Wait. Do not move on until they confirm.

## Stage 3: the stress test

Push the perspective until the parts only this writer could say show up. Present five scannable blocks:

1. **Paradoxes**: two or three tensions inside the topic, one line each.
2. **Concept expansion**: three to five supporting ideas, including a possible named method (two to four words), an identity shift, and a second-order consequence.
3. **Specificity bombs**: three to five exact numbers, moments, names, or sensations from the interview that a generic version could never contain.
4. **Differentiation check**: two or three things that would never appear in the generic version of this piece.
5. **Vulnerability hook**: the place they still struggle, said plainly.

Everything here comes from their answers. Never invent a number, a moment, or a struggle to fill a block.

**Gate 3**: ask what resonates and what is wrong. Wait. Revise the card if their answer changes it.

## Stage 4: angle and structure routes

**Angle routes** (only when more than one viable piece is hiding in the material): present three to five angle routes that differ in what the reader receives. Each: central claim, promise, tension, proof, credibility risk. Recommend one. Ask. Wait.

**References**: ask for pieces or creators to learn from. If they give any, read the actual post or transcript (`eden_read_social_post`; `eden_resolve_creator` then `eden_analyze_creator` with `since: "all"` for a creator they name) and map the mechanism: how it opens, where credibility lands, each section's job, the loops, the ending. Never the wording. These reads count against the 8-call budget.

**Structure routes**: propose exactly three from the six in `craft-reference.md` (contrarian argument, story-led transformation, framework or tutorial, research-led explainer, case study, the list). Each as a four-line route card:

1. Route name, central angle, thesis.
2. Reader promise and opening idea.
3. Major beats in one line.
4. Strength and risk.

Recommend one and say why in one line. Hybrid only when one route stays dominant.

**Gate 4**: wait for the pick.

## Stage 5: packaging research

Never write titles or subject lines from memory. Research how the niche packages similar promises on the platforms this writer publishes to, judged against each creator's own baseline, across a range of creators.

Lanes, inside the 8-call budget:

- **Titles lane** (1 to 2 calls): `eden_study_top_titles` with `niche` set to the topic, `platform` matching where they publish (`youtube` for scripts, `substack` for newsletters and articles, `twitter` for X articles), and `topic` set to the piece's subject so each skeleton comes back refilled as an example. It returns each headline's skeleton, the move that makes it pull, and a `doNotReuse` list. Short-form carries no title; never study a platform they did not ask about.
- **Performance lane** (2 to 3 calls): `eden_search_social_content`, `scope: {kind: "global"}`, `orderBy: "outlier"`, `platforms` limited to where they publish, `since: "year"` for the durable families and `since: "month"` for what is moving now, `minOutlierScore: 3`, `limit` 8 to 10. Read titles and openings for the promise families they use.
- **Pivotal reads** (up to 2 calls): `eden_read_social_post` on the one or two pieces whose package sits closest to this outline's promise. Read for mechanism and promise integrity.

Extract skeletons: the frame with the creator-specific parts lifted out, in brackets with slots. Reuse the skeleton, replace the substance. Never carry another creator's numbers, names, story, or phrasing. If a proposed title would survive being moved to a different piece unchanged, it is unfinished.

Report a compact **market signal** before the options: lane searched, observed families, recurring promises, saturated approaches, open opportunities. Only pieces actually retrieved appear here. If research is unavailable (tool errors, out of credits), say so in one line and build from the families in `craft-reference.md`.

Then generate **five to eight options across different families**:

- **Newsletter**: each subject line paired with a different opening line. Different sentences; the subject gets the open, the opening keeps the reader.
- **Script**: pair the strongest three with a thumbnail direction that adds information the title withholds, and state what the first five seconds must confirm.

Recommend one primary package and two alternatives. Promise integrity is the gate: title, opening, body, and payoff describe the same piece.

**Gate 5**: wait for the pick before writing the note.

## Stage 6: the outline note

Follow `outline-format.md` exactly. One note, titled `Long-Form Outline: [working title]`, created with `eden_create_note` on the "Long-form outlines" board. Revisions update the same note with `eden_update_note` and the note's `baseContentHash`; never create a second note for the same piece.

## Revisions

When the writer changes the reader, rejects an angle, removes a source, or brings better evidence, name which downstream decisions it touches and rerun only those. Fix in this order: broken promise; missing argument, proof, or payoff; flat progression; weak opening; unresolved loops; then polish.
