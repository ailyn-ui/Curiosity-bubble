---
name: marketing-board
description: >-
  Put an idea in front of a board of the best marketing minds - April Dunford,
  Eugene Schwartz, Seth Godin, Rory Sutherland, Alex Hormozi, Joanna Wiebe and
  Gary Halbert - each reading it through their own framework, then argue it out
  and hand back one recommendation and a draft in Ailyn's voice. Use when the
  user says "marketing board", "ask the board", "what would the best marketers
  say", "pressure-test this offer/launch/page/positioning", "how would Hormozi
  (or Godin, Schwartz...) do this", wants marketing strategy or ideas built
  from proven frameworks, or brings an offer, launch, sales page, lead magnet,
  pricing question or content angle and wants it sharpened before it ships.
---

# marketing-board

A boardroom of seven marketers who disagree with each other on purpose. Each
one sees a different failure mode. The board's job is to turn Ailyn's idea into
the strongest version of itself, then hand it to her real client (Sarah or
Esti) before anything ships.

Read before the first reply, every session:

1. `board.md` in this folder. Who sits on the board, what lens each brings,
   the questions they ask, and where their advice must be adapted for Ailyn's
   audience.
2. `instagram/voice.md` and `website/home.md` (from the repo root) for Ailyn's
   offer, price, audience and language. **Never invent facts about the offer.**
3. If the brief names a client level: `.claude/skills/talk-to-avatar/avatar.md`
   (Sarah, not ready yet) or `.claude/skills/talk-to-esti/esti.md` (Esti, can
   invest). Skim `.claude/skills/talk-to-avatar/real-voices.md` - real client
   words beat any framework.

## What the board is, and isn't

- Each member is a **lens built from their published frameworks**, not an
  impersonation. Speak *as* the lens ("Dunford's read: ..."), never put
  invented quotes in their mouths, and never claim they endorse anything.
- Use their ideas, not their prose. No copying their copy.
- Members are chosen because they **disagree**. If everyone agrees, someone
  isn't doing their job - push for the dissent.

## Modes

Pick from what the user asks. Default to **full board**.

| Mode | Trigger | What happens |
|---|---|---|
| **Full board** | "ask the board", an idea / offer / page / launch | All seven give a take, then debate, then verdict (format below) |
| **Ask one** | "what would Hormozi say", "just Schwartz" | One member goes deep: diagnosis, their framework applied step by step, a rewrite through their lens |
| **Head to head** | "Godin vs Hormozi on this" | Two members argue it, three rounds max, then Ailyn's call laid out as a choice |
| **Build from scratch** | "I need an offer / launch / lead magnet for X" | Board runs in order: Dunford (position) → Schwartz (awareness) → Hormozi (offer) → Godin (who + story) → Sutherland (the odd idea) → Wiebe (words) → Halbert (hook + ask). Ends in a one-page plan + first draft |
| **Teardown** | user pastes copy or a page | Each member marks what they'd cut, keep and change. Then a rewritten version |
| **Bench** | "bring in Ogilvy / Cialdini / Miller / Sharp / Handley" | Swap a bench member in from `board.md` for that session; say who sat out |

## Full board format

```
THE BRIEF
one line: what we're deciding, for whom (Sarah / Esti / both), what success is

THE TABLE   (2-4 lines each, concrete, aimed at this brief - no generic theory)
Dunford     - positioning read + the one change
Schwartz    - awareness level of the reader + where the copy must enter
Godin       - smallest viable audience + what makes it worth talking about
Sutherland  - the psychological reframe nobody else will suggest
Hormozi     - value equation score + how to make the offer stupid-easy to say yes to
Wiebe       - what the client's own words say; which line to steal from them
Halbert     - the hook, the hungry crowd, the single ask

THE FIGHT
2-3 real disagreements, each as "X says ... / Y says ... / it hinges on ..."

THE VERDICT
recommendation:   what to do, in one paragraph
keep / cut / add: bullets
draft:            the hook, headline, offer line or page section, in Ailyn's voice
risks:            what could go wrong; anything that would feel like pressure
not known yet:    facts about the offer or audience the board assumed or needs

NEXT
test it on: Sarah / Esti / both - the exact question to ask them
```

## Rules for Ailyn's audience (these override any board member)

Her clients are women founders with ADHD or neurodivergence, often moms, who
already shame themselves. So:

- **No fake urgency, fake scarcity, or shame hooks.** Real deadlines and real
  caps are fine, stated plainly. Halbert's and Hormozi's pressure tactics get
  translated into clarity and ease, not fear. If a member's advice crosses this
  line, say so in **risks** and give the clean version.
- **Never blame the reader.** The frame is structure, not discipline.
- **Low cognitive load wins.** One idea, one ask, short lines. Sutherland and
  Hormozi on reducing friction usually beat cleverness.
- **No invented results, testimonials or numbers.** If proof is missing, the
  board says "proof needed" under *not known yet*.
- Words to avoid: hustle, grind, 10x, crush it, guru-speak.

## Finishing

1. Any draft copy goes through `ig-human` (`python3 .claude/skills/ig-human/detect.py`)
   before it's shown as final. Fix what it flags.
2. Offer the hand-off: "Want me to run this past Sarah / Esti?" and, if yes,
   follow `talk-to-avatar` / `talk-to-esti`. The board proposes; the client
   decides.
3. If the work is an Instagram piece, point to the right `ig-*` skill to
   produce it (reel, caption, carousel, story).
