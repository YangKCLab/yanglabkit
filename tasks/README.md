# Tasks

This folder contains versioned evaluation tasks for exercising and comparing
YangLabKit skills. A task packages a concrete objective, fixed inputs, expected
outputs, validation rules, and review criteria so that different people or AI
agents can attempt the same work under comparable conditions.

Tasks are not skills and are not loaded automatically by an agent. The
canonical, reusable guidance remains in [`../skills/`](../skills/). Each task
links to the skills it evaluates and adds only the task-specific requirements
needed for a fair run.

## Included tasks

| Task | Status | Skills evaluated | Deliverables |
|---|---|---|---|
| [Public-data figure comparison](public-data-figure-comparison/README.md) | Ready for submissions | `yanglabkit-figures`, `yanglabkit-scicolor` | Six PNG figures, source code, alt text, palette metadata, and run metadata |

### Public-data figure comparison

This task gives every participant the same six plot-ready public-data inputs:
NASA GISTEMP, World Bank regional urbanization, Palmer Penguins, UCI Wine
Quality, UCI Auto MPG, and the USGS Earthquake Catalog. Participants produce a
line chart, horizontal bar chart, box plot, heatmap, scatter plot, and
histogram while applying the two figure-related skills.

The task includes:

- a human-readable brief and machine-readable task contract;
- frozen derived inputs with provenance, transformations, and checksums;
- an agent- and programming-language-neutral submission template;
- an automated PNG and metadata validator;
- a blinded HTML comparison builder with a separate identity key; and
- a transparent per-figure scoring rubric.

Candidate figures are intentionally separate from the task definition. The
task can therefore be reused across multiple agents and runs without changing
the inputs or instructions.

## Recommended setup

Run tasks from a local checkout of this repository. Before starting a new task
or candidate run, pull the latest task definitions, fixed inputs, validators,
and canonical skill sources together:

```bash
git clone git@github.com:YangKCLab/yanglabkit.git
cd yanglabkit
git pull --ff-only
```

If the repository is already cloned, only the final two commands are needed.
Use a clean checkout at the intended commit so every candidate receives the
same task version and skill version.

It is also recommended to install the task's linked skills into the local agent
environment before testing. Follow the agent-appropriate method in the root
[`Installation`](../README.md#installation) section and install from this
checkout's canonical [`skills/`](../skills/) directories. This tests the skills
through the agent's normal discovery and activation mechanism rather than
treating their Markdown files as an ad hoc prompt.

Local installers may create copies or symlinks under `.agents/skills/` or
`.claude/skills/`, plus `skills-lock.json`. Those repository-local installation
artifacts are gitignored; the tracked source of truth remains `skills/`. Reload
or start a fresh agent session after installation if the agent caches its skill
registry.

## Standard task layout

Tasks should use the following structure where applicable:

```text
tasks/<task-slug>/
├── README.md               # Human-readable objective and instructions
├── task.json               # Versioned machine-readable contract
├── data/                   # Fixed inputs, provenance, and checksums
├── submission-template/    # Required output and metadata structure
├── submissions/            # Isolated candidate runs
├── validate_submission.py  # Automated structural checks
└── RUBRIC.md               # Human review criteria
```

A task may add preparation or comparison utilities when needed, but candidate
generation code belongs inside each submission rather than in the task itself.

## Running a task

1. Open the task's `README.md` and its linked YangLabKit skill files.
2. Use the committed inputs without fetching replacements or newer values.
3. Copy the submission template into a directory named
   `<agent-harness>_<model>_<run-id>` and use the same `submission_id` in its
   metadata.
4. Produce the required outputs and retain the complete generating source.
5. Run the task's validator before adding the submission to a comparison.
6. Keep generator identity hidden until rubric-based scoring is complete.

## Conventions for new tasks

- Keep instructions portable across agent vendors and coding environments.
- Give the task a stable ID and version whenever inputs affect comparability.
- Record authoritative sources, reuse terms, transformations, and checksums.
- State which task-specific rules override a general skill default.
- Separate immutable task materials from generated submissions and comparisons.
- Provide machine validation for objective requirements and a rubric for
  judgments that require human review.
- Add every new task to the index above.
