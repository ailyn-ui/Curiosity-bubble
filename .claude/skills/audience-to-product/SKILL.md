---
name: audience-to-product
description: >-
  Start from an audience, not from the founder's skills: research what digital
  products that audience is already searching for, complaining about and paying
  for, turn the evidence into scored product ideas, then build the chosen one
  end to end (the product itself, the sales page and the launch plan) under a
  brand-new, separate brand with its own name, positioning and voice. Use
  whenever the user names a group of people and wants to know what to sell
  them: "what digital product could I make for X", "product ideas for
  [audience]", "what are [audience] looking for", "find me a product to sell
  to...", "I want a side brand/side income selling to...", "research this
  audience", "validate a digital product idea", or wants a template, guide,
  course, toolkit, planner or printable for a specific audience and doesn't
  know which one yet. Also use when they've picked an idea from an earlier run
  and want to keep building it.
---

# audience-to-product

The audience is the input. Demand is the filter. The founder's skills are
**not** a criterion: if the evidence says the audience wants something, it
goes on the list, and you work out how to build it (research, AI, templates,
contractors) afterwards. Don't ask the user what they're good at, and don't
quietly drop ideas because they're outside the user's expertise.

The product ships under a **new, separate brand**. That isn't a branding
exercise for its own sake: a separate brand keeps the user's consultancy
positioning clean, and lets the new product be judged on its own.

## The four phases

Run them in order and stop at each checkpoint for the user's decision. Each
phase writes a file to `ventures/<slug>/` at the repo root. Make the slug from
the audience at first, then rename the folder once the brand has a name. These
files are how a later session picks the work back up: if
`ventures/*/` already holds a project for this audience, read it and continue
from the last finished phase instead of starting over.

```
ventures/<slug>/
├── 01-research.md     # evidence log
├── 02-ideas.md        # scored ideas + recommendation
├── 03-brand.md        # the new brand
├── 04-product/        # the product itself (files the buyer gets)
├── 05-sales-page.md
└── 06-launch.md
```

### Phase 0: Intake (one short message)

You need: **who** the audience is, as specific as the user can make it (for
example "first-time foster parents in the UK", not "parents"). Optional extras:
the market or language, a price range, formats to avoid, and how soon they
want to launch. If the audience is vague, offer two or three sharper
sub-segments and let them pick, because a vague audience produces vague
evidence. Don't ask about the user's skills, experience or existing brand.
If the user gave no market, don't stop to ask. Default to the market with the
most online evidence (usually English-speaking), say so, and add a short note
on the user's home market at the end of the research.

If the user names Sarah or Esti, you may read their persona files
(`.claude/skills/talk-to-avatar/avatar.md`, `.claude/skills/talk-to-esti/esti.md`)
**as audience insight only**. Persona files are a starting hypothesis, not
demand evidence. Still do the outside research.

### Phase 1: Demand research → `01-research.md`

Read `references/research.md` for the sources and search patterns. The goal
is **evidence that people want, and pay for, solutions**, not opinions about
what they might like. Gather it with WebSearch and WebFetch. Run several
searches per turn. If subagents are available and the user wants depth, split
the work by source type (communities, marketplaces, search demand).

What to collect:

- **Pains in their own words**: verbatim quotes, each with its link. Note how
  often a pain repeats across different places.
- **What they already buy**: marketplace bestsellers (Etsy, Gumroad, Amazon
  KDP, Udemy, Teachers Pay Teachers, Creative Market and similar), with
  prices, review counts and formats.
- **Gaps**: 1 to 3 star reviews, "I wish this had...", "does anyone know a
  [thing] for...", requests that get no good answer.
- **Where they gather**: subreddits, Facebook groups, forums, hashtags,
  newsletters and podcasts. This decides distribution later.
- **Who pays**: the person with the problem isn't always the buyer (parents
  pay for teens, managers for teams). Name both, because it changes the price
  and the sales page.
- **The price ladder**: list what exists at each price, from free to DIY,
  done-with-you and done-for-you. Empty bands are where opportunities sit.

If WebFetch can't reach pages (a blocked network or a host that doesn't
resolve), keep going with search-result excerpts, but label every quote
taken that way as a *search excerpt* that hasn't been checked against the
original. List the blocked domains so the user can allow them in the
session's network settings and rerun.

