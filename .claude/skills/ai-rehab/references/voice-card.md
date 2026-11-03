# Voice card, quick-start, and always-on lines

## The voice card

Any voice source (a voice skill, project instructions, the user's own instructions, or samples) reduces to one card:

- **Writer:** who is writing and in what role.
- **Reader:** who reads it and what they need.
- **Sounds like:** 3 to 5 habits, each shown by a real line.
- **Never:** words, moves, and topics the writer avoids.
- **Rhythm and marks:** sentence length, how thoughts join, punctuation habits (dashes, exclamation marks, emojis, all-caps), and how pieces end.
- **Real lines:** 2 or 3 short lines the writer confirmed are their own.

## Quick-start (optional, only when the user asks)

Starts with "build my voice" or when the user pastes samples of their own writing.

1. Ask for 3 pieces the user wrote themselves: posts, emails, or messages. Say plainly: "Skip anything AI or a copywriter wrote, and anything a client wrote."
2. Write each sample to its own file and run `python3 scripts/count_tells.py scan FILE --json` on each, to see how they write: sentence length, dashes, exclamation marks, warmth, and the tells they already use on purpose.
3. Build the card. Every habit must trace to a line in the samples. Never invent a catchphrase.
4. Show the card and ask: "Does this sound like you? Point at anything that's off." Fix it once.
5. Ask which lines under "Real lines" are theirs to keep. Keep only those.
6. Use the card for this chat, and hand back one line, under 1,500 characters, to save:

```
My writing voice for AI Rehab: [Writer]. Reader: [reader]. Sounds like: [habits]. Never: [never-list]. Rhythm: [rhythm and marks]. Real lines: "[line]" "[line]".
```

Where to save it:
- Claude: click your initials (lower left), then Settings, then "Instructions for Claude". Paste it on a new line.
- ChatGPT: Settings, then Personalization, then Custom instructions. Paste it in.

Once saved, it counts as the user's own instructions, so AI Rehab uses it in every chat. For a deeper match, point them to a full voice-building skill.

## Always-on line

To make AI Rehab run on everything Claude writes for the user, and on text they paste with no other words, they save this line in "Instructions for Claude":

```
Use my ai-rehab skill on everything you write for me and on any text I paste without other instructions. My other instructions win if they conflict. "Skip rehab" means skip it for that message.
```

It adds to their existing instructions. To turn it off, they open the same setting and delete the line. "Stop rehab" in a chat should give them these steps.

## Banned words line

"Add 'X' to my banned words" means: treat X as a tell from now on and hand back the updated line to save in the same setting:

```
AI Rehab banned words: [word], [word], [word].
```
