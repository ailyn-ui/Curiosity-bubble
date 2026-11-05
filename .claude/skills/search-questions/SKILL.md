---
name: search-questions
description: >-
  Find the real questions people type into Google and YouTube about a topic,
  the way AnswerThePublic does: collects search suggestions by question word
  (how, why, what, can I...), preposition (for, with, without, vs...) and
  letter, groups them into themes, picks the ones Ailyn's clients would ask,
  and turns the best into hooks, post topics, reel ideas and FAQ answers.
  Fetches live from Google and YouTube suggestions when the network allows,
  or works from an AnswerThePublic CSV, Google "People also ask" questions or
  YouTube suggestions the user pastes. Use when the user says "what are people
  searching", "search questions", "answer the public", "what do people ask
  about...", "leading questions", "keyword ideas", "YouTube search ideas",
  "what should my post answer", or wants topics grounded in real searches.
---

# search-questions

Real questions, in the searcher's own words, so posts and pages answer what
people already ask. Search data shows **what** people ask and roughly how they
phrase it. It doesn't show who asked, how many, or why: treat it as a list of
leads, never as proof.

Read before the first answer:

1. `positioning.md` (who Ailyn serves, the problem she solves).
2. `.claude/skills/talk-to-avatar/avatar.md` (Sarah) and
   `.claude/skills/talk-to-esti/esti.md` (Esti), for who's reading.
3. `instagram/voice.md` if it exists, for how Ailyn sounds.

## 1. Seeds

Ask once, in one short message, unless the user already said:

- **Topics** (2–5 short seed phrases), e.g. "brand strategy", "brand for small
  business", "AI for my brand", "ADHD founder", "personal brand". Suggest seeds
  from `positioning.md` if she has none.
- **Where:** Google, YouTube, or both (default both).
- **Language and country:** default English, Switzerland (`--lang en --country ch`).
  Offer US or UK too: more searches, broader phrasing. German if she wants Swiss clients who search in German.

## 2. Collect

**Live (preferred).** Run the collector, one call per seed:

```
python3 -I .claude/skills/search-questions/collect.py "brand strategy" --source both --lang en --country ch --out research/search-questions/<date>-<slug>.json
```

It asks Google's and YouTube's suggestion service for the seed combined with
question words, prepositions, comparisons and a–z, pausing between requests,
and saves every suggestion with what produced it. 54 requests per seed and
source, under a minute each.

If it prints `BLOCKED`, the session's network doesn't allow
`suggestqueries.google.com`. Tell the user in one line: add that domain under
Network access → Allowed domains (environment menu in the title bar → Edit),
and that it may only apply to a new session. Then switch to **from exports**.
Never fill the gap with invented questions.

**From exports.** Any of these, pasted or uploaded:

- an AnswerThePublic CSV (a few free searches a day on their site)
- the "People also ask" questions from a Google search (expand a few; more appear)
- YouTube's suggestions as she types the seed into the search box
- Google's "Related searches" at the bottom of the results page

Save what she gives in `research/search-questions/<date>-<slug>-export.md`
(or the CSV as is), then continue.

## 3. Sort

From everything collected:

1. **Clean:** drop duplicates, brand names that aren't hers, jobs and salary
   searches ("brand strategist salary"), students ("brand strategy course
   assignment"), and anything off-topic.
2. **Group** into 5–8 themes in plain words, e.g. "Is a brand just a logo?",
   "Doing it myself with AI", "Too scattered to start", "Cost and is it worth it".
3. **Mark each question** for who would ask it:
   - **Sarah** (early, overwhelmed, DIY), **Esti** (established, team,
     bottleneck), **not ours** (designers, students, big companies).
   - Its stage: **unaware** (doesn't know the problem is the brand), **aware**
     (knows, looking for how), **choosing** (comparing ways or people).
4. **Pick the 10–15 best:** clearly a client's question, phrased the way a person
   talks, and something Ailyn can answer better than a generic article.

## 4. Turn into content

For the top picks, give:

| Question (their words) | Theme | Who · stage | Use it as | Hook or first line |
|---|---|---|---|---|

"Use it as" is one of: post or carousel, reel, FAQ on the offer page, email,
story poll, a question for client interviews. Write hooks in Ailyn's voice:
sentence case, plain, warm, no hype. Keep the searcher's own words in the hook
where they're strong.

Then, in a few lines:

- **Patterns:** what the questions say about how people think about brands now
  (e.g. "brand" = logo, AI can do it for free).
- **Gaps:** questions nobody answers well that fit Ailyn exactly.
- **Next:** hand the best hooks to `/socmed-hook-engine` or `/ig-reel`, the FAQ
  lines to `/copy-team`, and check the picks with `/talk-to-avatar` or
  `/talk-to-esti` before building a series on them.

## Saving

Save the summary as `research/search-questions/<date>-<slug>.md` (date, seeds,
source, language and country, top picks, themes, patterns). Keep the raw JSON
or export beside it. Commit only when the user asks.

## Never

- Never invent search questions, volumes or trends. No numbers unless a tool
  the user gave actually shows them (AnswerThePublic's CSV may; suggestions
  don't).
- Never present suggestions as market research or as what clients said.
  Real client words live in `real-voices.md` and outrank search data.
- Never get around a block (other sites, spoofed headers, scraping result
  pages). Blocked means ask for the domain or an export.
