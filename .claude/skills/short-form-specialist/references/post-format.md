# The post format

The exact output contract: how posts are delivered, what the two memory notes contain, the log line, and the writing rules. Every post must stand alone: a reader who sees only that post gets the whole idea.

## Writing rules (non-negotiable)

- **Plain spoken language**, short words, short sentences. Every opening line passes the say-it-out-loud test.
- **No em dashes.** Periods, commas, colons.
- **No jargon**: no salience, narrative, discourse, reframe-as-a-noun, or the usual AI filler words. Banned frames at most once per day across all posts: "X is not Y, it's Z", "You don't need X, you need Y", "Stop X. Start Y", "Most people think X".
- The creator's own vocabulary, named concepts, and rhythm from the Voice and pillars note. A post that could belong to any growth account is a failed post.
- Never eight or more words in a row from any source. Borrow the shape, never the sentences.
- Never diagnose, dismiss, or redefine a medical or mental-health condition for a hook.
- Post ids and item ids never appear in prose. Receipts render as data lines.
- Honest when thin: if only one post clears the bar, deliver one and say why.

## Delivering a post in chat

Each post is its own block so the creator can save, edit, or reject any one of them. Order: the header line, a blank line, the post text exactly as it would be published, then up to three short lines.

```markdown
**Post 1 · X · concise assertion**

{the post text, exactly as it would be published; thread segments separated by a line with three dashes}

Rides: {angle family} · {opening family} · {ending family}
Receipt: @{handle} ({platform}) · {N.N}x baseline · {what its shape proved, one line}
Unverified: {anything the creator should check before it goes out, or omit this line}
```

After the last post, at most three lines: where today's material came from, which posts went where (draft saved on [account], saved as a note, shown in chat only), and the one post to lead with today and why.

**Live chat, first delivery only**, add one more line: the routine offer from the skill.

**Unattended run** (a scheduled task or cron): print the full text of every post labeled with its angle and where it was saved, then one line saying drafts are waiting in the Scheduler. Nothing else.

## The Post log line

One line per handed-over post, newest first. Append at the top of the list when the tool allows; otherwise append at the end and read the whole log by date.

```
YYYY-MM-DD · {platform} · {the claim in ten words or less} · {angle family} · {opening family} · {shape} · {draft saved | scheduled by ask | shown in chat | saved as note}
```

Under the day's lines, when a Weekly ideas row was used: `used memo row: {row's claim, first six words}`.

## The Voice and pillars note (under 600 words, living)

```markdown
# Voice and pillars

## Setup

Workspace: {name}. Platform and handle: {platform @handle}. Second platform: {or none}.
Posts per day: {1 to 3}. Scheduler: {account label, scheduleId, timezone}. Standing instruction: {save approved posts as drafts: yes | no | not asked}.
Brand source: {Brand throughline | Brand strategy note | four answers}.

## Who and against what

{two to four lines: who they write for, what they are against}

## Pillars

- {pillar}: {the recurring claim in one line}
- ...

## Vocabulary and named concepts

{their words, their names for things, comma separated}

## How they write

{sentence length, rhythm, certainty, humor, directness, favorite shapes; three to five lines}

## Proven shapes

- {hook shape or post shape} · {N.N}x baseline · {pillar} · {date of the refresh}
- ...

## Never

{what they never do; two to five lines}

## Change log

- YYYY-MM-DD: created from {source names}
- YYYY-MM-DD: {one line per change}
```

Keep it under 600 words by replacing lines, never by appending. Every edit adds a Change log line. Unattended runs may add only a proven-shapes line or a vocabulary term.

## Styled delivery

Posts are the deliverable and belong in chat as text the creator can copy. The styled document is a companion, used when the day has two or more posts:

1. **HTML artifact / file**: `assets/daily-posts-template.html`. Replace the `{{...}}` slots and repeat the marked post block. Keep its design; do not restyle it.
2. **Markdown**: the chat blocks above, exactly.

The memory writes (Post log append, Voice and pillars edits) happen regardless of how the posts were shown.
