# The kit run

How a Promotion Kit gets built and refreshed: exact tools, budgets, gates. The skill summary is not enough; this is the method. Read `craft-reference.md` alongside it.

## Budgets

- **Market diagnosis: at most 8 research calls per kit.** That covers `eden_search_ads`, `eden_search_social_content`, and `eden_read_social_post` together. Spend them on different questions, never on rewording one query.
- **Own posts: at most 3 calls** (`eden_get_analytics`, `eden_list_analytics_posts`, `eden_analyze_creator`). Their posts are voice and topic evidence, never market evidence.
- Workspace reads (finding and reading the blueprint, strategy, kit, and settings notes) and delivery writes sit outside these numbers. The whole first run stays under roughly 22 tool calls.
- Weekly runs spend at most 2 research calls, and only when the log shows an angle died and a replacement needs grounding.
- If your environment can run subagents or parallel tool calls, run the own-posts lane and the market lane at once; otherwise run them one at a time inside the budget. No more than four independent calls in one batch.
- Retry a failed call once. After a second failure, record what is missing and write from verified inputs.

## Three kinds of run

Decide which run this is before doing anything else:

1. **First kit**: no "Promotion Kit:" note exists for this offer. Full run, steps 0 to 5.
2. **Weekly run** ("Write this week's promotions"): a kit note exists. Read the log, write the next seven, update the same note. Steps 0, 6, 5.
3. **Correction** (the user pushes back on the diagnosis, an angle, or an email): redo the diagnosis line that was wrong, then rewrite every promotion that depended on it. Never patch one line and leave the rest pointing at the old read. Record the rejected angle in the settings note.

## Step 0: home base and memory

1. Resolve the workspace (`eden_list_workspaces` if more than one; remember the choice in the settings note).
2. `eden_search_workspace_items` for a board named **"Promotion"**. Missing: `eden_create_board` "Promotion".
3. `eden_search_workspace_items` for notes titled **"Promotion Kit:"** on that board. One per offer. If the user named an offer, pick that one; if several exist and they did not, ask which in one line.
4. Find or create the **"Promotion settings"** note on the board. It records: the workspace choice, where they post and how often, which newsletter they run, their resolved handles, launch window or evergreen, and every rejected angle. Read it every run; never re-ask what it already holds.
5. Weekly run: read the kit note with `eden_get_note_markdown` and keep its `contentHash`. You will need it as `baseContentHash` on `eden_update_note`.

## Step 1: the inputs

Open with one compact message that says what you are looking for and that you can work from a conversation alone. Then look before you ask:

| Input                   | Find it                                                                                                                                                                                                         | Lift from it                                                                |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Offer Blueprint         | `eden_search_workspace_items` for a note titled "Offer Blueprint:" (the Offer Consultant workflow, or the Custom AI, writes it)                                                                                 | Big idea, mechanism, pain points, quantifiable outcome, guarantee, price    |
| Personal Brand Strategy | `eden_search_workspace_items` for "Personal Brand Strategy:" (the Personal Brand Strategist workflow keeps it on the "Personal brand strategy" board)                                                           | Audience, worldview, pillars                                                |
| Their best posts        | `eden_get_analytics`, then `eden_list_analytics_posts` sorted by the metric that matters for them; or `eden_resolve_creator` then `eden_analyze_creator` with `since: "month"` when analytics are not connected | Their voice at its most direct; which topics already earn saves and replies |

Read each note with `eden_get_note_markdown`. Confirm what you lifted in one line each, so a wrong assumption gets caught before it shapes a month of copy. Never guess a handle; `eden_resolve_creator` every one, and if it comes back ambiguous, ask which candidate before going on.

**Interview only what is missing, one question per message**, in this order: what they sell and the result with a number and a timeframe; who buys and what they tried before; mechanism, guarantee, price; where they post and how often; launch window or always open; what proof they actually have. Push once for numbers where they give adjectives. Record every proof gap; the kit flags each one.

Gate: do not move to step 2 until you can state the offer in one sentence (who, gets what, by when, for how much, with what guarantee) and the user has confirmed it.

## Step 2: the diagnosis (market lane, 8 calls)

Two lines before any copy: awareness stage and sophistication level. Research places the level; the inputs place the reader.

- **Spend-proven ads** (2 to 3 `eden_search_ads` calls): the offer's category and its nearest neighbor. Read the hooks and promises. Ads that have run for months are paid proof of what this market still responds to.
- **Top posts in the niche** (2 to 3 `eden_search_social_content` calls, `scope: {kind: "global"}`, `orderBy: "outlier"`, `since: "month"`, `minOutlierScore: 3`, `limit` 5 to 8): queries from the offer's outcome and the audience's pain, not the product name.
- **Full reads** (up to 2 `eden_read_social_post`): the posts whose hook you need to see whole.

