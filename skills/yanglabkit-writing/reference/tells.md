# AI tells

A cross-level scan of `yanglabkit-writing`. The level files describe what good
text does; this file lists the moves by which machine-written text is
recognized. It serves two jobs:

- **Scan the text.** Each tell carries a level tag. A run includes the tells
  of the levels in its scope; a request to "unslop" or to check whether text
  "sounds like AI" runs the tells alone.
- **Audit your own output.** Replacement text and new drafts are where tells
  enter. Before presenting any replacement or draft, reread it against this
  list. A replacement that adds a tell is worse than the original sentence.

Machine-written text is recognized by its moves. A word list is only a hint: a
model told to avoid a word switches to a synonym and keeps the move. Each tell
below names the move, then gives examples.

Rules for every tell:

- Never introduce one. Remove one when you find it, and cite it by ID and name
  ("T3 tail participle clause").
- Removing a tell must not remove a claim, a number, or a citation. If the
  claim survives only with the tell, keep the claim and flag the tell.
- A tell is a move, not a word. Keep a listed word when it is a technical term
  in context or the field's own name for the thing.

Adapted from the `unslop` skill in
[pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan
(MIT), reworked from word lists into moves and extended with academic cases.

## Content

- **T1 Significance inflation** · P3 Polish. A sentence asserts importance,
  scale, or momentum instead of stating a fact. "In today's rapidly evolving
  landscape", "has become an indispensable part of", "plays a crucial role",
  "a testament to", "paving the way for", "despite these challenges, the field
  continues to". Replace with the specific fact, or delete.
- **T2 The swap test** · P3 Polish. A sentence that could appear unchanged in
  another paper, proposal, or project's post says nothing about this one. Cut
  it, or make it specific to this work. Boilerplate a venue requires (data
  availability, ethics statements) is exempt.
- **T3 Tail participle clauses** · P3 Polish. A trailing "-ing" clause that
  comments on the sentence it hangs from. "..., highlighting the importance of
  X", "..., underscoring the need for Y", "..., ensuring Z", "..., showcasing
  W". Delete it, or make it its own sentence with its own evidence.
- **T4 Filler assertions** · P3 Polish. Words that announce a point instead of
  making it. "It is worth noting that", "Importantly", "Notably", "In other
  words", "This means that", "Overall", a closing sentence that restates the
  paragraph, a transition whose only job is to sound connected ("Building on
  this", "With this in mind"). Delete. (The restating forms are also P3.1.)
- **T5 Unattributed consensus** · P0 Argument. "Studies have shown", "prior
  work suggests", "it is widely recognized", "experts agree" with no citation
  attached. Keep the claim as written; do not delete it or restate it as fact.
  Ask the writer for the citation. Never invent one. (See P0.3.)

## Sentence moves

- **T6 Contrast frames built for rhythm** · P2 Flow. "not X but Y", "not only
  X but also Y", "X rather than Y", "it's not about X, it's about Y" when the
  reader never held X. State Y.
- **T7 Cadence triplets and false ranges** · P2 Flow. Three items where the
  natural number is two or five. "From X to Y" where X and Y are not on a
  scale ("from health rumors to political propaganda"). Use the real list.
- **T8 Verbs that dress up "is"** · P3 Polish. "serves as", "stands as",
  "represents", "acts as", "boasts", "features", "offers". Write "is" or
  "has".

## Words

- **T9 Elevated vocabulary** · P3 Polish. An abstract or elevated word where a
  plain one exists. Delve, crucial, pivotal, landscape, tapestry, underscore,
  leverage, utilize, robust, nuanced, holistic, foster, navigate, testament,
  garner, intricate, interplay, enhance, showcase, vibrant, facilitate,
  numerous, "Additionally". Use the plain word: use, help, many, also, strong,
  improve. Keep a word that is a technical term in context ("robust to label
  noise", "a robust standard error").
- **T10 Metaphor nouns as technical terms** · P3 Polish. Paradigm, substrate,
  scaffolding, north star, flywheel, lens, vector (outside math), bedrock,
  wedge. Keep a term when it is the field's name for the thing (agent harness,
  information ecosystem, API primitive). Replace it when it stands in for a
  plainer word. (See P3.4.)
- **T11 Synonym cycling** · P2 Flow. Rotating names for one referent: users,
  accounts, individuals; model, system, approach, framework. Pick one term per
  referent and repeat it. This is the same rule as P2.3 (one name per thing):
  in a run that includes P2 Flow, report it there; in a tells-only run, report
  it as T11.

## Punctuation

- **T12 Punctuation as rhythm** · P2 Flow. Em-dashes the author did not use
  elsewhere in the piece (do not swap them for parentheses; that is the same
  move). Colons as mid-sentence connectors or reveals ("The result: ...").
  Inverted openers ("Worse than slow: ..."). Sentence fragments for emphasis.
  Rhetorical questions. Use a period or a comma.
- **T13 Hedge and intensifier stacks** · P3 Polish. "may potentially", "could
  possibly suggest", "significantly / dramatically / remarkably improves"
  where a number exists. Keep one hedge. Use the measured value. Keep
  "significant" only when it reports a statistical test. (Whether the hedge
  matches the evidence at all is P0.5.)

## Markdown only

- **T14 Formatting tells** · P3 Polish. A bold label and colon that restate
  the line ("**Speed:** speed improved 12%"), bold on every proper noun, Title
  Case headings, emoji in headings or bullets, curly quotes, a bullet list
  where a sentence would do. Convert to prose, sentence case, straight quotes.
  A bold lead-in that ends in a period and is followed by new detail is fine.
  Slide decks and other formats where bullets are the unit are exempt from the
  bullet-list rule.

## Delivery

The shared delivery rules in `method.md` apply: affirm first, evidence for
every finding, questions for the writer, a "Net:" line.

- **In a level run,** tells are listed with that level's findings, each with
  a drop-in replacement and the tell ID and name as the reason.
- **In a tells-only run,** state the scope as "AI tells only", list the items
  in document order — one item per sentence, naming every tell in it — and
  check only the `WT` items of `target.md`. Any other problem noticed while
  reading (a missing claim, a misplaced section) gets one line with its level
  name and no fix. End with a "Net:" line saying whether the passage as a
  whole reads as machine-written, and which tells drive that.
- **T5 has no replacement.** It is a question for the writer.
