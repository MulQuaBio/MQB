# AI-assisted programming in biology: lecture

The 30-minute lecture that opens the MQB AI-assisted coding workshop. It
accompanies the [chapter](../../notebooks/ai-assisted-programming.ipynb) and the
[workshop worksheet](../../appendices/ai-coding-workshop.md), and uses the
chapter's terminology, opening example (missing counts at site C), strict versus
inclusive boundary example and practical IDs (R2, U1, A1, A3, N1, E1, E4, C-A,
C-B, C-C, P1). The chapter is revised in parallel: the slides cite practical IDs,
not section numbers, so check them against the chapter if it changes.

## Render

From the MQB repository root:

```bash
quarto render content/lectures/ai_coding/ai_coding.qmd --to revealjs
```

The generated `ai_coding.html` embeds its resources and needs no network. Quarto
leaves trailing whitespace in the embedded CSS and JavaScript; strip it after
rendering (`sed -i -E 's/[ \t]+$//' content/lectures/ai_coding/ai_coding.html`)
so that `git diff --check` passes, as for the algorithms deck. The
local `ai_coding.scss` uses system fonts and adds a few classes: `.ask` for the
question on a slide, `.take` for its takeaway and `.box` for the one diagram.
There are no CDN requests, images or mathematics. Press `S` for speaker view.
Quarto execution is disabled; the deck contains no code that is run.

The book's `mqb_lectures` extension is expected to copy the deck to
`lectures/ai_coding/ai_coding.html`, as for the algorithms lecture. Its links to
the chapter, appendix and algorithms resources are relative (`../../notebooks/…`,
`../algorithms/…`) and resolve only in the built book.

## Timing

There are 26 core slides, whose `data-timing` values total 1800 s, followed by
five optional slides at 0 s (including Sources). Each slide's notes begin with
its clock range.

| Minutes | Slides | Content |
| --- | --- | --- |
| 00–04 | 1–4 | Create first; site C and D example; the plausible wrong answer |
| 04–10 | 5–8 | How an assistant works; training, context and tools; variability; what a passing run shows |
| 10–16 | 9–12 | Bloom's six levels, algorithms link, practical map, plan → implement → test → explain → rerun |
| 16–20 | 13–16 | Mode/model/effort/context/permissions decision slide; Ask, Plan, Agent demonstration; A3 and P1 diffs; VS Code versus GitHub.com |
| 20–25 | 17–20 | Where code and data go; processing, retention, training; who controls what; check question |
| 25–28 | 21–23 | Goal, attempt, help, check; equal scrutiny; permitted use and acknowledgement |
| 28–30 | 24–26 | Route through the practicals; three Create tracks; evidence to keep |

Minutes 16–20 are tight. If the live demonstration (slide 14) runs over, use the
prepared sequence and keep slides 15 and 16 to a sentence each.

Optional slides (after slide 26, not presented in the 30 minutes): a sketch of a
correct site summary, R2 expected answers, the P1 pipeline, what to do if the live
demonstration fails, and Sources. The worksheet carries clock times; the route
slide gives durations only so that the deck stays reusable.

## What the lecture does not do

- It states no AI rules for assessed work. Assignment 4 is individual and its
  brief sets its own rules; the slide says only that.
- It states no retention, training or hosting facts. It teaches the distinctions
  (processing, retention, review, training; user, institution, provider) and
  points to the chapter's data section and the cited sources.
- It does not reproduce Imperial College London ECRI course material or licence
  text, and carries no adaptation notice. Sources credits the course page only for
  the ordering of ideas actually used (how generative AI works, the Copilot
  interface, then reviewing, editing and writing code). Text and examples are new.

## Verified, and when

Checked on 24 November 2026 by reading the pages below (not by using VS Code).

