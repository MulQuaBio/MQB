(ai-coding-workshop)=
# AI-assisted coding workshop: worksheet

This is your guide to the AI-assisted coding workshop on Wednesday 25 November 2026, 14:00–17:00 GMT. A coding assistant can produce an answer that looks right and isn't. In this session you practise deciding what to ask for, what to work out yourself first, and which independent check would tell you the answer is wrong. You will repeat one routine throughout: **plan → implement → test → explain → rerun**.

The worksheet selects a route through the practicals in the {ref}`AI-assisted programming in biology chapter <ai-assisted-programming>` and tells you what to do before, during and after each one. The chapter owns the task contracts, inputs and checks. If this page and a practical card ever differ, follow the card.

```{admonition} This is practice, not assessment
There are no marks. The work you produce is for your own learning and for the closing discussion.

Assignment 4 has its own brief and its own rules on AI. Follow the brief for that work. Use the workshop's practice files only for the workshop.
```

## Before 14:00

Have all of this open and working when the session starts.

1. **VS Code, signed in to the GitHub account that has Copilot access.** If you haven't done this, start with {ref}`the Copilot setup appendix <vscode-copilot-setup>`. Make one harmless request, as in its {ref}`setup check <copilot-setup-check>`, so you know that it works.
2. **Python and R.** In the integrated terminal, `python3 --version` and `Rscript --version` should each print a version. If you normally run Python with `python`, use that name wherever this page says `python3`.
3. **The practice pack.** Download the {download}`workshop practice pack <../data/workshop_ai_inputs.zip>` and keep it where the chapter's workspace-setup cell can find it. The chapter's {ref}`practice-workspace instructions <ai-practicals>` explain where.
4. **An empty scratch folder** containing `code/`, `data/` and `results/`, opened as the project root in VS Code. The chapter's setup cell creates one for you and prints its location. Open that folder if you want to work outside the notebook. Keep your own attempts in files with a `my_` prefix so that a supplied candidate can't overwrite them.
5. **The chapter,** open in a Jupyter-capable editor, or the chapter's scripts open if you prefer to work in the terminal.

```{warning}
Use synthetic or approved data only. The practice pack contains made-up data. Keep passwords, tokens, other people's work, coursework and restricted research data out of your scratch folder and out of every request. Before you send a request, check which files your Copilot chat view has attached to it.
```

## Timetable

All times are GMT.

| Time | Minutes | Block | Chapter practical |
| --- | ---: | --- | --- |
| 14:00–14:30 | 30 | Lecture | {ref}`Why a plausible answer needs checking <ai-plausible>` |
| 14:30–14:45 | 15 | Readiness check | {ref}`Prepare a practice workspace <ai-practicals>` |
| 14:45–14:50 | 5 | Interface warm-up | {ref}`A3 <ai-a3>`, demonstrated |
| 14:50–15:00 | 10 | Remember | {ref}`R2 <ai-r2>` |
| 15:00–15:10 | 10 | Understand | {ref}`U1 <ai-u1>` |
| 15:10–15:25 | 15 | Apply | {ref}`A1 <ai-a1>`, function part |
| 15:25–15:35 | 10 | Break | |
| 15:35–15:50 | 15 | Analyse | {ref}`N1 <ai-n1>` |
| 15:50–16:15 | 25 | Evaluate | {ref}`E1 <ai-e1>` and {ref}`E4 <ai-e4>` |
| 16:15–16:50 | 35 | Create | {ref}`C-A <ai-ca>`, {ref}`C-B <ai-cb>` or {ref}`C-C <ai-cc>` |
| 16:50–17:00 | 10 | Individual explanation and reflection | |
| | **180** | | |

## How to work every block

Each block follows the same pattern, so that the AI never does your thinking for you:

1. **Predict or design first.** Write down what you expect, or how you would solve the problem, before you ask for anything.
2. **Ask for something small.** Say what you want, what you have already tried and how you will check the result. The chapter's {ref}`worked request <ai-request>` shows the pattern: *my goal is… here is my attempt and the relevant specification… I want this specific help… I will check the result by…*
3. **Inspect the response.** Read it before you run it. Reject a suggestion that changes more than you asked for.
4. **Run an independent check.** The check must come from your own prediction, a hand calculation or the specification. It must not come from the assistant telling you that it works.
5. **Write down what you decided and why.**

Start with **Ask** mode and **Auto**, as in the appendix's {ref}`controls check <copilot-controls>`. You don't need an agent for anything in the main route. If you do use one for the Create block, choose Manual permissions and read the proposed edits and commands before you approve them. The chapter's {ref}`decision guide <ai-model-choice>` explains how mode, model and permissions differ. Use your own Copilot chat view, not a screenshot, to find the controls. Labels vary between versions.

If something about your account or Copilot stops working, go straight to the {ref}`route for working without Copilot <no-account-route>`.

