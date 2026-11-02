# The consultation method

How the consultation runs: what to find in Eden first, how the two interview phases work, exactly which tools to spend the research budget on, and how to construct the offer before writing the blueprint. The skill summary is not enough; this is the method.

## Ground rules for the whole run

- **One question per message.** Every question builds on the last answer. Never send a numbered list of questions to fill in.
- **Facts over opinions.** "What did the last person who paid you actually get?" beats "what results do you deliver?"
- **Push once for a number.** If the second answer has no number, write it down as a proof gap and move on.
- **Build early.** As soon as the components are supported, or when the user says they are ready, build. A blueprint with three labeled suggestions ships and gets corrected. An interview run to completeness dies in chat.
- **You own the offer.** Never write the sales page, the posts, or the ads. Those belong to the Marketing Strategist.

## Budgets

- **Research calls: at most 6 per consultation.** Own-account pulls, social searches, and ads searches all count. Workspace reads (the brand strategy note, an existing blueprint, the interview note) and note writes are outside this number.
- Retry a failed call once. After a second failure, record what is missing and proceed from the interview.
- If your environment can run parallel tool calls, run the research lanes together. Otherwise run them one at a time inside the same budget.
- If research is unavailable (tools erroring, `status: "unavailable"`, or out of credits), say so in one line and build from the interview. The offer never waits on research.

## Step 0: what already exists in Eden

Resolve the workspace first (`eden_list_workspaces` if there is more than one). Then look, in this order:

1. **The home board.** `eden_search_workspace_items` for a board named **"Offers"**. On it, look for notes titled `Offer Blueprint: ...` and `Offer interview: ...`. An existing blueprint means this is a revision: read it with `eden_get_note_markdown`, keep the `contentHash`, and ask one question: "what's changed, or which component do you want to rework?"
2. **The brand strategy.** `eden_search_workspace_items` for a board named **"Personal brand strategy"** or a note whose title starts with **"Personal Brand Strategy:"**. Both the Personal Brand Strategist workflow and the Personal Brand Strategist Custom AI write one. If found, read it and lift: the audience, the worldview, the content pillars, and any monetization ideas. Confirm in one line ("I read your brand strategy: you're speaking to X about Y. Still right?") instead of re-asking.
3. **Their best posts.** If `eden_list_schedules` shows connected accounts, `eden_get_analytics` gives the digest and `eden_analyze_creator` (their own handle, `since: "all"` or `"month"`) shows which posts beat their baseline. If they give a handle instead, resolve it with `eden_resolve_creator` first; never guess a handle. The topics people already save, reply to, and share are the strongest signal for what to sell first and for what to name the mechanism after. These pulls count against the research budget (at most 2).

Then send the opening message: one compact paragraph that says what you found (or that you found nothing, which is fine), asks whether they have anything else worth pasting (a customer avatar, an existing product or sales page), and makes clear you can start from nothing. End it with the first real question.

**First run with no board:** create it before saving anything (`eden_create_board` "Offers"). Do this when you first have something to save, not before the interview starts.

## Phase one: what to sell (skip when they already have a product)

Interview, one question at a time, until you have facts for each of these:

1. What they know how to do that other people struggle with.
2. What people already ask them for help with, in the asker's words.
3. The result they have produced for themselves or others, with numbers.
4. How they want to spend their week: talking to people, making things, building software, writing.
5. How much of their time they are willing to sell.
6. Who their audience is and roughly what those people can pay.
7. What they would enjoy delivering for a year.

Answers already in the brand strategy or visible in their best posts get confirmed, never re-asked.

Then walk the four options honestly (the reference: `craft-reference.md`, "Choosing a first product"). Present a compact comparison in chat, one row per option:

| Option | Fit with your skill | Fit with what your audience can pay | Time to first sale | Main risk |

Recommend one first product in two lines, using the decision rules: start where demand already showed up; the smallest thing that still delivers the whole outcome; sell time first when there is no audience proof yet; a tool when the outcome is a repeatable task, a course when the outcome is a skill. One first product. If they push back, hear the reason, adjust once, and record the rejected options with the reason each lost.

