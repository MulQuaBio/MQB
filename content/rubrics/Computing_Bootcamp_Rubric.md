# Computing Bootcamp Rubric

## Final assessment of CMEE computing bootcamp

**Note**: This rubric synthesises the [MulQuaBio assessment guidelines](https://mulquabio.github.io/MQB/notebooks/appendix-assessment.html) for the computing bootcamp 

**Group work note**: Some bootcamp weeks include assessed group-work practicals. Group-work criteria (6-7) are assessed only when a group-work repo URL is provided; otherwise group-work evidence is not collected and those criteria are not assessed. In weeks where criteria 6-7 are not assessed, marks are first awarded out of 85 and then linearly rescaled to a final score out of 100 for reporting consistency. For assessed group work, marks are awarded based on both (i) the quality of the group’s submitted solution and (ii) each student’s individual contribution, as evidenced by Git history, documentation, and peer assessment, following MulQuaBio coursework guidelines.

### The Good, The Bad, and The Ugly (reading guide)

This rubric can be read through a practical triad used in feedback:

* **The Good (what you must do consistently well)**: Strong organisation, readability, documentation, version-control practice, and clear learning progression (especially Criteria 1, 3, 4, 5, 9, 10; plus 6-7 for assessed group work).
* **The Bad (errors, missing files, etc - must avoid; usually easy to prevent)**: Functional failures that stop code from running or reproducing outputs (especially Criteria 2 and 8).
* **The Ugly (niggling quality issues that improve with practice)**: Work that may run but is hard to maintain, assess, or trust because structure/documentation/workflow quality is weak (especially Criteria 1, 3, 4, 5, and 6-7 for assessed group work).

Use this as an interpretation aid only; marks are awarded strictly by the formal criteria and descriptors below.

*Summative marking rubric (total = 100 marks)*

> **Missing submissions policy**: Where required code files, scripts, or directories are missing, marks will be deducted according to the rules below, in addition to any criterion-specific deductions. This ensures consistent treatment of incomplete submissions.

| #           | Criterion                                                                                                     | Weight                                                        | What earns **full marks**                                                                                                                                                                     | Typical reasons for lost marks                                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **1**       | **Repository organisation & workflow discipline**                                                             | **15 marks**                                                  | - Correct top-level layout (`code/`, `data/`, **empty** `results/`, optional `sandbox/`) and consistent naming throughout  <br>- No oversized or stray files; sensible use of `.gitignore`.   | • Mixed or missing directories (e.g. results committed) • Large binary files left in repo • `.gitignore` absent or incomplete. |
| **2**       | **Code completeness & functional correctness**                                                                | **25 marks**                                                  | - Every script runs error-free on a clean Linux install and reproduces expected outputs.                                                                                                      | • Runtime errors, missing inputs, hard-wired paths • Scripts that only work on assessor’s machine after fixes.                 |
| **3**       | **Code quality & style** (readability, basic structure, commenting)                                           | **10 marks**                                                  | - Basic functions, meaningful variable names, helpful comments explaining *what* and *why*. <br>- Clear code structure with minimal repetition.                                               | • Meaningless variable names • No comments or excessive copy-paste • Monolithic scripts without structure.                     |
| **4**       | **Documentation** (README + basic usage)                                                                      | **15 marks**                                                  | - Clear weekly READMEs stating script purpose, basic usage, and example commands. Root README summarising bootcamp work.                                                                      | • README missing or lacking usage examples • No explanation of what scripts do.                                                |
| **5**       | **Version-control practice (Git fundamentals; individual repo)**                                               | **15 marks**                                                  | - Regular commits with descriptive messages. <br>- Clean repository without unnecessary files. <br>- Sensible branching for personal work (e.g. topic/feature branches as appropriate).        | • Generic commit messages • Committing generated files • Little or no evidence of Git usage. • Committing large or unnecessary binary files (e.g., outputs, datasets, images). • Only `main` used when branches were expected. |
| **6**       | **Collaborative Git workflow (group work; assessed through group repo)**                                | **7 marks**                                                   | - Assessed only when a group repo URL is provided. <br>- Use of branches for individual tasks. <br>- Merging via pull requests or equivalent with evidence of review or discussion. <br>- Full Git history preserved. | • All work committed directly to `main` • No branches or reviews • Collaboration not evident.                                  |
| **7**       | **Individual contribution & accountability (group work; assessed through group repo)**                  | **8 marks**                                                   | - Assessed only when a group repo URL is provided. <br>- Clear individual contribution evidenced by commit history. <br>- Accurate and complete `CONTRIBUTIONS.md`. <br>- Engagement in coding, testing, documentation, or review. | • Sparse or last-minute commits • Missing or inaccurate `CONTRIBUTIONS.md` • Contributions unclear or overstated.              |
| **8**       | **Basic error-handling & input validation**                                                                   | **8 marks**                                                   | - Scripts handle missing files gracefully; basic input checks; informative error messages.                                                                                                    | • Scripts crash on missing files • No argument checks • Silent failures.                                                       |
| **9**       | **Problem-solving approach & method implementation**                                                          | **7 marks**                                                   | - Demonstrates understanding of the computational problem; appropriate basic algorithms; logical reasoning.                                                                                   | • Copy-paste without understanding • Incorrect algorithms • No evidence of problem comprehension.                              |
| **10**      | **Learning progression demonstration**                                                                        | **5 marks**                                                   | - Clear evidence of skill development across the bootcamp; increasing complexity and integration of workflows.                                                                                 | • No progression visible • Final work similar to early weeks.                                                                  |

---

### Missing submissions & non-runnable code

The following rules apply across **all criteria**:

* **Missing required script or notebook** (referenced in README or expected for the week): *–5 marks per missing file*, capped at the maximum marks for the affected criterion.
* **Script present but non-runnable** (errors on clean Linux run, missing inputs, hard-coded paths): treated as *missing for functional criteria* (Criteria 2 and 8, plus Criterion 9 where method implementation cannot be evidenced).
* **Empty or placeholder files** (e.g. zero-length scripts, commented-out code only): treated as missing submissions.
* **Missing required directories** (`code/`, `data/`, `results/`): up to *–10 marks* under Criterion 1, depending on severity.
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
| < 50   | Insufficient demonstration of foundational computing skills. | Fail |

---

### Group work assessment notes

For bootcamp weeks that include group work:

* Group solution quality contributes to the shared component of the mark.
* Criteria 6-7 are assessed only when a group repo URL is provided; otherwise they are not assessed and group-work evidence is not collected.
* Individual marks may differ within a group based on:

  * Git commit history and branch activity
  * Accuracy and completeness of `CONTRIBUTIONS.md`
  * Participation in reviews, discussions, testing, and documentation
  * Peer assessment (used as supporting evidence)

A strong group submission does not guarantee equal marks for all members.

---

### Bootcamp-specific assessment guidelines

**Week-by-week progression expectations:**

* **Week 1**: Basic file organisation, simple scripts that run successfully
* **Week 2**: Functions, basic error handling, meaningful commit messages
* **Week 3**: Data-processing workflows, documentation habits, input validation
* **Week 4 to final submission**: Integrated analysis workflows, reproducible outputs, clear reporting

**Common considerations:**
Assessment will:

* be lenient on advanced programming concepts not explicitly taught
* prioritise evidence of learning progression over absolute technical perfection
* recognise that an intensive bootcamp involves rapid skill acquisition
* value problem-solving approach even when implementation has minor technical issues
