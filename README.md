# Introduction

`yanglabkit` is a skill set for AI agents.
It's a focused collection tailored to the [Yang Lab](https://www.kaichengyang.me)'s research workflows — **not** a general-purpose research toolkit.

Those interested in research skills that covers the broad research lifecycle can refer to the following skill sets:

- https://github.com/yy/claude-scholar
- https://github.com/letitbk/claude-academic-setup 

Skills use the portable `SKILL.md` convention, so they're usable by any AI agent that supports the standard.

## Installation

Each skill lives in its own folder under `skills/<name>/` and follows the portable
`SKILL.md` convention, so any agent that reads markdown instruction files can use
it. Compatible with Claude Code, Cursor, Windsurf, GitHub Copilot, and others.
Pick whichever install approach fits your agent.

### Claude Code plugin (recommended)

Add this repo as a plugin marketplace, then install the `yanglabkit` plugin — this
registers every skill in the set and keeps them updatable:

```
/plugin marketplace add YangKCLab/yanglabkit
/plugin install yanglabkit
```

### Clone into your agent's skills directory

Clone the repo, then point your agent at the individual skill folder(s) you want:

```bash
# Claude Code — clone, then symlink the skill you want into ~/.claude/skills/
git clone git@github.com:YangKCLab/yanglabkit.git ~/src/yanglabkit
ln -s ~/src/yanglabkit/skills/yanglabkit-scicolor ~/.claude/skills/yanglabkit-scicolor

# Cursor — link into your project (or global) rules/skills directory
ln -s ~/src/yanglabkit/skills/yanglabkit-scicolor .cursor/skills/yanglabkit-scicolor

# Any agent — clone anywhere, then point it at skills/<name>/SKILL.md
git clone git@github.com:YangKCLab/yanglabkit.git /path/to/yanglabkit
```

### `skills` CLI

For agents that support the [`vercel-labs/skills`](https://github.com/vercel-labs/skills) CLI:

```bash
npx skills install https://github.com/YangKCLab/yanglabkit
```

Once a skill is available to your agent, it activates automatically when your
request matches its description.

## Skills

- **[`yanglabkit-scicolor`](skills/yanglabkit-scicolor/SKILL.md)** — Pick a
  scientifically sound colour palette for a figure, chart, heatmap, map, slide,
  or UI. Applies the decision logic from Crameri et al. (2020), [*"The misuse of
  colour in science communication"*](https://www.nature.com/articles/s41467-020-19160-7),
  to a self-contained snapshot of the lab's
  [scicolor](https://github.com/yang3kc/scicolor) palettes and returns concrete
  hex codes (discrete or continuous). Defaults to colourblind-safe, perceptually
  uniform choices and refuses rainbow/jet. No runtime dependencies — pure
  markdown + bundled JSON.
- **[`yanglabkit-figures`](skills/yanglabkit-figures/SKILL.md)** — Style
  matplotlib/seaborn figures the Yang Lab way: minimal, print-first design with
  spines dropped by plot type, frameless legends, percentage axes, gray dashed
  reference lines, and vector PDF export, with colour deferred to
  `yanglabkit-scicolor`. Refuses pie charts and rainbow/jet. Triggers when you
  write plotting code or ask how to style/export a scientific figure. No runtime
  dependencies — pure markdown guidance.

## License

See [LICENSE](LICENSE).
