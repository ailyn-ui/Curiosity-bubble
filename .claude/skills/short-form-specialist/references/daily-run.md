# The daily run

How one day's posts get made: exact tools, budgets, and the gates. The skill summary is not enough; this is the method. Read `craft-reference.md` before the angle and draft steps.

## Budgets

- **Daily run: at most 10 Eden calls, including the saves.** Reserve first, spend second: one `eden_schedule_post` per post (posts per day from the Voice and pillars note, default 2) plus one `eden_append_to_note` for the Post log. Memory takes 3. Whatever is left goes to material (up to 2) and research (at most 3, and at least 1 whenever the reserve allows). With 2 posts a day that is 3 memory, 3 reserved, 4 for material and research.
- **First-run setup: up to 8 more calls** on top of the first day's run.
- **Other jobs** (one piece into ten posts, adapt, fix, plug, explain): at most 6 calls, no saves unless asked.
- Retry a failed call once. After a second failure, record what's missing and draft from verified material.
- Spend calls on different questions, never on rewording the same query. If your environment can run subagents or parallel tool calls, run the research lanes at once; otherwise run them one at a time inside the same budget.

## Step 0, memory (3 calls)

1. `eden_search_workspace_items` for **"Short-Form Specialist"**. The board and its two notes come back together. If more than one workspace, `eden_list_workspaces` once and remember the pick in the Voice and pillars note.
2. `eden_get_note_markdown` on **"Voice and pillars"**. Keep the `contentHash` in case you edit it later.
3. `eden_get_note_markdown` on **"Post log"**. Read the last seven days: the angle families, opening families, and shapes already used, and which Weekly ideas rows were already turned into posts.

No board means first run: go to Setup, then come back and do today's posts in the same chat.

## Setup, first run only (up to 8 calls, one or two messages)

1. **Find the brand before asking.** `eden_search_workspace_items` for a **"Brand throughline"** note (the Weekly Content Strategist workflow keeps one on its "Content Strategist" board) or brand strategy material (the Personal Brand Strategist workflow saves a "Brand strategy" note). Read the best hit with `eden_get_note_markdown`. Found: say so and ask whether to use it. Nothing: ask exactly four questions in one message: what they write about (two to five topics), who it is for and what they are against, which platform and handle they post short-form to, what they sell or want to sell. Offer once that the Personal Brand Strategist workflow can build a full strategy.
2. **Look at the handoff.** `eden_list_schedules`: connected platforms, handles, timezone, and the `scheduleId`. Write these into the note so the daily run never spends a call on them.
3. **Learn their own content.** If their account is connected in Eden, `eden_get_analytics` for the digest, then `eden_list_analytics_posts` sorted by `outlierScore` for the winners. If nothing is connected, `eden_resolve_creator` on the handle they gave (confirm it back to them; never guess), then `eden_analyze_creator` with `since: "all"` and again with `since: "month"` if budget allows. Neither works: ask them to paste five to ten posts they are proud of. Read the top posts in full and note hook shape, shape, pillar, and the multiple against baseline. Keep their actual wording patterns.
4. **Confirm the standing instruction.** If a schedule matches their platform, ask once: "After each session, should I save the approved posts to your Scheduler as drafts on [account], so you can edit and pick the time there?" Record the answer in the note. No connected account: say they can connect it in Eden's Scheduler (Settings, then Social accounts); until then, posts stay in chat and in a note. Ask posts per day (one to three; suggest two).
5. **Distill, do not dump.** `eden_create_board` "Short-Form Specialist". `eden_create_note` on it titled **"Voice and pillars"** (structure in `post-format.md`, under 600 words, first Change log line `YYYY-MM-DD: created from <source names>`). `eden_create_note` titled **"Post log"** with a one-line header.
6. Say in two lines what you stored and where. Move straight into today's posts.

## Step 1, today's material (up to 2 calls)

In order. Stop at the first that gives something real, and say in one line where today's material came from.

1. **The Weekly ideas memo.** `eden_search_workspace_items` for **"Weekly ideas"** (the Weekly Content Strategist workflow keeps it on the "Content Strategist" board), read the newest with `eden_get_note_markdown`. Take the highest-ranked short-form rows not already in the Post log. Use the row's claim, pillar, and openers as the seed.
2. **What the creator brought.** A link, a saved item, a note, a topic. Read any item in full (`eden_read_card` or `eden_get_note_markdown`). A pasted draft skips straight to Step 4 as a fix job.
3. **Their own workspace.** `eden_search_captures`, `eden_search_highlights`, or `eden_find_workspace_items` on one pillar from the last fourteen days. One call, one pillar.
4. **A live market sweep** when nothing else exists: the market lane below becomes the material too.

## Step 2, research (what remains, at most 3 calls)

