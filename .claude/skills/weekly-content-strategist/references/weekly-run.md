# The weekly run

How the research happens: exact tools, budgets, and the rules that keep the memo honest. The skill summary is not enough; this is the method. The market lane borrows the Weekly Strategist's sweep method (PROOF, EARLY, PROVEN), sized down because the deliverable here is the ideas list, not the market read.

## Budgets

- **Whole run: target 14 to 20 Eden calls including lookup and delivery. Hard ceiling 24.** Stop researching when you reach 24 no matter what is still open and write from verified evidence.
- **Never more than four calls in one batch.**
- Retry a failed call once. After a second failure, record the missing coverage in the memo and move on.
- Spend calls on different questions, never on rewording one query. Every search result is the complete ranked set for that query; a similar query returns the same posts.
- If your environment can run subagents or parallel tool calls, run the three lanes at once as self-contained briefs that return evidence only, each holding its own lane budget below. Otherwise run them one at a time in this order: scoreboard, market, library.

Typical spend on a weekly run:

| Lane                                   | Calls  |
| -------------------------------------- | ------ |
| Lookup (settings, throughline, memo)   | 3      |
| Scoreboard                             | 1 to 3 |
| Market (creators, searches, reads)     | 5 to 7 |
| Library (searches, reads)              | 3 to 5 |
| Delivery (memo, throughline, settings) | 3      |

First run: setup adds the brand strategy search (1 to 3), handle resolution (1 to 3), the idea bank lookup (1), and three creates. To stay under the ceiling, the first run uses the lifetime scoreboard instead of the monthly one, two market searches instead of four, and three library searches. Say in the memo that the first week ran light.

## Lookup (every run)

`eden_search_workspace_items` for the board "Content Strategist" and the note "Strategist settings". Then `eden_get_note_markdown` on the settings note, the "Brand throughline" note, and the newest "Weekly ideas" note (sort by title; the date is in it). From those three you carry: accounts, topics, radar, where ideas live, the used-library-items list, the Topic ledger, last week's picks, and each open finding's first-seen date. Read one older memo only when a longer comparison needs it.

## Setup (first run only)

Run this once, when the lookup finds no "Strategist settings" note. Then continue straight into the weekly run in the same chat.

1. **Find the brand strategy before asking for it.** `eden_find_workspace_items` and `eden_search_workspace_items` for brand strategy material: "brand strategy", "throughline", "worldview", "pillars", and a board named "Personal brand strategy" (the Personal Brand Strategist workflow saves there, note titled "Personal Brand Strategy: ..."). Found: tell the user in one line each and ask whether to use them. Nothing solid: ask them to paste their brand strategy. None exists: ask exactly three questions in one message (what they make content about, 2 to 5 topics; who it is for and what they are against; which accounts are theirs, platform and handle). Offer once that the Personal Brand Strategist workflow can build a full strategy.
2. **Confirm accounts and radar.** `eden_get_analytics` shows connected accounts. Resolve every handle with `eden_resolve_creator`; never guess. Ask for up to 8 radar creators only if none are obvious from the strategy. Optional.
3. **Find where their ideas live.** `eden_search_workspace_items` and `eden_list_tags` for a board or tag named like "Ideas", "Idea Bank", "Content ideas", "Swipe file". Nothing: ask once. "No" is fine; then the whole library is the idea bank.
4. **Distill, do not dump.** `eden_create_board` "Content Strategist", then `eden_create_note` "Brand throughline" on it in the section structure from `ideas-memo-format.md`. Under 800 words. Quote the creator's own vocabulary. Seed the Topic ledger from the lifetime winners the first scoreboard returns (write the note after the scoreboard lane if you run lanes in sequence). First Change log line: "YYYY-MM-DD: created from <source names>".
5. `eden_create_note` "Strategist settings" per `ideas-memo-format.md`. Say in two lines what you stored and where, then move on.

## Lane 1: Scoreboard (their own posts)

| Job                            | Tool                                              | How                                                                    |
| ------------------------------ | ------------------------------------------------- | ---------------------------------------------------------------------- |
| Recent performance vs baseline | `eden_analyze_creator`                            | each own account, `since: "month"`; keep the top 5 per account         |
| Lifetime winners               | `eden_analyze_creator`                            | `since: "all"`; first run and about once a month after                 |
| Read the top posts in full     | `eden_read_social_post`                           | first run only, top 3 lifetime winners, for hook and audience response |
| Private numbers when connected | `eden_get_analytics`, `eden_list_analytics_posts` | optional, one call; never present syncing metrics as zeros             |

What you want per winner: the hook verbatim, multiple against baseline, reach, format, which pillar it rides, and the top audience question or pushback in the replies. Judge by typical multiple, never one hit: 2x solid, 3x and up a real breakout. Own posts are never market evidence, never finding receipts, never watchlist entries.

No connected accounts: say so once and run the same reads on their public handles. Analytics that returns `activating: true` or `not-available` is not a dead end; `eden_analyze_creator` covers the public numbers.

## Lane 2: Market findings

