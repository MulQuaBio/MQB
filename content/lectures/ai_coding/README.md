# AI-assisted programming in biology

Use this deck with the exercises in the [MQB chapter](../../notebooks/ai-assisted-programming.ipynb).
The [workshop worksheet](../../appendices/ai-coding-workshop.md) shows when to
open each exercise in a two-hour session. Count the minutes from when you start.

## Render and rebuild the pack

From the MQB repository root, with Git and the book's Python environment available:

```bash
.venv/bin/python scripts/package_ai_workshop.py
quarto render content/lectures/ai_coding/ai_coding.qmd --to revealjs
sed -i -E 's/[ \t]+$//' content/lectures/ai_coding/ai_coding.html
```

Quarto embeds the diagrams and reveal.js. The book's lecture extension copies
the standalone HTML to its corresponding folder in the built book. Relative
links to the chapter and appendix resolve from that copy. Press **S** for
speaker notes. The shared diagrams and their [source credits](../../images/ai-coding/NOTICE.md)
are under `content/images/ai-coding/`.

## Teaching sequence

| Elapsed minute | Deck heading | Instructor cue |
| --- | --- | --- |
| 0 | Introduction and Remember | Ask where an assistant can help with an analysis, then ask for a prediction before explaining tokens. |
| 10 | Understand | Explain training, cut-offs and context, then compare chat, editor assistance and agents. |
| 25 | Apply | Leave time for a hand check and a short edit. |
| 43 | Break | Take ten minutes. |
| 53 | Analyse | Trace the counts and show the edit to the report. |
| 72 | Evaluate | Ask learners what they would keep or change, and which check helped them decide. |
| 90 | Create | Give learners time to choose what they will estimate before they see a worked design. |
| 110 | Individual transfer | Open the final exercise and give everyone ten minutes to work independently. |

Slide timings are estimates for the explanation or demonstration. The worksheet
gives the full times, including independent attempts and discussion.
The 45-second version-control slide follows the demonstration and points to
the optional Git exercise. Students can complete it in their own time.

## Rehearse the demonstration

1. Extract the pollinator pack into a fresh folder. Open the chapter and the
   deck from the built book. Open the diff and command output in `replay/`.
2. Ask learners to review the one-file plan, name what it may change and
   decide whether to approve a hypothetical request to edit a fixture.
3. Run the independent check in the chapter. Review the diff and verify that
   the changed report exposes observed minutes and preserves the rate.
4. For a live instructor demonstration, rehearse the same task with a
   classroom account and clean folder. Confirm the harness, included context,
   saved approvals and sandbox. Switch to replay if a feature is unavailable
   or the request takes too long.

The replay is a prepared teaching example with local command output. A live
student-account walkthrough, a classroom RStudio check, and a timed learner
pilot require the actual teaching environment.
