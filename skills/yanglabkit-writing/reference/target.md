# yanglabkit-writing — Target

The acceptance spec for a revised or drafted passage. Mode-independent: an
interactive session runs it as the final check before a diagnosis ships; an
automated run (via `yanglabkit-goalrun`) treats it as the definition of done.

Items are numbered 1:1 to the principles in `prose-principles.md` — every "no"
points to exactly one rule to apply. There are deliberately **no mechanical
items**: prose checks are all judgment, which caps this skill's automation at
judge-based runs. Each pass/fail is a judgment call backed by one line of
evidence.

Tier semantics: `[judged]` — must pass, with evidence; `[advisory]` — reported,
never blocking.

## Items

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

## Target report (automated mode)

Write `<text-stem>.target-report.md` next to the file, one line per item
(`id pass|fail|n/a — one-line evidence`). Done = W1–W10 all `pass` or `n/a`
with reason; W11 is reported either way and never blocks.

Automated runs follow the branch contract in `yanglabkit-goalrun`: edits are
applied and iterated on a dedicated `goalrun/<slug>` branch, committed and
pushed as the run progresses, and reviewed as one branch diff before the user
merges. Interactive sessions keep propose-before-apply and run these items as
the pre-ship checklist instead.