## Lecture

Listen for the opening observations example, where a missing count turns into a zero. You will meet the same example again in the Evaluate block. Make a note of any term you can't explain in your own words; you will use the chapter to follow it up afterwards.

## Readiness check

**Goal:** be confident that the live route and the supplied-response route both work, before you rely on either.

- **Do:** run the chapter's workspace-setup cell. It stops with a message if `bash`, `awk` or `Rscript` is missing. Confirm that the account in VS Code is the one with Copilot access, and make one harmless request. Look at the context attached to that request.
- **Stuck?** Ask for help now. Use the route for working without Copilot if the problem doesn't resolve quickly.
- **Write down:** which route you are using (live Copilot, or supplied responses).

## Interface warm-up

**Practical:** {ref}`A3 — Documentation is also code review <ai-a3>`.

**Goal:** learn how to reject a completion, ask about selected code, see what a request includes and review an edit before keeping it. Staff will demonstrate one small documentation edit for the tree-height function. You follow along.

- **Before you ask:** state the function's contract yourself: what its arguments mean, their units, the permitted ranges and what it returns.
- **Check:** the diff should show documentation only. The calculation should behave exactly as before, so rerun the behaviour checks.
- **Write down:** one documentation sentence that you would keep and, if you find one, one that you would reject.

The chapter card contains the Python and R versions and a misleading prepared patch. Work through it after the session.

## Remember

**Practical:** {ref}`R2 — A one-character botanical disagreement <ai-r2>`.

**Goal:** get a short expression recalled correctly, then show that it answers the right question: how many heights are *strictly* greater than 10 cm?

- **Before you ask:** write down the count you expect for 8, 12, 10 and 15 cm. Also predict the results for a single height of exactly 10 cm and for an empty vector. The card also asks about matrix row means, so predict those too.
- **Check:** compare the card's expectations with the result, including the edge cases. Can you say why `>` and `>=` ask different scientific questions? The card is written in R. If you prefer Python, do the same strict count there and compare it with R.
- **Write down:** the expression, its expected result and one sentence on `>` versus `>=`.

## Understand

**Practical:** {ref}`U1 — What is this pipeline actually sorting? <ai-u1>`.

**Goal:** understand a shell pipeline well enough to explain each stage yourself, including what `ls -s` measures on this machine.

- **Before you ask:** predict what the pipeline orders. Then ask for an explanation of one stage at a time, and ask the assistant *not* to rewrite the command yet.
- **Check:** compare the explanation with the output the card produces and with your local `ls` manual page. Allocated disk blocks are not logical file sizes, and the defaults differ between systems.
- **Write down:** a short annotation of each stage, and one assumption that you verified or corrected.

## Apply

**Practical:** {ref}`A1 — Port the tree-height calculation <ai-a1>`. In this session, stop after the function. The whole-file CSV port is for afterwards.

**Goal:** carry a calculation you know in R into Python without changing its units or its input rules.

- **Before you ask:** describe the algorithm in words. State the units and the input rules for yourself, then write your own attempt in a `my_` file.
- **Check:** the card's hand-worked case, which gives a height of 8 m at a distance of 8 m and an angle of 45 degrees, with a small tolerance for floating-point error. Then add a second hand-worked case and at least one invalid input. Two implementations that agree could still share the same mistake.
- **Write down:** your second case and one difference between your attempt and the candidate.

## Break

Ten minutes away from the screen.

## Analyse

**Practical:** {ref}`N1 — Diagnose the actual loop <ai-n1>`.

**Goal:** find out why the loop fails, and see why removing the error would not tell you what the function was meant to calculate.

- **Before you ask:** trace a small positive integer through the loop on paper. When does the denominator reach zero? Run it and look at the traceback, or use the card's debugger option, and compare it with your trace.
- **Check:** ask for an explanation and one diagnostic step. Don't ask for a repair yet. Compare the explanation with your trace.
- **Write down:** the state you predicted, the state you observed and what extra specification you would need before a repair means anything.

## Evaluate

**Practicals:** {ref}`E1 — Catch the plausible observations summary <ai-e1>` and {ref}`E4 — Same specification, same scrutiny <ai-e4>`.

**Goal:** decide whether a candidate meets a written specification, and show that you apply the same standard whoever wrote it.

- **Before you ask:** write your expected results for the ordinary and boundary data before you look at any candidate. What should an entirely missing site report, and how does that differ from an observed zero?
- **Check:** run the same checks against every candidate. Add one hand-derived case of your own. For E4, judge candidates A and B against the specification and decide to accept, revise or reject each one *before* you open the note about where they came from.
- **Write down:** the case that failed or passed, what it means for the biology, and your decision with its reason. Note one assumption that the checks leave untested.

A correct candidate is a valid outcome. The chapter cards are longer than the time here, so do the core checks now and the rest afterwards.

