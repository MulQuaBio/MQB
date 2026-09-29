# MQB Introductory Lectures

This area contains two standalone Quarto Reveal.js presentations with different
purposes:

- [mqb_intro.qmd](mqb_intro.qmd) is a course-neutral orientation to computational
  methods in ecology and evolution. It motivates the scientific questions,
  applications, models, data, reproducibility, and practical toolchain.
- [intro_computing.qmd](../intro_computing/intro_computing.qmd) is a separate
  beginner computing lecture. It introduces operating systems, terminals,
  shells, paths, simple Unix commands, and a short live demonstration.

The first deck should not absorb the terminal tutorial or daily practical tasks
from the second deck.

## Render and Preview

From the MQB repository root, with [Quarto](https://quarto.org/docs/get-started/)
installed, render the orientation deck with:

```bash
quarto render content/lectures/intro_talk/mqb_intro.qmd --to revealjs
```

This creates `content/lectures/intro_talk/mqb_intro.html`. The HTML embeds the
Reveal.js runtime, stylesheet, and local images, so the presentation remains
usable without a network connection. The YouTube video is intentionally external
and requires network access.

Preview the presentation with:

```bash
quarto preview content/lectures/intro_talk/mqb_intro.qmd
```

Use preview when presenting the video. YouTube may reject playback from a page
opened directly with a `file://` URL because it has no HTTP referrer. The video
slide includes a direct link for blocked playback, and the rest of the deck works
offline.

The source contains no executable notebook cells, and rendering requires no
Python, R, Jupyter, or IPython kernel. Do not edit the generated HTML directly;
change the QMD and render it again.

These presentations are standalone teaching materials. They are not included in
the Jupyter Book table of contents or its deployment workflow.
