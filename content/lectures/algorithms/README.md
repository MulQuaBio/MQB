# Algorithms: solving problems with computation

This MQB lecture adapts Stanislav (Stanley) Modrak's *Analysis of algorithms*,
including the 61-page Bootcamp lecture supplied on 27 October 2026, itself
adapted from Robert Sedgewick and Kevin Wayne's *Algorithms*, 4th edition,
[Section 1.4](https://algs4.cs.princeton.edu/14analysis/) and its
[Princeton lecture material](https://algs4.cs.princeton.edu/lectures/keynote/14AnalysisOfAlgorithms.pdf).
It accompanies the [core algorithms chapter](../../notebooks/algorithms.md).
Contributor review remains open; this is not a release record.

The revision keeps the wider scientific, intellectual, programming, social and
commercial motivations but reaches 3-SUM by minute eight. The progression is
deliberate: 3-SUM reveals growth, 1-SUM simplifies counting operations, and
2-SUM compares algorithms and their time–memory trade-off. It restores the new
lecture's two incorrect 2-SUM implementations as prediction questions.

Both core 2-SUM algorithms take **distinct integers**, count pairs of positions
`i < j`, and preserve the input. Repeated values require the separate
frequency-map extension. Time claims for the hash-set version are expected
linear time under average constant-time hashing assumptions.

## Render and build

From the MQB repository root:

```bash
quarto render content/lectures/algorithms/algorithms.qmd --to revealjs
make test
```

The generated `algorithms.html` embeds presentation resources. The local
`algorithms.scss` uses system fonts and the equations use native MathML,
avoiding font and mathematics CDN dependencies. Use a current browser with
MathML support. Press `S` to open speaker view.

The book's `mqb_lectures` extension copies the deck to
`lectures/algorithms/algorithms.html` in the HTML build. This preserves the
chapter-to-deck URL and the deck's relative links to the rendered chapter.
Open the built chapter and deck together when checking navigation; the source
directory itself does not contain the rendered chapter.

Quarto execution is disabled. Separately check the Python examples and run the
completed practical; a successful presentation render does not execute code.

## Prerequisites and practical

Students need functions, loops, basic containers and independently expected
tests. Sets are explained in the lecture. No profiler, notebook, AI account,
external animation or additional Python package is needed.

The [chapter practical](../../notebooks/algorithms.md#practical-predict-test-measure-and-explain)
links a partial script and a measured fallback CSV with metadata. The script
supplies timing, known-answer input construction and writing; students complete
two functions, add a test, predict scaling and interpret the results.
Use a project with `code/`, `data/` and `results/`, running:

```bash
python3 code/algorithms_compare_starter.py
```

Defaults: `n=128,256,512,1024`, one warm-up, five measured calls, median seconds.
Use identical non-mutating inputs for both algorithms. The prepared data are
measurements from one machine, not grading thresholds. The illustrative cubic
table earlier in the lecture is a model, explicitly labelled as such.
Keep reference practical verification in the private solutions repository.

## Timing and optional material

The source has 32 core slides, including break and discussion, and three optional
slides. Their timing metadata totals 120 minutes. This is a proposed delivery
budget, not evidence of an observed full classroom trial.

| Minutes | Focus |
| --- | --- |
| 00–08 | Question, wider motivations and definitions |
| 08–18 | 3-SUM contract, implementation and editable trace |
| 18–30 | Repeated timing, doubling prediction and empirical model |
| 30–42 | 1-SUM count and return to the exact 3-SUM count |
| 42–55 | Theta, Big O, growth classes and doubling ratios |
| 55–65 | Break |
| 65–80 | 2-SUM contract, diagnostic errors and two correct algorithms |
| 80–100 | Fifteen-minute paired practical and five-minute debrief |
| 100–110 | Memory, scientific relevance, HPC and exit question |
| 110–120 | Protected questions and practical recovery |

The full log transformation, repeated-value extension and source slide follow
the discussion slide with zero extra core time. Do not add them on top of a
full two-hour delivery.

## Source versions and graphics

| Source PDF | SHA-256 | Treatment |
| --- | --- | --- |
| Earlier 48-page source used by the first MQB draft | `1640b9cfa450bd006b413bd775c61b25cff5695166022c97032a4e5ade36271c` | Original extraction and page mapping retained for audit. |
| New 61-page source supplied 27 October 2026 | `579ed377b204d66dd9282acf20ac59318d9bc4ff51964c78adaa7f26103f1b99` | Current reference for content and flow revision; recorded separately. |

The [asset record](assets/README.md) distinguishes these versions. The updated
deck uses editable code, equations, tables and a locally constructed trace.
It does not embed any files from `assets/original/`. The old files and masks
remain available for contributor provenance review; their retention does not
establish permission for public reuse.

The original Sedgewick/Wayne attribution and the source/permission questions
tracked in MQB issues [219](https://github.com/MulQuaBio/MQB/issues/219) and
[220](https://github.com/MulQuaBio/MQB/issues/220) remain part of contributor
review. Record any future visual reuse and its source in the manifest.
