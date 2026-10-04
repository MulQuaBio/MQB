# Computing Bootcamp Rubric

## Final assessment of CMEE computing bootcamp

**Note**: This rubric synthesises the [MulQuaBio assessment guidelines](https://mulquabio.github.io/MQB/notebooks/appendix-assessment.html) for the computing bootcamp 

**Rubric version 2026.1.** Submissions 1–3 are formative feedback checkpoints and receive no numeric mark. Submission 4 is the cumulative summative assessment and accounts for 100% of the bootcamp coursework mark.

Criteria 1–5 and 8–10 assess individual work and total 85 points. Criteria 6–7 assess group work and total 15 points; use them only when the released brief specifies an assessed group task and requires a group repository. If group work is not assessed, mark Criteria 6–7 as N/A, not zero, and convert the individual score to a percentage using `individual points / 85 × 100`. If group work is assessed, add the individual and group points for a score out of 100. Compare the unrounded score with the classification thresholds; do not round across a threshold.

### The Good, The Bad, and The Ugly (reading guide)

This rubric can be read through a practical triad used in feedback:

* **The Good (what you must do consistently well)**: Strong organisation, readability, documentation, version-control practice, and clear learning progression (especially Criteria 1, 3, 4, 5, 9, 10; plus 6-7 for assessed group work).
* **The Bad (errors, missing files, etc - must avoid; usually easy to prevent)**: Functional failures that stop code from running or reproducing outputs (especially Criteria 2 and 8).
* **The Ugly (niggling quality issues that improve with practice)**: Work that may run but is hard to maintain, assess, or trust because structure/documentation/workflow quality is weak (especially Criteria 1, 3, 4, 5, and 6-7 for assessed group work).

Use this as an interpretation aid only; marks are awarded strictly by the formal criteria and descriptors below.

*Summative marking rubric (total = 100 marks)*

**Scoring rule:** Apply each rubric criterion once. Do not add a flat missing-file or missing-directory penalty on top of a deduction for the same evidence.

| #           | Criterion                                                                                                     | Weight                                                        | What earns **full marks**                                                                                                                                                                     | Typical reasons for lost marks                                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **1**       | **Repository organisation & workflow discipline**                                                             | **13 marks**                                                  | - One coursework repository with a root `README.md`, `code/` and `data/`; generated `results/` are kept out of commits and created when needed; optional `sandbox/` is ignored <br>- Consistent naming and sensible `.gitignore` use. | • Required files spread across per-week repositories or directories • Generated results committed unnecessarily • `.gitignore` absent or incomplete. |
| **2**       | **Code completeness & functional correctness**                                                                | **21 marks**                                                  | - Required scripts run in the documented environment and produce the specified outputs.                                                                                                      | • Runtime errors, missing inputs, hard-wired paths • Scripts that only work on assessor’s machine after fixes.                 |
| **3**       | **Code quality & style** (readability, basic structure, commenting)                                           | **8 marks**                                                   | - Basic functions, meaningful variable names, helpful comments explaining *what* and *why*. <br>- Clear code structure with minimal repetition.                                               | • Meaningless variable names • No comments or excessive copy-paste • Monolithic scripts without structure.                     |
| **4**       | **Documentation** (README + basic usage)                                                                      | **13 marks**                                                  | - One root README summarising the coursework and giving purpose, usage and test examples for required scripts; update it as submissions extend the same project. | • Root README missing or lacking usage examples • No explanation of what scripts do. |
| **5**       | **Version-control practice (Git fundamentals; individual repo)**                                               | **13 marks**                                                  | - Regular, descriptive commits and a clean repository; sensible branching where appropriate.                                                                                                 | • Generic commit messages • Committing generated files • Little or no evidence of Git usage • Unnecessary binary files.          |
| **6**       | **Collaborative Git workflow (group work; assessed through group repo)**                                | **7 marks**                                                   | - Assessed only when a group repo URL is provided. <br>- Use of branches for individual tasks. <br>- Merging via pull requests or equivalent with evidence of review or discussion. <br>- Full Git history preserved. | • All work committed directly to `main` • No branches or reviews • Collaboration not evident.                                  |
| **7**       | **Individual contribution & accountability (group work; assessed through group repo)**                  | **8 marks**                                                   | - Assessed only when a group repo URL is provided. <br>- Clear individual contribution evidenced by commit history. <br>- Accurate and complete `CONTRIBUTIONS.md`. <br>- Engagement in coding, testing, documentation, or review. | • Sparse or last-minute commits • Missing or inaccurate `CONTRIBUTIONS.md` • Contributions unclear or overstated.              |
| **8**       | **Basic error-handling & input validation**                                                                   | **7 marks**                                                   | - Scripts handle specified missing, invalid, and boundary inputs with informative outcomes.                                                                                                  | • Scripts fail on specified inputs • No basic argument checks • Silent failures.                                               |
| **9**       | **Problem-solving approach & method implementation**                                                          | **6 marks**                                                   | - Demonstrates understanding of the computational problem; appropriate basic algorithms; logical reasoning.                                                                                   | • Copy-paste without understanding • Incorrect algorithms • No evidence of problem comprehension.                              |
| **10**      | **Learning progression demonstration**                                                                        | **4 marks**                                                   | - Shows development between the published formative checkpoints and the cumulative submission, using the recorded submission evidence.                                                       | • No relevant development evidence in the available snapshots • Final work does not address formative feedback.                |

---

### Missing submissions & non-runnable code

The following rules apply across **all criteria**:

* **Missing required script or notebook**: assess the missing evidence under the criterion or criteria that require it; do not apply an additional fixed deduction for the same missing file.
* **Script present but non-runnable**: assess functional correctness under Criterion 2 and relevant validation under Criterion 8. Award partial credit for source-level evidence where the rubric supports it; an execution error alone does not make a present file missing under unrelated criteria.
* **Empty or placeholder files** (e.g. zero-length scripts, commented-out code only): treated as missing submissions.
* **Missing required project structure**: assess it under Criterion 1. Do not deduct marks solely because an empty `results/` directory is absent from Git; assess required outputs when scripts or the assessment runner execute.
* **README references non-existent files or commands**: deductions applied under Documentation (Criterion 4) **and** the relevant technical criterion.

> **Important**: Partial credit may still be awarded where a student clearly attempted the task and provided runnable code for a subset of required components.

---

### Marking scale

| Score  | Overall criteria | Classification |
| ------ | ----------------------- | -----------|
| 80–100 | Outstanding progress; exemplary foundational computing practice for an intensive bootcamp (of typically 4 weeks). | Distinction |
| 70–79  | Strong foundational skills with minor areas for improvement.   | Distinction |
| 60–69  | Competent basic skills with clear areas for development.  | Merit |
| 50–59  | Meets minimum bootcamp standards; several areas need work.   | Pass |
| 0–49   | Insufficient demonstration of foundational computing skills. | Fail |

---

### Group work assessment notes

For bootcamp weeks that include group work:

* Group solution quality contributes to Criterion 6 only when the released brief specifies assessed group work and a group repository is provided.
* Criterion 7 assesses the student's individual contribution in that group repository. If group work is not assessed, Criteria 6–7 are N/A and the individual score is converted from 85 points to a percentage as described above.
* Individual marks may differ within a group based on:

  * Git commit history and branch activity
  * Accuracy and completeness of `CONTRIBUTIONS.md`
  * Participation in reviews, discussions, testing, and documentation
  * Peer assessment (used as supporting evidence)

A strong group submission does not guarantee equal marks for all members.

---

### Bootcamp-specific assessment guidelines

**Progression expectations for the cumulative submission:**

* Compare the published formative submission snapshots with the cumulative submission; use only available, attributable evidence.
* Look for development in computational reasoning, implementation, testing, documentation, and reproducibility across the stated assignment scope.
* Do not infer progression from calendar-week directories, language changes alone, commit counts, or unavailable snapshots.

**Common considerations:**
Assessment will:

* be lenient on advanced programming concepts not explicitly taught
* prioritise evidence of learning progression over absolute technical perfection
* recognise that an intensive bootcamp involves rapid skill acquisition
* value problem-solving approach even when implementation has minor technical issues