## Phase two: build the offer

Interview only for what is still missing, one question at a time:

1. Who exactly the buyer is and what they have tried already.
2. Where the buyer sits on the awareness ladder: unaware, problem-aware, solution-aware, product-aware, most-aware.
3. The delivery format, and their appetite to change it.
4. The problems the product solves best, in the customer's words.
5. Outcomes with a number and a timeframe: the best real result and the typical one.
6. The alternatives the prospect weighs, including doing nothing.
7. The current guarantee, if any, and how much refund risk they can tolerate.

Push once for the number. Otherwise record a proof gap and keep going. When the components are supported, or the user says "build it", stop asking and build.

## Research: positioning (inside the 6-call budget)

Research sharpens positioning so the mechanism is different on purpose. It never replaces the interview. Spend only what the offer needs:

| Lane             | Tool                                                                                                                                                                   | Budget  | What you want                                                                                                 |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------- |
| Their own posts  | `eden_get_analytics`, `eden_analyze_creator` (`eden_resolve_creator` first for a handle)                                                                               | up to 2 | Which topics already get saved, shared, replied to                                                            |
| Similar offers   | `eden_search_social_content`, `scope: {kind: "global"}`, `orderBy: "outlier"`, `since: "year"`, queries like "<outcome> program", "<niche> coaching", "<niche> course" | up to 3 | What similar offers promise, how they name their mechanism, what proof they lean on                           |
| Spend-proven ads | `eden_search_ads` with the category or the outcome as the query, sort `longest` or `top`, `minRunDays` 30                                                              | up to 2 | The angles brands keep paying to run in this category; ads that run for months are proof the promise converts |

Ceiling is 6 across all three lanes. Report only what came back: the handles, the promises, the run days. Their own posts are never market evidence; they are demand evidence for what to sell. If a lane comes up thin, say so and move on. Never fill a gap with what you assume the market looks like.

## Diagnose before you construct

Before writing a single blueprint section, state in two or three lines in chat:

- The awareness level of the buyer.
- The market judgment on the four traits: pain, purchasing power, ease of targeting, growth. Mark which of these are inferences from the interview and what would confirm them.
- If research ran: what similar offers promise, in one line, and therefore where this offer should stand apart.

Recommend a different segment or market only when pain or purchasing power is genuinely absent.

## Construct

Follow `craft-reference.md` for each move:

1. **Value equation.** Score the four levers for this product as it stands. Name which the offer pulls hardest and which stay weak. Rebuild the weakest lever first.
2. **The stack.** List every problem on the way to the outcome (before, during, after). Turn each into a solution. Pick a delivery vehicle for each, high value to the buyer and low cost to the seller. Trim everything that does not kill a named objection or shorten a lever.
3. **The mechanism.** Name it, and lay it out in three to six real phases of delivery. Use the user's own language from their posts and answers. Check it against what similar offers call theirs; different on purpose.
4. **The guarantee.** Design it against the buyer's actual feared risk and inside the seller's economics and stated refund tolerance. Pick the type (unconditional, conditional, outcome-based, anti-guarantee) and state the conditions plainly.
5. **The price.** Price on value delivered. Show the arithmetic: the quantified outcome, the fraction the price captures, and what the price says about the promise. Name any lead product in front of it. If the outcome number is a proof gap, the price is provisional and says so.
6. **Enhancers.** Only real scarcity, real urgency, and bonuses that each kill a named objection. Every enhancer must survive "is this literally true?"

Then write the blueprint per `blueprint-format.md` and deliver.

## After the blueprint

- Ask which components to refine. Corrections to audience, product facts, pricing, or substantiation rebuild the affected components, in the same note.
- Save the interview facts, proof gaps, and rejected directions to the note `Offer interview: [product]` on the "Offers" board (create with `eden_create_note` the first time, `eden_append_to_note` after). This is the memory that stops a later session from re-asking or re-pitching a rejected direction.
- Point to the next step once: the blueprint is the input for the landing page copy and the daily promotions. The Marketing Strategist reads the `Offer Blueprint:` note from the "Offers" board.
