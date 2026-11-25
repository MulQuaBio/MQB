(ai-coding-workshop)=
# AI-assisted coding workshop

Suppose you ask a coding assistant for a few lines of Python. The code runs and gives you a table that looks reasonable. What would you check before using those numbers?

The <a href="../lectures/ai_coding/ai_coding.html">lecture slides</a> explain how coding assistants work and what changes as you give them more to do. The [AI-assisted programming in biology chapter](../notebooks/ai-assisted-programming.ipynb) takes those ideas into a small field survey. In the workshop, you’ll work out a result for yourself, try a suggestion, and decide whether you’d trust the answer.

Set aside two hours, including a ten-minute break. You can work on your own or with a group. Count the minutes from when you start and follow the links in the timetable to the exercises and checks in the chapter. If you’re doing assessed work as part of a course, follow the rules for that assessment.

## Get set up

1. Download the {download}`pollinator practice folder <../data/workshop_ai_pollinators.zip>` and extract it into a separate folder. `task.html` inside it is an optional local copy of the chapter’s exercises; you can follow the chapter instead. Check that `python --version` works in a terminal. Use `python3` or `py -3` if that is how you start Python.
2. Open the practice folder in your editor. Keep coursework, private data and credentials outside it.
3. If you already have Copilot set up, you can use it in the practice folder. Otherwise, use the prepared examples in each exercise and run the same checks. The {ref}`VS Code setup <vscode-copilot-setup>` is available if you want to try Copilot later.

## Timetable

| Elapsed minutes | What to do | What to have at the end |
| --- | --- | --- |
| 0–10 | {ref}`Remember <ai-live-remember>`. Get set up, look at the opening slides and make your prediction before running the starter. | A hand-worked prediction to compare with the output. |
| 10–25 | {ref}`Understand <ai-live-understand>`. Compare two chat replies (Scenario I) and consider the information each needs. | An explanation of why they disagree and a list of what you would share. |
| 25–43 | {ref}`Apply <ai-live-apply>`. Try a chat hint (Scenario I) or an editor completion (Scenario II), then run a check. | Your own check for a zero or unavailable rate. |
| 43–53 | Break | |
| 53–72 | {ref}`Analyse <ai-live-analyse>`. Trace the calculation, then use the demonstration or replay to review an agent’s edit (Scenario III). | A trace or annotated diff and a reason to approve or decline an action. |
| 72–90 | {ref}`Evaluate <ai-live-evaluate>`. Compare candidates and work through a risk scenario. | A decision, the check it rests on and the consequence for the survey. |
| 90–110 | {ref}`Create <ai-live-create>`. Choose a summary and devise a check to distinguish it from the other choice. Then decide what help, if any, you want. | Your question, pseudocode and a hand-worked case. |
| 110–120 | {ref}`Final exercise <ai-live-transfer>`. Spend the final ten minutes working through this exercise on your own. | Your own check, your decision and what the result tells you about the survey. |

## Work through an exercise

Write your prediction or plan before consulting a reply. Read the suggestion or diff, then run the same checks you would use on your own code. Explain which change you would keep and what the output lets you say about the survey. Write your reasoning down or discuss it with a partner. Save your work in the practice folder and leave the supplied data and checks intact.

Start the agent exercise by reading the plan. Which file should change? Which command would you run to check the change? For the prepared example, open the `replay/` folder in the pack and run the command in the Analyse exercise.

## Finish and follow up

Keep your individual answer and a short note of the change you checked. Record how you used assistance, including whether you used a prepared reply or diff. If you want to practise further, try the chapter’s {ref}`self-study practicals <ai-practicals>`.

The workshop adapts CodeRefinery’s lesson under CC BY 4.0. See the chapter’s {ref}`credits and figure sources <ai-references>`.
