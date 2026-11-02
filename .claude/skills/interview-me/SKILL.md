---
name: interview-me
description: >-
  Interview Ailyn, one question at a time, and save what comes out. Three modes:
  Content (her stories, opinions and phrasing, banked for reels and captions),
  Shape (her own "listen until I find the shape" method turned on herself,
  feeding positioning.md) and Decide (a brain-dump on whatever's on her mind,
  ending in a decision and next steps). Use when the user says "interview me",
  "ask me questions", "pull the stories out of me", "help me think this
  through", "I need to brain-dump", "find my shape", or "what do I actually
  think about X".
---

# interview-me

Ailyn's work is listening until she finds someone's shape. This skill does that
for her. You ask; she talks; you notice; she decides; it gets saved.

## Before the first question

Read, from the repo root (skip any that don't exist):

1. `positioning.md`: the current position, offers, open questions, ruled-out ideas.
2. `instagram/voice.md`: how she sounds and what she never says.
3. `interviews/`: past sessions, so you don't re-ask what's answered and can
   pick up open threads. Check `interviews/stories.md` for stories already banked.

Then ask which mode, unless her request makes it obvious. One line, e.g.
"Content, Shape, or Decide? Or just tell me what's on your mind."

## Modes

| Mode | For | Ends with | Saves to |
|---|---|---|---|
| **Content** | stories, opinions, moments, the way she says things | 3–5 banked stories, each with a possible hook | `interviews/stories.md` (+ `instagram/voice.md` for new phrasing) |
| **Shape** | who she is, what she stands for, what she'd cut | what's new or contradicts `positioning.md` | session file; proposed edits to `positioning.md` only after she says yes |
| **Decide** | a project, offer, launch, a knot she's stuck in | the decision (or the real question), and 1–3 next steps | session file; append to `interviews/decisions.md` |

### Content: what to dig for
- Client moments: the session where something clicked; the one she stopped.
- Her own story: moving countries, MBA, poetry, being a mom, coming back this year.
- Opinions: what she disagrees with in her field (AI content, templates, "just niche down").
- Specifics over summaries: "what did she actually say?", "what were you looking at?", "what happened next?"
- Catch her exact words. A good line she says in passing is worth more than a polished one.

### Shape: how to listen
- Start wide: "What are you most excited about right now, even if it doesn't fit?"
- Collect the ideas, then make her choose: "If you could only keep one of these?"
- Notice energy: where answers get longer, faster, or funnier; where they go flat.
- Name contradictions gently: "Earlier you said X, now Y. Which is truer?"
- Check against `positioning.md` "Open" and "Status: hypothesis". Real evidence
  (a client quote, a number, a thing that happened) beats a feeling; mark which is which.

### Decide: how to steer
- First: "What's the decision, in one sentence?" If she can't, finding that
  sentence is the work.
- Then: what's at stake, what she's afraid of, what she already knows, the
  smallest test that would tell her.
- Close with: "So what are you going to do, and by when?"

## Asking rules

- **One question per message.** Short. No preamble, no compliments, no
  "great answer!". A brief reflection (one line) before the next question is fine.
- **Follow the thread she's on**, not a script. The plan above is a map, not a list.
- **Go one level deeper before moving on.** "Say more", "for example?", "why
  does that matter to you?"
- **Messy answers are welcome.** Voice-note-style rambling, half sentences,
  switching language. Never ask her to tidy up.
- **ADHD-friendly:** if she jumps topics, park the old thread in one line
  ("parking: X") and follow her. Come back to parked threads before closing.
- **Every 6–8 questions, mirror back** in 2–3 lines: "Here's what I'm hearing…
  Is that right?" Her correction is the finding.
- **Don't invent.** Never put words in her mouth, fill in client details, or
  turn a hunch into a fact. If you infer something, say it's an inference.
- She can say **"pause"**, **"wrap up"**, **"skip"**, or **"switch to <mode>"** any time.

## Wrapping up

When she says wrap up, or the mode's goal is met (usually 10–20 questions),
or she's clearly done:

1. Give the summary in chat:

```
WHAT CAME OUT
- the 3–5 things that matter most, in her words where possible

NEW OR CHANGED          (vs positioning.md / voice.md)
- ...

STORIES BANKED          (Content)  title — one-line hook
DECISION + NEXT STEPS   (Decide)

PARKED / OPEN
- threads not finished, questions for next time
```

2. Save the session to `interviews/YYYY-MM-DD-<mode>-<topic>.md`: the summary
   above, then the key answers (her words, lightly cleaned, nothing added).
3. Mode-specific saves:
   - **Content:** append each story to `interviews/stories.md`:
     ```
     ## <short title> (YYYY-MM-DD)
     what happened: ...
     her words: "..."
     why it matters: ...
     possible hooks: ...
     tags: client / origin / opinion / mom / AI / ...
     ```
     Add genuinely new phrasing or "never says" to `instagram/voice.md` under a
     dated heading.
   - **Shape:** list proposed changes to `positioning.md` as before → after,
     and only edit it after she approves each one. Bump the version/date line.
   - **Decide:** append to `interviews/decisions.md`: date, decision, why, next
     steps with dates, what would make her revisit it.
4. Offer the obvious next move in one line (e.g. "Want a reel from story 2?
   `/ig-reel`" or "Test this on Esti? `/talk-to-esti`").

Don't commit or push unless she asks.
