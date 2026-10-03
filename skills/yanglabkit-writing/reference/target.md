# yanglabkit-writing — Target

The acceptance spec for a revised or drafted passage. Mode-independent: an
interactive session runs it as the final check before a diagnosis ships; an
automated run (via `yanglabkit-goalrun`) treats it as the definition of done.

Items are numbered 1:1 to the principles in the level files — `W1.4` checks
P1.4 — so every "no" points to exactly one rule to apply. `WK` items check the
preservation rules in `method.md`. A run checks the items of the levels in its
scope, highest level first; `WK` items apply whenever a P0 Argument or P1
Structure change was made. There are deliberately **no mechanical items**:
these checks are all judgment, which caps this skill's automation at
judge-based runs. Each pass/fail is a judgment call backed by one line of
evidence.

Tier semantics: `[judged]` — must pass, with evidence; `[advisory]` — reported,
never blocking.

## Items — P0 Argument

- W0.1 `[judged]` The piece's claim can be written in one disputable sentence?
  (A descriptive passage is `n/a` with the reason noted.) → P0.1
- W0.2 `[judged]` Each question the stated reader judges by has a stated
  answer, in a place this reader will look? → P0.2
- W0.3 `[judged]` Every claim has support of the right kind and amount, with a
  stated reading, placed with it? → P0.3
- W0.4 `[judged]` Every conclusion follows from what is stated, with no premise
  left for the reader to supply? → P0.4
- W0.5 `[judged]` Verbs, quantifiers, and scope match the strength of the
  evidence — neither overclaimed nor over-hedged? → P0.5
- W0.6 `[advisory]` The objections this reader is likely to raise are answered
  where they arise? → P0.6

## Items — P1 Structure

- W1.1 `[judged]` The parts that carry the claim get the most space, counting
  figures and captions? → P1.1
- W1.2 `[judged]` Each paragraph builds only on what earlier ones established —
  ordered by the argument's logic, not a surface taxonomy? → P1.2
- W1.3 `[judged]` Each paragraph holds one theme, and each recurring theme
  lives in one place, located where it does its work? → P1.3
- W1.4 `[judged]` Reading only the first sentence of each paragraph
  reconstructs the argument? (A deliberate payoff paragraph is `n/a` with the
  reason noted.) → P1.4
- W1.5 `[judged]` No main-line paragraph is interrupted by background? → P1.5
- W1.6 `[judged]` Each unfamiliar concept is introduced before use, one new
  idea per step, with nothing explained below the stated reader's level?
  → P1.6

## Items — P2 Flow

- W2.1 `[judged]` Every sentence is framed by its local job, not by the
  grandest framing it could carry? → P2.1
- W2.2 `[judged]` No connective verb that merely restates the section's
  premise? → P2.2
- W2.3 `[judged]` Each thing keeps one name throughout the document? → P2.3
- W2.4 `[judged]` Every sentence parses in one pass — no nested clauses,
  subject near its verb — without collapsing into choppy fragments? → P2.4

## Items — P3 Polish

- W3.1 `[judged]` No sentence restates a point already made — by its neighbor
  or by an earlier section? → P3.1
- W3.2 `[judged]` No two sentences assert the same effect, and no sentence
  survives whose only job is defining a noun in the previous one? → P3.2
- W3.3 `[judged]` No sentence could lose words without losing an idea? → P3.3
- W3.4 `[judged]` No abstract label that needs a gloss where the concrete
  thing could be named? → P3.4
- W3.5 `[advisory]` Every word a P2 Flow or P3 Polish edit *added* does
  load-bearing work? → P3.5

## Items — preservation (after a P0 Argument or P1 Structure change)

- WK1 `[judged]` Every original claim is still made, or its removal is listed?
  → K1
- WK2 `[judged]` Every number, citation, quotation, and example survives, or
  its removal is listed? → K2
- WK3 `[judged]` Scope limits, conditions, and stated uncertainty are intact?
  → K3
- WK4 `[advisory]` The writer's phrasing survives wherever it was not the
  problem? → K4

## Target report (automated mode)

Write `<text-stem>.target-report.md` next to the file. State the scope on the
first line, with level names, then one line per item in scope
(`id pass|fail|n/a — one-line evidence`), grouped under the level headings
above. Done = every `[judged]` item in scope `pass` or `n/a` with reason;
`[advisory]` items (W0.6, W3.5, WK4) are reported either way and never block.
A `fail` on W0.1, or a W0.2–W0.4 `fail` that needs a fact the text does not
contain, cannot be fixed by iterating: stop the run, write the report, and
name what the writer must supply.

Automated runs follow the branch contract in `yanglabkit-goalrun`: edits are
applied and iterated on a dedicated `goalrun/<slug>` branch, committed and
pushed as the run progresses, and reviewed as one branch diff before the user
merges. Interactive sessions keep propose-before-apply and run these items as
the pre-ship checklist instead.