| Fact used or avoided on the slides | Source |
| --- | --- |
| Copilot harness lists built-in **Ask** (read-only), **Agent** and **Plan**; Plan is invoked with `/plan` | [Agent harnesses](https://code.visualstudio.com/docs/agents/run/agent-harnesses#choose-a-built-in-agent), [Planning](https://code.visualstudio.com/docs/agents/run/planning) |
| Permission levels are **Manual permissions** (default), **Assisted permissions** and **Allow all**; Manual does not mean every command prompts; organisations can restrict levels | [Approvals](https://code.visualstudio.com/docs/agents/run/approvals) |
| Model picker in the chat input; thinking effort under the model's configuration submenu for reasoning models; defaults are recommended and adaptive; higher effort uses more credits; organisation can set an **Org default** model | [Language models](https://code.visualstudio.com/docs/agent-customization/language-models) |
| Picker may offer **Auto** and **Copilot Fusion**, depending on account and policy | [Choose a model](https://code.visualstudio.com/docs/agents/guides/choose-a-model) |
| Copilot Free and Student show "Auto model selection only" | [Copilot plans](https://docs.github.com/en/copilot/get-started/plans) |
| Copilot in VS Code covers suggestions, chat, inline chat, agent work and cloud sessions | [Copilot in IDEs](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-in-ides) |
| GitHub.com: a newer "Copilot in the cloud" experience from 28 October 2026 for paid plans, with Free users on the older chat; sessions can continue across clients | [Copilot on GitHub.com](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github) |
| ICL course syllabus (generative AI, Copilot interface, reviewing, editing, writing code) | [ICL ECRI course page](https://www.imperial.ac.uk/early-career-researcher-institute/learning-and-development/courses-by-programme/research-computing-and-data-science/ai-assisted/) |

`https://code.visualstudio.com/docs/copilot/chat/chat-modes` now redirects to the
custom-agents page, so the old "chat modes" wording is not used. The slides do not
mention legacy Edit mode.

The data sources on the Sources slide (model hosting, Copilot policies, GitHub
privacy statement, the ICL Copilot page) were checked only to return HTTP 200 on
24 November 2026; their contents were not re-read for this deck, which makes no
claims from them.

The Bloom DOI returns 403 to automated requests (publisher blocking) but is the
reference the chapter uses.

## Checked in the rendered deck

On 24 November 2026, with Google Chrome 158 at 1280 × 720 and a Playwright
script: no slide's content extends beyond the frame; every slide has speaker
notes; timings total 1800 s over 26 core slides; no request to a non-local
address when the deck loads. The repository's `check_content.py` and
`check_runtime_paths.py` reported no issues. The full book build and `make test`
were not run.

## Not verified

- The labels and behaviour of the live VS Code Chat view, mode picker, model
  picker and permissions picker on an ICL account.
- Whether ICL students' Copilot is Business/Enterprise or Student, and which model
  choices and data controls their accounts show.
- The live Ask → Plan → Agent demonstration, and its timing. The deck was not
  rehearsed aloud.
- Links within the built book (chapter, appendix, algorithms lecture and chapter).
- Contrast on the classroom projector, and screen-reader behaviour.

## Morning-of-workshop checks

1. In the VS Code you will present from, confirm the Chat input shows Ask, Agent
   and Plan (or `/plan`), a model picker and a permissions picker. If a label
   differs, say it aloud and keep the slide's idea; update slides 13 and 14 if
   the difference will confuse people.
2. Check the account you will demonstrate: plan, whether the model list is
   Auto-only, whether Manual permissions is selected, and whether any approvals are
   already saved.
3. Run the slide 14 sequence once on a practice copy of the E1 candidate. Keep a
   screenshot or recording as the fallback.
4. Prepare the dated screenshot or staff-account view for slide 19 (one data
   control, who can change it, what it does not do).
5. Check that nothing you plan to say contradicts the Assignment 4 brief, and
   that the worksheet's wording matches slide 23.
6. Open the built book's lecture and check the three relative links.
