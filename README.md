# Introduction

`yanglabkit` is a skill set for AI agents.
It's a focused collection tailored to the [Yang Lab](https://www.kaichengyang.me)'s research workflows — **not** a general-purpose research toolkit.

Those interested in research skills that covers the broad research lifecycle can refer to the following skill sets:

- https://github.com/yy/claude-scholar
- https://github.com/letitbk/claude-academic-setup 

Skills use the portable `SKILL.md` convention, so they're usable by any AI agent that supports the standard.

## Installation

Add this repo as a Claude Code plugin marketplace, then install the `yanglabkit`
plugin:

```
/plugin marketplace add yang3kc/yanglabkit
/plugin install yanglabkit
```

Skills follow the portable `SKILL.md` convention, so any agent that supports the
standard can load a skill directly from `skills/<name>/`.

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

## License

See [LICENSE](LICENSE).