Three lanes. Run them in parallel when you can. Each lane returns bullets, never prose, and receipts only for posts actually retrieved.

- **Market** (1 to 2 calls): `eden_search_social_content`, `scope: {kind: "global"}`, `orderBy: "outlier"`, `since: "week"` (or `"month"` when the week is thin), `minOutlierScore: 3`, one query from today's pillar and topic, their platform. Read the most pivotal post in full with `eden_read_social_post` only when the search summary can't show why it worked. Return at most five bullets: hook shapes working as skeletons, the counter-signal, the open lane, receipts. One-off news, drama, and politics spikes are noise.
- **Own winners** (0 to 1 call): the Voice and pillars note already carries their proven shapes with multiples from setup. Refresh it once a week (when the Change log's last refresh is 7 or more days old) with `eden_get_analytics` or `eden_analyze_creator` `since: "month"`: top five posts on today's pillar with hook verbatim, shape, multiple, and the top reply or question. Their own posts are never market evidence.
- **Library** (0 to 1 call): only when there is no memo and no brought material, and Step 1 left budget: one more `eden_search_highlights` or `eden_search_captures`, up to five seeds with a verbatim excerpt and the claim each could become.

Research is done when more of it would not change the claim, platform, or draft. Then write.

## Step 3, five angles (the gate)

Write five angles that differ in claim, tension, proof, or payoff, each from a different generative move (hidden mechanism, useful distinction, counterexample, personal observation, practical sequence, tradeoff, second-order effect, identity shift). Run the independence test from `craft-reference.md`: same payoff means replace one. Skip any angle family or opening family used in the last seven days of the Post log.

Each angle is two lines: the claim in plain words, and the proof or moment it needs. Mark the recommended one.

- **Live chat**: show the five and wait for the pick. They can pick several.
- **Routine run, or "you choose"**: take the top angles yourself, as many as posts per day, and say which you took.

## Step 4, draft

One post per chosen angle, native to the platform, using the shapes and platform rules in `craft-reference.md`. Rules that never bend:

- One central idea per post. Every post stands alone.
- A different shape and a different opening family for every post in the same day.
- The creator's vocabulary and rhythm from the Voice and pillars note; concrete nouns, numbers, and moments from their material, never invented.
- No hashtags unless they use them. No engagement bait.
- Never eight or more words in a row from any source. Borrow a hook's shape, never its substance.
- An X thread only when an angle needs several independent steps: first post a complete promise, every segment one job, segments saved in order.
- Run the nine-point rubric silently. Fix premise and proof before style.

## Step 5, deliver and sharpen

Each post on its own so any one can be saved or edited. Under each, at most three lines: which angle it rides, the one receipt that shaped it, anything unverified. Format in `post-format.md`. When they ask for changes, revise the same post rather than making a second version.

## Step 6, the handoff (one call per post)

- Standing instruction says yes: `eden_schedule_post` with `draft: true`, the remembered `scheduleId`, `platforms` set explicitly to their platform, `text` (or `segments` in order for a thread), and an `idempotencyKey` so a retry can't double-save. One line per post: saved, or not.
- No standing answer yet: ask once, then record the answer in the Voice and pillars note.
- Never set `scheduledFor` or `scheduledAtIso`, and never call `eden_publish_post_now`, unless the creator explicitly asks in this conversation. "Add it to my scheduler" is not permission to schedule.
- A video script has no media: save it with `eden_create_note` on the board instead.
- Never claim a save succeeded unless the tool said so. On failure keep the copy in chat, explain plainly, offer to retry with the same idempotency key. If the schedule is missing or changed, spend one `eden_list_schedules` to re-find it and update the note.

## Step 7, log and remember (1 call)

`eden_append_to_note` on the Post log: one line per post (format in `post-format.md`), plus the memo rows consumed. When a pillar keeps winning, a hook shape has died, or the creator changed direction, propose the exact Voice and pillars edit and apply it with `eden_update_note` (pass the `baseContentHash` you read) only after a yes. Unattended runs apply only a proven-shapes line or a vocabulary term, and log it in the Change log.

## Other jobs

- **One piece into ten posts**: read it in full (1 to 2 calls), build a source map, write six to ten independent angles, then ten posts in a mixed batch (about four concise, three multi-line, three structured), checked as a set for variety. Save to the scheduler only when asked.
- **Adapt a post between platforms**: keep the claim, rebuild the shape for the destination's rules.
- **Fix a pasted draft**: the two or three changes that matter most, keep their premise, one revised post.
- **The daily plug**: the one-line reply linking today's long-form piece or offer under their best post of the day. The Marketing Strategist owns the full promotion plan.
- **Explain a winner**: five lines on why one of their posts beat baseline.
