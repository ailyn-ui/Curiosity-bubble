# The Offer Blueprint format

The exact output contract. The deliverable is one editable Eden note that holds only the blueprint. Coaching, commentary, and next steps stay in chat. A reader who opens only the note should be able to hand it to a copywriter and get a landing page back.

## Writing rules (non-negotiable)

- **Plain spoken language.** Short words, short sentences. Every promise must pass the say-it-out-loud test in front of a real customer.
- **No em dashes.** Use periods, commas, colons.
- **Banned words**: delve, tapestry, unleash, unlock, leverage, robust, journey, landscape, navigate, foster, harness, vibrant, dynamic, holistic, paradigm, game-changing, revolutionary, transform (as hype), effortless, guaranteed results.
- **No AI frames**: "X is not Y, it's Z", "You don't need X, you need Y", "Stop X. Start Y", "Most people think X".
- **Never invent** numbers, results, testimonials, or market facts. A number appears only when the user gave it or a tool returned it.
- **Mark suggestions.** Any component built by inference rather than verified fact carries the tag `(suggested)` at the end of its first line. Any claim that needs proof carries `(needs proof: ...)` naming what would prove it.
- **No manufactured scarcity or urgency.** No income or health promises the product cannot support. No guarantee the seller's economics cannot survive.
- **Clarity over completeness.** A thin section written honestly beats a full section padded with guesses.

## The note

- **Title**: `Offer Blueprint: [product name]`. Use the product's working name, not the mechanism name, so it stays findable.
- **Location**: the **"Offers"** board. Create the board with `eden_create_board` when missing.
- **One note per product.** Revisions go into the same note with `eden_update_note` and the `baseContentHash` from the last read. Never create a second blueprint for the same product.
- **Contents**: only the sections below, in this order, with these exact headings.

```markdown
# Offer Blueprint: {product name}

{One line: who this is for and the one outcome, under 25 words.}

## First Product Decision

{Only when phase one ran. Three lines: the option chosen and why in one line; the two runners-up, each with the one-line reason it lost.}

## Target Audience

{One tight paragraph: who exactly, their situation, what they have tried. Ends with: Awareness level: {level}.}

## Delivery Mechanism

{The format and why it fits this buyer and this seller's week. One short paragraph.}

## Big Idea

{One concise articulation of the promise. One or two sentences.}

## Big Problem

{The primary pain, framed for the awareness level. One short paragraph.}

## Irking Pain Points

1. {pain point}
2. {sharper}
3. {sharper still}
4. {the one they do not say out loud}

## Quantifiable Outcome

{A measurable result with a timeframe. Best real result and typical result when both exist. Tag proof gaps.}

## Risk Reversal

{The guarantee type, the promise, and the conditions stated plainly. One paragraph.}

## Unique Mechanism

**{Mechanism name}**

1. {Phase one: what happens and what it produces}
2. {Phase two}
3. {Phase three}
   {three to six phases total}

## Features and Benefits

- **{Feature}**: removes {the obstacle it removes}
- **{Feature}**: removes {obstacle}
  {one line per stack item; bonuses listed last and labeled Bonus}

## Value Equation Analysis

- **Dream outcome**: {what the offer does for this lever, and how strong it is}
- **Perceived likelihood**: {same}
- **Time delay**: {same}
- **Effort and sacrifice**: {same}
  {End with one line: pulls hardest on {lever(s)}; weakest on {lever}.}

## Positioning Recommendations

{How to communicate the offer across their channels. When research ran: what similar offers promise and where this one stands apart, citing only what the tools returned. When it did not: say the section was written without market research.}

## Pricing

{The recommended price. The arithmetic: the quantified outcome, the fraction captured, what the price signals. Any lead product in front of it, with its price. Provisional when the outcome number is a proof gap.}
```

## Styled delivery

The blueprint is a document. In order of preference:

1. **HTML artifact / file**: use `assets/offer-blueprint-template.html`. Replace the `{{...}}` slots, repeat the marked blocks (pain points, mechanism phases, features), and delete the First Product Decision block when phase one did not run. Keep its design; do not restyle it.
2. **Markdown**: the note template above, exactly.

In every case, ALSO save the markdown to the Eden note `Offer Blueprint: [product]` on the "Offers" board. That note is the input the Marketing Strategist reads, and the memory a later session revises.

## The chat close

After delivering, close in chat with three short parts:

1. The two or three components that carry `(suggested)` or `(needs proof)` tags, so they know what to correct first.
2. One question: which component do you want to refine?
3. One line on the next step: the blueprint feeds the landing page copy and the daily promotions (the Marketing Strategist reads it from the "Offers" board).