## Create

**Choose one track** with your partner or group: {ref}`C-A <ai-ca>`, {ref}`C-B <ai-cb>` or {ref}`C-C <ai-cc>`. Return to the others later. You are extending a practical you may not have seen before. The task is the extension, not rebuilding the original.

| Track | The question | What you design before asking | A good choice if |
| --- | --- | --- | --- |
| {ref}`C-A — Keep every best sequence alignment <ai-ca>` | How can the alignment search keep *all* equally good alignments, rather than one? | Inputs, allowed offsets, scoring, tie handling and output. | You are comfortable with loops and string matching and want the most self-contained problem. |
| {ref}`C-B — Which survey locations need a second look? <ai-cb>` | Which survey locations have more than half their rows rejected, and why? | The denominator, the threshold, how reasons are counted and how ties are broken. | You like working with tables and summaries. |
| {ref}`C-C — What does this population trace actually support? <ai-cc>` | What does a finite time series support: extinction, approach to equilibrium, oscillation, or no firm conclusion? | An observation window, thresholds, an oscillation criterion and an `indeterminate` outcome. | You know basic population models. If you don't, choose C-A or C-B. |

Work in this order:

1. **Plan.** Write the inputs, outputs, assumptions, ordered steps, edge cases and one worked example. Ask your partner whether the plan answers the question.
2. **Implement.** Ask for a bounded implementation in the track's named practice file, or review the prepared candidate. Read every proposed change and command first. Chat, manual editing and a supplied patch are equally good routes.
3. **Check.** Write one extra boundary or failure case by hand, run the prepared checks and regenerate the track's output from the project root.
4. **Explain.** Without asking the assistant, explain one design decision and one suggestion you accepted or rejected.

The card for your track gives the scoring, the file names and the checks. Keep the card's scaffold and prepared checks as they are. If C-C takes longer than the slot, finish it after the session.

## Individual explanation and reflection

Explain your work in your own words. A partner may ask you questions, but the explanation is yours. Then write three sentences:

1. Where did assistance save you effort while still leaving you able to explain the result?
2. Which check detected, or would have detected, a plausible error that mattered scientifically?
3. What rule will you use when you ask for help on your next project?

**What to keep.** You don't need the whole conversation, or a count of your prompts. In your practice `README.md`, keep:

- your Create plan or pseudocode;
- the commands you ran to reproduce the result from the project root;
- one prompt that was useful;
- the decision you took and the check that supports it, as a short prompt, decision, check table;
- the tool and date. If you already use Git, make a checkpoint commit in your practice folder.

If you used a prepared candidate rather than a live response, say so, and say what you reviewed and tested.

(no-account-route)=
## If you can't use Copilot

Not having working access doesn't stop you doing any of this. Tell a member of staff before the session if you can. Otherwise tell them as soon as you notice, including when you have reached a usage limit.

- Use the prepared candidate or response that comes with each practical card. It has the same specification and the same checks as the live route.
- You still predict, inspect, run the checks, edit and explain. The thinking is yours either way.
- For the warm-up, follow the demonstration and read the prepared patch in the A3 card.
- Work next to someone whose account works if you like, but you don't need to share an account.
- Don't switch to another chatbot to fill the gap. Different services handle your data differently, and {ref}`the chapter's data section <ai-data>` explains why that matters.

## If you finish early or fall behind

**Falling behind.** Keep the prediction or design step and the independent check in every block. Use the prepared candidate instead of waiting for a live response, and skip optional comparisons. In the Create block, a plan and a decision you can explain matter more than a finished implementation.

**Finishing early.** Deepen what you have done before you start something new: add another hand-worked case, break your own check on purpose, or rerun from the project root and compare the results. If you still have time, try another practical at the same level from the chapter's {ref}`practical bank <ai-practicals>`.

**Afterwards.** The other practicals are for you to take at your own pace. Start with the whole-file part of A1 and the full A3 card, since you have already begun them. {ref}`P1 <ai-p1>` is a separate project of 60–90 minutes of study. It is not part of the session. It builds on one of the Create tracks, with C-B as the worked route and transfer routes for C-A and C-C.

## For the closing discussion

Bring:

- your three-sentence reflection;
- one check that caught, or would have caught, an error, and what the error would have done to a biological conclusion;
- one suggestion you rejected or revised, and your reason;
- your Create track, your pseudocode and one thing you would do differently next time;
- the practical you want to try next.

## Where to go next

- The {ref}`AI-assisted programming in biology chapter <ai-assisted-programming>` contains every practical, with preparation notes, prepared responses and checks.
- {ref}`Getting started with GitHub Copilot in VS Code <vscode-copilot-setup>` covers access, sign-in and the controls.
- For coursework, follow the assignment's rules on AI use and acknowledgement. For research, follow the project's rules on data and authorship.
