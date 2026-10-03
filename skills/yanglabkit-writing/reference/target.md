# yanglabkit-writing — Target

The acceptance spec for a revised or drafted passage. Mode-independent: an
interactive session runs it as the final check before a diagnosis ships; an
automated run (via `yanglabkit-goalrun`) treats it as the definition of done.

Every item cites exactly one principle — every "no" points to one rule to
apply. `WA`, `WS`, and `WK` items cite `argument-structure.md`; `W1`–`W12` are
numbered 1:1 to the principles in `prose-principles.md`. A tightening-only
request checks `W1`–`W12`; a full revision checks all items, higher levels
first. There are deliberately **no mechanical
items**: prose checks are all judgment, which caps this skill's automation at
judge-based runs. Each pass/fail is a judgment call backed by one line of
evidence.

Tier semantics: `[judged]` — must pass, with evidence; `[advisory]` — reported,
never blocking.

## Items — argument

- WA1 `[judged]` The piece's claim can be written in one disputable sentence?
  (A descriptive passage is `n/a` with the reason noted.) → A1
- WA2 `[judged]` Each question the stated reader judges by has a stated
  answer, in a place this reader will look? → A2
- WA3 `[judged]` Every claim has support of the right kind and amount, with a
  stated reading, placed with it? → A3
- WA4 `[judged]` Every conclusion follows from what is stated, with no premise
  left for the reader to supply? → A4
- WA5 `[judged]` Verbs, quantifiers, and scope match the strength of the
  evidence — neither overclaimed nor over-hedged? → A5
- WA6 `[advisory]` The objections this reader is likely to raise are answered
  where they arise? → A6

## Items — structure

- WS1 `[judged]` The parts that carry the claim get the most space, counting
  figures and captions? → S1
- WS2 `[judged]` No main-line paragraph is interrupted by background? → S2
- WS3 `[judged]` Each unfamiliar concept is introduced before use, one new
  idea per step, with nothing explained below the stated reader's level? → S3

## Items — preservation (after a restructure)

- WK1 `[judged]` Every original claim is still made, or its removal is listed?
  → K1
- WK2 `[judged]` Every number, citation, quotation, and example survives, or
  its removal is listed? → K2
- WK3 `[judged]` Scope limits, conditions, and stated uncertainty are intact?
  → K3
- WK4 `[advisory]` The writer's phrasing survives wherever it was not the
  problem? → K4

## Items — prose

- W1 `[judged]` No sentence restates a point already made — by its neighbor or
  by an earlier section? → principle 1
- W2 `[judged]` No two sentences assert the same effect, and no sentence
  survives whose only job is defining a noun in the previous one? → principle 2
- W3 `[judged]` No connective verb that merely restates the section's premise?
  → principle 3
- W4 `[judged]` No sentence could lose words without losing an idea?
  → principle 4
- W5 `[judged]` Every sentence parses in one pass — no nested clauses, subject
  near its verb — without collapsing into choppy fragments? → principle 5
- W6 `[judged]` Each paragraph holds one theme, and each recurring theme lives
  in one place, located where it does its work? → principle 6
- W7 `[judged]` Each paragraph builds only on what earlier ones established —
  ordered by the argument's logic, not a surface taxonomy? → principle 7
- W8 `[judged]` Reading only the first sentence of each paragraph reconstructs
  the argument? (A deliberate payoff paragraph is `n/a` with the reason noted.)
  → principle 8
- W9 `[judged]` Every sentence is framed by its local job, not by the grandest
  framing it could carry? → principle 9
- W10 `[judged]` No abstract label that needs a gloss where the concrete thing
  could be named? → principle 10
- W11 `[advisory]` Every word the revision *added* does load-bearing work?
  → principle 11
- W12 `[judged]` Each thing keeps one name throughout the document?
  → principle 12

## Target report (automated mode)

Write `<text-stem>.target-report.md` next to the file, one line per item
(`id pass|fail|n/a — one-line evidence`). Done = every `[judged]` item `pass` or `n/a`
with reason; `[advisory]` items (WA6, WK4, W11) are reported either way
and never block. A `fail` on WA1, or a WA2–WA4 `fail` that needs a fact the
text does not contain, cannot be fixed by iterating: stop the run, write the
report, and name what the writer must supply.

Automated runs follow the branch contract in `yanglabkit-goalrun`: edits are
applied and iterated on a dedicated `goalrun/<slug>` branch, committed and
pushed as the run progresses, and reviewed as one branch diff before the user
merges. Interactive sessions keep propose-before-apply and run these items as
the pre-ship checklist instead.
