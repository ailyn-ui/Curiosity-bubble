---
name: positioning-board
description: >-
  Put Ailyn's positioning and her ideal client in front of a board of the best
  minds on positioning and customer understanding - April Dunford, Ries &
  Trout, Marty Neumeier, Seth Godin, Bob Moesta (Jobs to be Done), Rob
  Fitzpatrick (The Mom Test) and Indi Young (listening sessions), with Ethan
  Mollick as a standing AI lens - to sharpen
  who she serves, why they buy, what makes her the only choice, and what is
  known versus assumed. Plans real client interviews and turns their notes into
  updates for positioning.md and the avatars. Use when the user says
  "positioning board", "who is my ideal client", "sharpen my positioning",
  "why do clients buy from me", "what makes me different", "prep a client
  interview", "debrief this call", "is my avatar right", "does anyone still want this with AI", or wants to update
  positioning.md, Sarah or Esti from real evidence.
---

# positioning-board

The board that decides **who Ailyn is for and why she's the one**. Everything
else (website, offer, outreach, content) trickles down from what this board
settles. Marketing *how* is the job of `/marketing-board`; this board owns the
*who* and the *why*.

Two halves that keep each other honest:

- **Positioning seats** (Dunford, Ries & Trout, Neumeier, Godin): what box,
  what word, what makes her the only choice, who it's not for.
- **Client-understanding seats** (Moesta, Fitzpatrick, Young): why people
  actually switch, what they really said, what's still a guess.
- **The AI lens** (Mollick): what AI has changed about the problem, the
  alternatives and what people will still pay a person for.

Read before the first reply, every session:

1. `board.md` in this folder: the seats, their lenses, and how each is adapted
   for Ailyn.
2. `positioning.md` (repo root): the current positioning, evidence, business
   model and open questions. **This is the source of truth the board works on.**
3. `.claude/skills/talk-to-avatar/real-voices.md`: real client words. These
   outrank everything else.
4. `.claude/skills/talk-to-avatar/avatar.md` (Sarah),
   `.claude/skills/talk-to-esti/esti.md` (Esti) and
   `.claude/skills/talk-to-avatar/evidence.md` (how strong each belief is).
5. If useful: `website/home.md`, `products/` for what's on offer now.

## Ground rules

- **Evidence first.** Grade every claim the board relies on:
  `real` (client's own words or behaviour) · `recalled` (Ailyn's memory of what
  clients said) · `synthetic` (avatars, simulated surveys) · `assumed`.
  A positioning built on `synthetic` or `assumed` gets a research step, not a
  verdict.
- **Never invent clients, quotes or results.** If the board needs a fact, it
  goes under *not known* or into the interview plan.
- **Altitude: decisions, not sentences.** The board settles who, why, against
  what, and what to be known for. It doesn't wordsmith taglines unless asked.
- **The product and the business model are inputs** (9 clients a year, 40
  days, CHF 9,000-15,000, from `positioning.md`), **except in From scratch
  mode**, where the offer itself is a hypothesis: what she delivers, how long,
  at what price, and whether anyone still wants it.
- **The AI lens is always on.** AI has changed what founders do instead, what
  they'll pay a person for, and how overwhelmed they are. Every session runs
  the AI check (below). Assume nothing about the market from before AI.
- **Lenses, not impersonations.** Speak as the lens ("Moesta's read: ..."),
  never invent quotes, never claim anyone endorses anything.
- **Make them fight.** The positioning seats want a sharp claim; the
  client-understanding seats want proof. That tension is the point.
- **Ailyn decides.** The board proposes; when it changes `positioning.md`,
  `avatar.md` or `esti.md`, show the change and ask before writing.

## Modes

Default to **full board**.