Then place the level using `craft-reference.md` section 1: everyone promising the outcome with no how, level 2 or 3; everyone naming mechanisms, level 4; winners barely mentioning the product, level 5. Write what you found and what you infer as two separate lines. If research came back thin, say the level is inferred from the inputs alone.

Also produce, from the same reads, the **congruence line**: the one promise every promotion points at and the landing page must say above the fold.

If the user's requested angle fights the diagnosis, say so in one line, then write what they asked.

Gate: the Diagnosis block is written and shown in chat before any promotion copy. This is the one mid-run pause on a first kit. Wait for an ok or a correction; a correction here saves rewriting thirty promotions later.

## Step 3: lead and hooks

Pick one lead per piece from the six (`craft-reference.md` section 2). Awareness sets directness; sophistication sets substance. Prefer the more direct lead when two fit. Never stack leads.

For the standalone promos and the emails, write hook variants that differ by angle (problem call-out, mechanism tease, proof-forward, identity or story open, offer-direct) and run each through the four tests. Ship only what passes all four. Hooks that could belong to any account in the niche fail test two.

Voice: their own posts pulled in step 1 are the reference. Match vocabulary and cadence at their most direct. Never reuse a run of 8 or more words from any ad or post you read.

## Step 4: write the kit

Follow `kit-format.md` exactly for the note: Inputs, Diagnosis, Social promotions (a month, numbered, one per day), Email promotions, Landing page brief, Promotion log.

Rules that always hold while writing:

- Five angles per week minimum (problem, mechanism, proof, story or identity, offer); never the same angle twice in one week.
- Most days a reply plug or an inside-the-newsletter plug; standalone promos two or three times a week; a story promo, an objection post, and a proof post at least once each in the month.
- Match the day's angle to the content they said they post that day where you know it.
- Launch window with a real close date: a launch sequence of five to seven emails. Always open: an evergreen sequence over one to two weeks.
- Each email: one lead type, one idea, one link, one call to action, two subject options from different families, subject and first line different sentences.
- The landing page brief is a brief. It is handed to a page writer; it never becomes the page.
- Mark every inferred line "(suggestion)". Mark every claim they must prove "(prove this)". Keep found and inferred separate.

## Step 5: deliver, log, offer

1. **Always** save to Eden. First kit: `eden_create_note` on the "Promotion" board titled `Promotion Kit: <offer>`. Weekly run: `eden_update_note` on the existing note with `baseContentHash` from step 0. Then update the settings note if anything changed.
2. Styled copy where you can: the HTML artifact or file from `assets/promotion-kit-template.html`; otherwise the markdown from `kit-format.md`.
3. Close in chat with three lines: the diagnosis in one sentence, the first promotion to run and when, and the one-line drafts offer: "Want this week's standalone promos saved as drafts in your Eden scheduler?"
4. **The drafts close**, only if they say yes: `eden_list_schedules` first (connected platforms, timezone). Then `eden_schedule_post` with `draft: true` for each standalone promo, story promo, objection post, and proof post in the coming seven days. Reply plugs and inside-the-newsletter plugs are never scheduled; they live under their own posts and inside their newsletter. Never set a publish time. Never call `eden_publish_post_now`. Never schedule a platform `eden_list_schedules` did not list as connected. Read-only token: hand them the copy and point at the fix in `connect-eden.md`. Record in the log which promos were saved as drafts.
5. After the FIRST kit only, the routine line from the skill: once, one line, then only act when they name a time.

## Step 6: the weekly run

Trigger: "Write this week's promotions." Read the kit note and the settings note first.

1. Read the log. For each row of the past week: response filled in or blank. Ask, in one message, for the responses on rows still blank if the user has them; if they do not, treat blank as unknown, not as zero.
2. Drop angles with no response two weeks running. Double the angle that drew the most (two slots that week instead of one). Keep the five-angle floor; if dropping an angle breaks it, swap in the untested one instead.
3. Pick up the format rotation where the last written day left off. Write the next seven, numbered on from the last number in the kit. Same voice, same congruence line.
4. A new launch resets: rotation starts from the open, and the email section gets a fresh launch sequence beneath the old one, dated.
5. Replace the Social promotions block's coming week and append seven rows to the log. `eden_update_note` with `baseContentHash`; on `LINEAR_NOTE_CONFLICT`, re-read, merge by hand, never overwrite.
6. Same close as step 5, minus the routine line.

## Out of credits and other failures

`status: "out_of_credits"` mid-diagnosis: stop research calls, finish the diagnosis from the inputs and say it is inferred, write the kit, label it partial in one line at the top, and give the `upgradeUrl` once. Any other failed call: one line under the diagnosis ("couldn't check ads in this category this run"), keep going. One broken call never cancels the run. Details in `connect-eden.md`.