If the audience is young or vulnerable, or mental-health or financial
distress shows up in the research, note it. Every product for that audience
then carries a short pointer to professional support.

Write the log with a source link next to every claim. Label anything you
couldn't verify as *unverified*. Never invent quotes, numbers or review
counts. If a source can't be reached, say so and move on. Close with the top
pains, ranked by how often they appeared and how intense they were.

### Phase 2: Ideas and scoring → `02-ideas.md`

Generate 8 to 12 ideas. Each one must point back to specific evidence lines
in the research log: an idea with no evidence behind it doesn't go on the
list. Vary the format (template, toolkit, mini-course, printable, Notion
system, swipe file, calculator, AI prompt pack, workshop, membership).

Score every idea with the rubric in `references/scoring.md`. Then:

- show a ranked table,
- write up the top three: the buyer, the promise, the format, the price, the
  evidence behind it, and what would kill it,
- recommend one, and give a **cheap validation test** to run before building
  it in full (a pre-sale, a waitlist page, a paid pilot, or a post in a
  community where that's allowed).

**Checkpoint:** the user picks an idea, or asks for more research.

### Phase 3: The separate brand → `03-brand.md`

Build a brand that stands alone:

- **Name**: 6 to 10 options in different styles (descriptive, evocative,
  invented). Check the top picks with WebSearch for clashes with existing
  products in the same space and for obvious domain or handle conflicts.
  Report what you found and what you couldn't check. Recommend a proper
  trademark search before the user spends money; you can't do one yourself.
- **Positioning**: who it's for, the problem, the alternative they use today,
  why this is different. One sentence plus a short paragraph.
- **Voice**: 3 to 4 traits, each with a "sounds like / doesn't sound like"
  pair, plus words to use and words to avoid. Take these from how the
  audience actually talks in the research log.
- **Look**: a direction, a palette with hex codes, a font pairing and a
  mood. Enough for the user or a designer to work from.

How the brand stays separate. Keep to all of these, because the whole point
is that nobody connects the two:

- Don't use the user's name, the consultancy's name, or its taglines, offers,
  palette or signature phrases. Don't read `instagram/voice.md`,
  `website/` or the consultancy brand files for style.
- Don't mention the consultancy or link to it in any product, page or launch
  copy, unless the user explicitly decides to.
- If an idea of yours sounds like the consultancy's voice, rewrite it.

**Checkpoint:** the user picks a name and approves the brand.

### Phase 4: Build → `04-product/`, `05-sales-page.md`, `06-launch.md`

1. **Outline first.** Show the structure of the product: sections, pages,
   modules or template parts, each mapped to the pain it solves. Get a quick
   yes before writing it out.
2. **Write the real product.** The actual contents the buyer receives, not a
   description of them: the guide text, the worksheets, the template
   structure with example entries, the prompts, the scripts. Write it in the
   new brand's voice. For the final file format, use the skill that fits:
   `anthropic-skills:pdf`, `anthropic-skills:docx`, `anthropic-skills:xlsx`,
   `anthropic-skills:pptx`, or an Artifact for an interactive tool. Keep the
   editable Markdown source in `04-product/` either way.
3. **Sales page** (`05-sales-page.md`): headline, the problem in the
   audience's words (taken from the research quotes), what's inside, who it's
   for and who it's not for, price, FAQ answering the objections found in the
   research, guarantee, call to action. Where a claim needs proof the user
   doesn't have yet (testimonials, results), leave a marked placeholder
   instead of inventing it.
4. **Launch plan** (`06-launch.md`): the validation test, then the first 30
   days. Name the specific places from the research where this audience
   gathers, how to show up there without breaking their rules, a sales
   platform (Gumroad, Lemon Squeezy, Etsy, Payhip or Stan, picked for the
   format and audience), and the numbers to watch.

Before showing any customer-facing copy, run it through `ig-human` if it's
available, so it doesn't read as AI-written.

## How to talk to the user

Plain language, short updates between phases ("research done: 41 sources,
top pain is X. Ideas next."). Put findings in the files and keep the chat to
the decision the user needs to make. Be honest about weak evidence: "only
three people mentioned this" is useful information, not something to hide.
If the research shows the audience doesn't spend money on digital products,
say so and suggest a better-paying adjacent segment rather than forcing an
idea.
