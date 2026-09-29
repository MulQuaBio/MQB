# Introduction to Computing

[intro_computing.qmd](intro_computing.qmd) is a beginner-friendly computing lecture for
biology/ecology MSc students using Linux or macOS. It produces **Reveal.js**
slides with Quarto, not a Jupyter RISE slideshow.

## Render and Present

From the MQB repository root, with [Quarto](https://quarto.org/docs/get-started/)
installed:

```bash
quarto render content/lectures/intro_computing/intro_computing.qmd --to revealjs
```

Open the generated HTML beside the source in a browser. Images and presentation
resources are embedded, so the slides do not require a network connection;
external reading links still do. The demo CSV is a separate file, not embedded
in the HTML. No Python or R kernel is needed and rendering executes no examples.

For live preview and speaker view:

```bash
quarto preview content/lectures/intro_computing/intro_computing.qmd
```

Press `S` in the presentation to open speaker notes; allow the speaker-view popup
if the browser blocks it. Use preview if the browser restricts speaker view for
a locally opened HTML file. Notes include timings, questions and demo fallback
outputs. Rehearse at the projector's resolution before teaching.

## Timing

The 15 slides budget **20 minutes**, including a two-minute terminal demo,
a one-minute pipe example and one minute for a closing question. Times are
targets for delivery, not automatic slide advancement.

| Time | Focus |
| :-- | :-- |
| 00:00-03:30 | Biological motivation and explicit analysis instructions |
| 03:30-06:00 | Computer, operating system, terminal and shell |
| 06:00-09:00 | Why Linux/*nix?! Names, benefits and limits |
| 09:00-11:30 | Files, paths and reading a command |
| 11:30-14:30 | Terminal demo and connecting tools with a pipe |
| 14:30-17:30 | Multilingual workflows and safe scientific habits |
| 17:30-20:00 | Understanding check, next steps and a question |

## Demo Setup

Before teaching, open a separate terminal in the lecture folder. From the
repository root:

```bash
cd content/lectures/intro_computing
```

Enlarge the terminal font. Students can watch rather than type along. Run:

```bash
pwd
ls
head -n 4 data/computing-demo.csv
grep '^woodland,' data/computing-demo.csv
grep '^woodland,' data/computing-demo.csv | wc -l
```

[data/computing-demo.csv](data/computing-demo.csv) contains six **synthetic**
plant-observation rows, invented for this lecture. There are three woodland
observations, representing two sites and two species. The final command prints
`3`, possibly preceded by spaces. It does not estimate diversity or test a
habitat effect. The file has a header and one newline-terminated record per line;
the line-based filter is not a general CSV parser.

These commands are read-only and use options supported by common Linux and
macOS tools. They need no network, extra packages, administrator privileges or
file creation. If the live terminal is unavailable, use the fallback outputs
in the speaker notes. Platform behaviour has been tested locally on Linux;
macOS should be checked on the teaching machine before delivery.

## Sources

- [MQB introduction](../../intro.md): multilingual computing and workflow habits.
- [MQB Unix chapter](../../notebooks/unix.ipynb): Unix concepts and command-line tools.

The lecture adapts these sources for beginners and qualifies older platform
generalisations rather than repeating them. The reused xkcd image is credited
on its slide, with its original licence link. Publishing the lecture is a
separate step; it is not added to the book's table of contents here.
