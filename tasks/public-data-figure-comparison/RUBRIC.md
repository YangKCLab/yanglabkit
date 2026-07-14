# Candidate review rubric

Score each figure independently while the generator identity is hidden. A
submission may therefore contribute zero, one, or several eventual README
figures. Record a short evidence-based note for every non-perfect category.

## Disqualifying checks

Do not score a candidate if any of these apply:

- it fails `validate_submission.py`;
- it uses the wrong input, variable mapping, figure type, or required output;
- labels, data, or marks are clipped or materially unreadable at the target
  README width;
- it uses rainbow, jet, HSV, Turbo, or an unsafe equal-luminance red–green
  distinction;
- it makes a causal or inferential claim not supported by the task; or
- it contains fabricated values, attribution, or palette metadata.

## Scoring (100 points per figure)

| Category | Points | What to evaluate |
|---|---:|---|
| Data and encoding fidelity | 25 | Inputs, values, variable mappings, plot type, transformations, and fixed histogram constraints match `task.json`. |
| Figure-convention adherence | 25 | Agent-selected axes, units, reference points, redundant encodings, spines/ticks, grid, legend/direct labels, typography, whitespace, marker scale, and layout follow `yanglabkit-figures`. |
| Colour quality | 20 | Palette class fits the variable semantics; palette is CVD-safe and perceptually appropriate; continuous colour has a scale; metadata matches the rendered choice. |
| Legibility and accessibility | 20 | The figure reads at about 3.5 inches wide, distinctions do not depend on colour alone, labels are concise, and submitted alt text accurately describes the visible figure. |
| README showcase value | 10 | The result is polished, visually economical, and helps a prospective user understand the skills' value at a glance. |

## Tie-break order

1. Higher data and encoding fidelity.
2. Higher legibility and accessibility.
3. Higher figure-convention adherence.
4. Better coherence with the other selected winners.
5. If still tied, prefer the simpler figure with less non-data ink.

## Collection review after per-figure scoring

Before promoting winners, review the mixed six-figure set together:

- Does the set demonstrate categorical, sequential, and diverging colour use?
- Are typography and apparent scale reasonably consistent?
- Does any repeated palette create a false cross-dataset semantic link?
- Do adjacent README figures feel excessively repetitive?
- Is every selected image still readable in a two-column gallery?

Selection is a human decision. The rubric organizes evidence; it does not turn
small numerical differences into an automatic winner.
