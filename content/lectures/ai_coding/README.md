# AI-assisted programming in biology: lecture

The 25-minute lecture that opens the MQB AI-assisted coding workshop, followed
in the same deck by a 10-minute controls tour and warm-up that the students do in
their own Copilot chat view. It accompanies the
[chapter](../../notebooks/ai-assisted-programming.ipynb) and the
[workshop worksheet](../../appendices/ai-coding-workshop.md), and uses the
chapter's terminology, opening example (missing counts at site C), strict versus
inclusive boundary example and practical IDs (R2, A1, A3, N1, E1, C-A, C-B, C-C,
P1; U1 and E4 are cited as afterwards study). The chapter is revised in
parallel: the slides cite practical IDs, not section numbers, so check them
against the chapter if it changes.

## Render

From the MQB repository root:

```bash
quarto render content/lectures/ai_coding/ai_coding.qmd --to revealjs
```

The generated `ai_coding.html` embeds its resources and needs no network. Quarto
leaves trailing whitespace in the embedded CSS and JavaScript; strip it after
rendering (`sed -i -E 's/[ \t]+$//' content/lectures/ai_coding/ai_coding.html`)
so that `git diff --check` passes, as for the algorithms deck. The local
`ai_coding.scss` uses system fonts and adds a few classes: `.ask` for the
question on a slide, `.take` for its takeaway, `.box` for the one diagram and
`.smallest` for the densest slides. There are no CDN requests, images or
mathematics. Press `S` for speaker view. Quarto execution is disabled; the deck
contains no code that is run.

The book's `mqb_lectures` extension is expected to copy the deck to
`lectures/ai_coding/ai_coding.html`, as for the algorithms lecture. Its links to
the chapter, appendix and algorithms resources are relative (`../../notebooks/…`,
`../algorithms/…`) and resolve only in the built book.

## Deck structure and timing

The `data-timing` values (seconds) are per section. Each slide's notes begin with
a clock range within its section (lecture `00:00–25:00`; the tour `Tour
00:00–10:00`).

| Section | Slides | Seconds | Delivered |
| --- | --- | ---: | --- |
| Lecture | 1–22 | 1500 | First 25 minutes |
| Controls tour and warm-up | 23–29 (plus an untimed fallback slide, 30) | 600 | After the readiness check, in the students' own chat view |
| Optional and backup (correct rule, R2 answers, P1 pipeline, Sources) | 31–34 | 0 | Only if asked |
| Exit ticket | 35 | 30 | In the final block of the session, not in the lecture or tour |

Lecture segments:

| Minutes | Slides | Content |
| --- | --- | --- |
| 00–04 | 1–4 | Create first; site C and D example; the plausible wrong answer |
| 04–10 | 5–8 | How an assistant works; training, context and tools; variability; what a passing run shows |
| 10–16 | 9–12 | Bloom's six levels, algorithms link, practical map, plan → implement → test → explain → rerun |
| 16–20 | 13–16 | Where code and data go (four slides): what leaves your computer; processing, retention, review, training; who controls what; check question |
| 20–23 | 17–19 | Goal, attempt, help, check; the same scrutiny for everyone's code; permission, acknowledgement and the assessment boundary |
| 23–25 | 20–22 | Route through the practicals (durations only); three Create tracks; evidence to keep (repeats the assessment boundary and says "we will do the controls tour after the readiness check") |

Controls tour (10 minutes): intro and contract writing (30 s); find the controls
(90 s); Step 1 Ask, Step 2 Plan, Step 3 bounded Agent (120 s each, students
following along); a small diff and a big diff (60 s); VS Code or GitHub.com (60
s).

Session blocks as shown on the route slide, durations only (no clock times, so
that the deck stays reusable; the worksheet carries them): lecture 25, readiness
check 15, controls tour and warm-up 10, R2 10, A1 15, break 10, N1 15, E1 25,
Create 40, reflection, exit ticket and discussion 15 (total 180).

### What changed in the revision, and why

- The lecture shrank from 30 to 25 minutes because the session now has a longer
  Create block and a closing discussion. The four slides on controls and
  surfaces (decision slide, Ask/Plan/Agent demonstration, small and big diffs,
  VS Code versus GitHub.com) moved out of minutes 16–20 into the tour, where the
  students use their own tools rather than watch. The data segment shrank from
  five to four minutes and stays at four slides. Other timings are unchanged.
- The tour example is the A3-style documentation edit on a practice copy of the
  tree-height function (Ask, then Plan, then a bounded Agent edit), so that it
  matches the worksheet. The site C example remains the lecture's thread and the
  E1 practical. The independent check in the tour is 8 m at 45 degrees giving
  8 m, plus invalid input still failing.
- U1 and E4 are no longer on the session route; they are afterwards study. The
  slide on equal scrutiny of human- and AI-written code stays in the lecture and
  points to E4 for later practice.
- The permission slide and the evidence slide state the assessment boundary
  word for word: "Today's practice tools and files are not for your portfolio.
  Do not use them on, or to rewrite, any file you will submit. Assignment 4 has
  its own brief and AI rules; follow it." Nothing more is said about the content
  of the Assignment 4 rules. The notes remind the instructor that the tree-height
  and observations examples use the same biological problems as earlier
  coursework, so students must use the separate practice files and never their own
  TreeHeight or observations scripts.
- A final "Exit ticket" slide carries the three questions used in the worksheet's
  closing block.
- The "if the live demonstration fails" slide is now the untimed fallback slide
  inside the tour section.

Minutes 20–25 and the tour are tight. If the tour runs over, shorten the last
two slides (diffs, GitHub.com) to a sentence each and move on to R2.

## What the lecture does not do

- It states no AI rules for assessed work beyond the boundary statement above.
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

After the revision, with Google Chrome 158 at 1280 × 720 and a Playwright
script: no slide's content extends beyond the frame; every slide has speaker
notes; the lecture totals 1500 s over 22 slides, the tour 600 s and the exit
ticket 30 s; no request to a non-local address when the deck loads. I viewed
screenshots of the changed slides. The repository's `check_content.py` reported
no issues; the full book build was not run.

## Not verified

- The labels and behaviour of the live VS Code Chat view, mode picker, model
  picker and permissions picker on an ICL account.
- Whether ICL students' Copilot is Business/Enterprise or Student, and which model
  choices and data controls their accounts show.
- The tour as students would do it (two minutes per step), and the lecture's
  timing. Neither was rehearsed aloud.
- Links within the built book (chapter, appendix, algorithms lecture and chapter).
- Contrast on the classroom projector, and screen-reader behaviour.

## Morning-of-workshop checks

1. In the VS Code you will present from, confirm the Chat input shows Ask, Agent
   and Plan (or `/plan`), a model picker and a permissions picker. If a label
   differs, say it aloud and keep the slide's idea; update the tour slides
   (24–27) if the difference will confuse people.
2. Check the account you will demonstrate: plan, whether the model list is
   Auto-only, whether Manual permissions is selected, and whether any approvals are
   already saved.
3. Run the tour's three steps once on a practice copy of the tree-height
   function. Keep a screenshot or recording as the fallback.
4. Prepare the dated screenshot or staff-account view for slide 15 (one data
   control, who can change it, what it does not do).
5. Check that nothing you plan to say contradicts the Assignment 4 brief, and
   that the worksheet's wording matches slides 19 and 22.
6. Open the built book's lecture and check the three relative links.