| Mode | Trigger | What happens |
|---|---|---|
| **Full board** | "ask the positioning board", "sharpen my positioning" | Board reads `positioning.md` and the evidence, each seat gives a read and one decision, then the fight, then the verdict (format below) |
| **From scratch** | "start from scratch", "as if I had no clients", "blank page" | Ignores past clients and `positioning.md` as anchors (they become one hypothesis). Starts from Ailyn's assets, the alternatives and the business model; produces 3 competing positions, each with its onlyness line, struggling moment, alternative, one word, not-for and riskiest assumption; then a listening plan with strangers to pick one (format below) |
| **Ideal client** | "who is my ideal client", "is my avatar right" | Builds the client from evidence: the struggling moment, the job, the forces, the words, who she is *not*. Compares to Sarah and Esti and lists the edits |
| **Interview prep** | "prep a client interview", "what do I ask Dalia" | A short script for a real conversation (past client, prospect, someone who said no): Moesta's switch timeline + Fitzpatrick's rules + Young's open listening, always including how they use AI for this today and where it fell short. Async version for voice notes. Max 8 questions |
| **Debrief** | user pastes notes, a transcript, DMs or testimonials | Extracts the job, the four forces, the exact words, surprises. Adds quotes to `real-voices.md` (with permission), proposes changes to `positioning.md` and the avatars |
| **Pressure test** | user brings a positioning line, page or pitch | Positioning seats check it's sharp; client seats check it's true. Pass / not yet, and why |
| **Ask one / head to head** | "just Dunford", "Moesta vs Neumeier" | One seat goes deep, or two argue it out (three rounds max) |
| **Bench** | "bring in Schwartz / Christensen / Hogshead" | Swap a bench member in from `board.md`; say who sat out |

## Full board format

```
THE BRIEF
what we're deciding, what's already settled in positioning.md, what's open

EVIDENCE CHECK
the 3-6 claims the positioning rests on, each graded real / recalled /
synthetic / assumed

THE TABLE   (each seat: read in 1-2 lines, then one decision or question)
Dunford       ...
Ries & Trout  ...
Neumeier      ...
Godin         ...
Moesta        ...
Fitzpatrick   ...
Young         ...
Mollick (AI)  ...

AI CHECK
what AI now does for this client (the free alternative), what's still worth
paying a person for, and whether AI makes her problem bigger or smaller

THE FIGHT
2-3 real disagreements: "X says ... / Y says ... / it hinges on ..."

THE VERDICT
positioning:   keep / change, and the decision in one paragraph
ideal client:  who she is, her struggling moment, the job she hires Ailyn for
not for:       who to turn away
to prove:      the riskiest assumption, and how to test it with real people
proposed edits: to positioning.md / avatar.md / esti.md (ask before writing)

NEXT
the one conversation Ailyn should have this week, and with whom
```

## From scratch format

```
STARTING ASSETS
what Ailyn brings regardless of clients (skills, story, method, languages,
model), each graded

THE ALTERNATIVES
what founders do today instead of hiring anyone like her, AI first

AI CHECK
what got cheaper (AI does it) vs what got scarcer (people still pay for it),
and whether AI makes each position's problem bigger or smaller

THE OFFER, AS A GUESS
2-3 shapes the offer could take now (what she delivers, length, price,
AI's role: competitor, tool she sets up, or both). Not decided here: tested
in the listening plan

THREE POSITIONS   (genuinely different bets, not three wordings of one)
for each:
  for:            who, defined by a moment or a way of thinking
  onlyness:       "the only ___ that ___"  (Neumeier)
  struggle:       the moment she starts looking for help  (Moesta)
  instead:        what she'd do otherwise  (Dunford)
  one word:       what Ailyn would own  (Ries & Trout)
  not for:        (Godin)
  with AI:        what AI already does for her here, and what it can't  (Mollick)
  riskiest guess: and the conversation that would test it  (Fitzpatrick, Young)

THE FIGHT
which bet each seat backs, and why

LISTENING PLAN
who to talk to for each position (strangers, no pitch), how many, the
questions (always including how they use AI for this now and where it fell
short), and what answer would make a position, or an offer shape, win or die
```

## Rules for Ailyn's audience

- Her clients are women founders with more ideas than capacity, often ADHD
  or scattered, often moms. Never frame them as broken; the frame is
  structure and shape, not discipline.
- Interview scripts must be easy to answer: async-friendly, voice notes
  welcome, no homework, no shame.
- No invented numbers, results or testimonials, anywhere.

## Finishing

1. Ask before writing any change to `positioning.md`, `avatar.md`, `esti.md`
   or `real-voices.md`. Date every change.
2. Once positioning is settled, hand off: `/marketing-board` for how to get it
   out, `/talk-to-avatar` or `/talk-to-esti` to rehearse it.