Budget inside this lane: 1 creator search, 2 to 4 content searches, 2 to 3 full reads.

1. **Creators.** `eden_search_creators` by the main topic once. Add one similarity round seeded by the radar creators only when the topic search is thin. Deduplicate, drop the user's own accounts, and pick three to five strategically distinct creators across sizes. Discovery produces leads, not findings.
2. **Searches.** `eden_search_social_content` with `scope: {kind: "global"}`, `orderBy: "outlier"`, queries written from the pillars in the throughline, across three lanes:
   - **PROOF**: `since: "month"`, `creatorTier: "mid"` or `"macro"`, `minOutlierScore: 3`. Real reach.
   - **EARLY**: `since: "week"`, no tier filter, `minOutlierScore: 5`. Small accounts breaking out first.
   - **PROVEN**: `since: "year"`, `minOutlierScore: 3`. Supporting receipts for why a mechanism works, never the claim that something moves now.
3. **Reads.** `eden_read_social_post` on the two to three pivotal posts. Ask WHY each popped: the hook, the format, the topic, the timing. Transferable mechanisms make findings; "this topic is hot" does not.

A **finding** is a market move that repeats across at least 2 different creators, with 2 to 4 receipts (handle, platform, multiple, reach, hook verbatim, one line on why it popped). Seen once is an **early signal**, labeled as such. At least one receipt per finding comes from outside the configured radar. One-off news, drama, and politics spikes are noise. `outlierScore` is the number that matters: how many times the post beat that creator's own baseline.

Return at most three findings plus a watchlist of 2 to 4 leads (creators, patterns, or topics worth watching next week; never the user's own accounts or their radar). Compare against last week's memo: each carried finding is now **building**, **saturating**, or gone; new ones are **new**; every finding keeps its first-seen date.

## Lane 3: Their library

Budget inside this lane: 3 to 5 searches, 1 to 2 full reads.

| Job                              | Tool                                               | How                                                                 |
| -------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------- |
| Saved posts, links, and captures | `eden_search_captures`                             | one query per pillar, in the creator's own words and plain synonyms |
| Quotes and clipped passages      | `eden_search_highlights`                           | pillar keywords; highlights are pre-distilled substance             |
| Notes and documents, by meaning  | `eden_find_workspace_items`                        | the fuzzy "what do they have on X" pass                             |
| The idea bank                    | `eden_read_board` or `eden_search_workspace_items` | the board or tag from the settings note, newest first               |
| Read what matters                | `eden_read_card`, `eden_get_note_markdown`         | the one or two items a row will lean on                             |

Search angles, in priority order: each pillar in its own words, the empty rungs in the Topic ledger, the audience questions from this week's scoreboard. Prefer the last 60 days. Skip anything already in the settings note's used list.

Return up to ten seeds, then keep three to six: what it is, title and source, a short verbatim excerpt, the pillar, any other item that agrees or clashes, and the one-line claim it could become. Rank by pillar fit, specificity, and connection to a winner or finding. A seed that agrees with a winner becomes a sequel. A seed that clashes becomes a contrarian post. Saved but never published is the freshest. Library seeds never count toward a finding.

When the library is empty (new Eden user), say so in the memo, lean on the scoreboard and the market, and tell them once that saving things to Eden makes next week's list better.

## Grade last week

From the newest memo's short-form and long-form tables, take the picks you recommended (the rows you called out in the close plus any the user said they took). Match each against this week's scoreboard. One line per pick: what they posted, the result against baseline, the grade. "You did not post it" is a grade. Never soften a miss. First run: "First run, nothing to grade yet."

## Update the throughline

Earned edits only: a new proven format, a pillar the numbers say is dead, a piece of vocabulary the audience adopted, a Do-not-do learned the hard way. Propose the exact line edits in chat and apply with `eden_update_note` after a yes. The Topic ledger always updates: add this week's recommended angles as "recommended YYYY-MM-DD" and mark last week's posted picks as published with their rung. Cap the ledger at 30 topics; retire the weakest. Every change gets a dated one-line Change log entry. A scheduled run with nobody in the chat applies only edits the scoreboard proves and logs them.

## Build the ideas

Read `references/craft-reference.md` now. The short version: rows 1 to 3 of the short-form table evolve their own winners by one of the eleven rules; at least two rows come from library seeds when seeds exist; every finding feeds at least one row through its structure, never its topic; reruns are capped at two and labeled; hook shapes and pillars vary across the table. Long-form: at least one direct sequel to their biggest long-form winner one rung down the ladder, and at least one from the library.

Before writing, run every row through three checks: does it pass the throughline's lens (would this creator say it), does it trace to a finding, the scoreboard, or a named library item, and has it already been published or ledgered as done. Kill anything that fails.

## Deliver

Write the memo per `references/ideas-memo-format.md`. Save it with `eden_create_note` on the "Content Strategist" board, titled `Weekly ideas — YYYY-MM-DD`. Update the settings note with `eden_update_note`: last run date, and the library items used this week appended to the used list (keep the newest 40, drop the oldest). Then the styled delivery from the template, and the three-line close.
