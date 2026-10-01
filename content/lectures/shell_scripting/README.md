# Shell Scripting: Turn Repeated Commands into a Reusable Recipe

[shell_scripting.qmd](shell_scripting.qmd) is an approximately 86-minute Reveal.js lecture
for students who have completed the MQB Unix chapter. It introduces
shell scripts through a recipe metaphor. It explains the four parts of the
boilerplate before introducing one input, quoting, choices, repetition and a
small data-integrity warning.

The deck is deliberately thin. Its teaching sequence, prompts and speaker notes
live in the QMD; selected explanations and examples are embedded from
[`content/notebooks/shell-scripting.ipynb`](../../notebooks/shell-scripting.ipynb)
by semantic cell tags. Edit the notebook first when changing canonical chapter
content, and edit the QMD when changing lecture pacing or delivery.

## Render and preview

From the MQB repository root, with Quarto installed:

```bash
quarto render content/lectures/shell_scripting/shell_scripting.qmd --to revealjs
quarto preview content/lectures/shell_scripting/shell_scripting.qmd
```

Rendering creates `shell_scripting.html` beside the QMD. The HTML embeds
Reveal.js and local styles, so it is usable offline. The presentation does not
execute a notebook or run its shell examples; rehearse any live terminal work
separately on disposable data.

Before sharing or publishing the rendered HTML, remove the absolute source
notebook paths Quarto adds to embedded cells:

```bash
python3 content/lectures/shell_scripting/sanitize_html.py content/lectures/shell_scripting/shell_scripting.html
```

Run this after every render; the helper is safe to rerun.

Press `S` during the presentation to open speaker view, including the timing
notes and next-slide preview. Do not edit the generated HTML directly; edit the
QMD or the tagged notebook cells and render again.

## Reusable source blocks

The lecture currently uses these tags:

- `shell-purpose`, `shell-tool-choice`, `shell-utility-examples`, `shell-utility-fit`
- `shell-anatomy`
- `shell-boilerplate-interpreter`, `shell-boilerplate-comments`
- `shell-boilerplate-body`, `shell-boilerplate-exit`
- `shell-run-bash`, `shell-first-argument`
- `shell-quoting-prompt`, `shell-quoting-explanation`
- `shell-if-choice`, `shell-for-loop`, `tabtocsv-empty-fields`

Tagged cells are intentionally compact standard Markdown blocks. Keep MyST
admonitions, extensive setup instructions and practical-only detail in adjacent
untagged cells unless they are specifically adapted for Quarto.
