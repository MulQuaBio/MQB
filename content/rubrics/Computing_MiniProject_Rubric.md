# MiniProject Rubric

**Note**: This rubric is derived from the [MulQuaBio MiniProject appendix](https://mulquabio.github.io/MQB/notebooks/appendix-mini-proj.html).

The MiniProject asks students to answer the biological question *"What mathematical models best fit an empirical dataset, and what biological insight do those models provide?"* in a **fully reproducible way**. Students choose (or are given) an empirical dataset, fit and compare ≥2 alternative models using an NLLS-based implementation workflow (with linear baselines where appropriate), and produce a LaTeX report. The project must be fully reproducible (runnable) end-to-end. MLE/Bayesian/machine-learning approaches are assessed as discussion-level extensions, not required implemented pipelines.

*Summative marking rubric — total = 100 marks (Part A: 50 marks; Part B: 50 marks)*

---

## Part A — Computing & Workflow (50 marks)

| #       | Criterion                                           | Weight     | What earns **full marks**                                                                                                                                                                                                                                                                                     | Typical reasons for lost marks                                                                                                                                                               |
| ------- | --------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Project organisation & README**                   | **10 marks** | - `MiniProject/` directory at the same level as `Week*/` directories. <br>- Expected subdirectories (`code/`, `data/`, `results/`) present and correctly populated. <br>- `results/` is empty in the repo (outputs generated on run). <br>- README states language versions, dependencies, and what each package is for. <br>- Sensible `.gitignore`; no large binary/output files committed. | • Missing or misnamed subdirectories. • `results/` contains committed outputs. • README absent, sparse, or missing required content. • Large data/output files committed without justification. |
| **A2**  | **Single-script reproducibility**                   | **15 marks** | - A single run script (`run_MiniProject.py` or `run_MiniProject.sh`) orchestrates the full pipeline: data preparation → model fitting → plotting → LaTeX compilation. <br>- Script completes without errors on a clean Linux environment. <br>- All expected outputs (PDF report, results CSVs) are produced. | • Run script absent or empty. <br>• Pipeline fails with errors (broken paths, missing packages, unhandled exceptions). <br>• LaTeX compilation step missing or failing. <br>• Environment-specific issues (hard-coded paths, OS-specific calls). |
| **A3**  | **Code quality & style**                            | **10 marks** | - Code is readable: meaningful variable/function names, consistent style (PEP 8 for Python, tidyverse/Google style for R). <br>- Functions used to avoid repetition; scripts modularised by task (e.g. separate data prep, fitting, and plotting scripts). <br>- Helpful inline comments explaining logic; docstrings/headers on functions. <br>- Language choice justified and used appropriately. | • Meaningless variable names or no comments. <br>• Monolithic scripts with excessive copy-paste. <br>• Inconsistent or no code style. <br>• Unjustified or inappropriate language choices.   |
| **A4**  | **Model fitting & statistical analysis**            | **10 marks** | - ≥2 mathematical models fitted using an NLLS-based workflow (with at least one nonlinear/mechanistic model; linear models may be used as baselines where appropriate). <br>- Starting values estimated and documented; convergence failures handled with `try`/`tryCatch`. <br>- Model comparison uses appropriate metrics (AIC, BIC, R², etc.). <br>- Results exported to CSV for downstream analysis and plotting. | • Only trivial linear models fitted (no NLLS-based fitting attempted). <br>• No model comparison metrics computed. <br>• Starting values absent or arbitrary with no justification. <br>• Convergence failures not handled. |
| **A5**  | **Version control & workflow discipline**           | **5 marks**  | - Regular commits throughout development with descriptive messages. <br>- Git history shows iterative, incremental progress (not bulk end-of-project commits). <br>- No unnecessary or generated files committed. | • Generic or absent commit messages. <br>• Single or very few commits (dump of finished work). <br>• Generated outputs or data committed without justification.                              |

---

## Part B — Written Report (50 marks)

The report must be written in LaTeX (`article` class, 11pt, 1.5-spaced, continuous line numbers, ≤3500 words excluding title page, references, and captions). It must include a separate Title page (title, author, affiliation, word count), Abstract, and sections: Introduction, Methods (with a *Computing Tools* sub-section), Results, and Discussion. References must use a non-numeric in-text citation format (e.g. `apalike`) compiled with BibTeX.

**Key Principle**: The narrative must flow coherently from title through discussion, with hypotheses/questions naturally emerging from biological context rather than appearing disconnected. Display items (4–6 figures/tables) should tell most of the story on their own.

| #       | Criterion                                           | Weight     | What earns **full marks**                                                                                                                                                                                                                  | Typical reasons for lost marks                                                                                                                                                  |
| ------- | --------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **B1**  | **Report format & presentation**                    | **10 marks** | - LaTeX `article` class at 11pt, 1.5-spaced with `lineno` continuous line numbers. <br>- Title page present with title, author, affiliation, and word count. <br>- Word count ≤3500 (excluding title page, references, captions). <br>- All figures/tables have informative captions and legends; vector graphics used where possible. <br>- References correctly cited in-text (non-numeric) and formatted via BibTeX. | • Missing or incorrectly configured LaTeX formatting. <br>• No word count or count not tracked. <br>• Figures low-resolution or unlabelled. <br>• Bibliography style numeric or missing. |
| **B2**  | **Introduction & objectives**                       | **10 marks** | - Opens with sufficient biological/ecological context, with citations, that motivates the study topic. <br>- The narrative **funnels logically** from general context to specific focus, so that by the end, stated hypotheses/questions emerge naturally (not abruptly). <br>- Biological question(s) or hypotheses stated clearly and backed by logical/theoretical arguments (if presenting hypotheses, brief explanatory statements help). <br>- Biological objectives clearly distinguished from methodological ones. <br>- The chosen modelling approach is justified as appropriate for the biological question. | • Context too brief, too generic, or disconnected from study focus. <br>• Hypotheses stated without logical build-up or theoretical grounding. <br>• Introduction consists only of methodological aims ("we will fit X models"). <br>• No citations or poorly integrated citations. <br>• Hypotheses appear "out of the blue" rather than emerging naturally from narrative. |
| **B3**  | **Methods (including** ***Computing Tools***)**     | **10 marks** | - Data and its provenance clearly described (source, units, how unique datasets/curves are identified). <br>- Model forms explicitly stated (with equations where relevant); fitting procedures described clearly and reproducibly (starting values/estimation, convergence criteria, comparison metrics). <br>- **Computing Tools sub-section is mandatory**: Explicitly states which languages (bash, Python, R) were used for each task, which packages/libraries were employed, and *justifies why each was chosen* (e.g., "Python/SciPy used for NLLS fitting because..."). <br>- Level of detail appropriate — does not recite code line-by-line, but sufficient for independent reproduction. | • Data provenance or description absent. <br>• Model forms or fitting approach not clearly described or reproduced. <br>• *Computing Tools* sub-section missing, incomplete, or lacks justification for tool choices. <br>• Either vastly over-detailed (reciting code) or too vague to reproduce. |
| **B4**  | **Results & display items**                         | **10 marks** | - Results presented clearly and in the same logical order as the objectives (Introduction→Results alignment). <br>- 4–6 well-designed figures/tables with captions explaining what is shown and conveying take-home messages. <br>- Model fits plotted over data; model comparison summary presented (AIC/BIC table or equivalent). <br>- No discussion of results in this section. | • Results not related back to stated objectives. <br>• Figures absent, poorly designed, or without meaningful captions. <br>• Model comparison not shown, or shown incompletely. <br>• Results section contains discussion or interpretation beyond factual reporting. |
| **B5**  | **Discussion, conclusions & abstract**              | **10 marks** | - Opens by reminding reader of original goals; key findings stated succinctly. <br>- Findings interpreted in biological context with additional citations beyond Introduction; implications discussed in wider scientific context. <br>- **Mandatory**: At least one substantive paragraph engaging with advanced statistical methods (MLE, Bayesian inference, machine learning): clearly explains *what additional biological insight* such methods would provide, *even if not implemented*. This demonstrates understanding of methodological scope. <br>- Caveats and limitations explicitly discussed; specific, concrete future directions suggested (not just "more work needed"). <br>- Concluding take-home messages stated clearly and distinctly. <br>- **Abstract** present (~200 words); self-contained with background, objectives, methods, key results, and main conclusions; specific about findings (not vague). | • Discussion fails to return to original objectives or biological context. <br>• No engagement with advanced methods; only describes work actually done. <br>• Caveats absent or superficial. <br>• Abstract vague or missing concrete findings (e.g., "this study shows model selection is important"). <br>• Conclusion absent or fails to deliver clear take-home message. |

---

## Mark classification

| Total mark | Classification                  |
| ---------- | ------------------------------- |
| 70–100     | **Distinction**                 |
| 60–69      | **Merit**                       |
| 50–59      | **Pass**                        |
| < 50       | **Below Pass threshold**        |

Provisional mark format (for assessor use):

```
Part A (Computing): XX/50
Part B (Report):    XX/50
Total Mark:         XX/100
Classification:     Distinction / Merit / Pass / Below Pass threshold
```

---

## Further guidelines

| Band | Typical profile |
|------|----------------|
| **Strong Distinction (75–90)** | Complete end-to-end reproducible workflow with no errors; NLLS correctly implemented with ≥2 models (including ≥1 mechanistic); appropriate model comparison metrics; well-crafted Introduction with natural narrative funnel to hypotheses; substantive, concrete Discussion engagement with advanced methods as discussion-level extensions (not required implemented pipelines); well-structured LaTeX report showing original synthesis; professional display items (4–6 figures with effective visual communication); clean project organisation; excellent Git history. |
| **Solid Distinction (70–74)** | Complete or near-complete reproducible workflow; NLLS with ≥2 models and appropriate comparison; Introduction logically structured with clear hypotheses; Discussion explicitly engages advanced methods as discussion-level extensions with concrete reasoning; all required sections present with good depth; clear Computing Tools justification; reasonable display items; solid organisation. |
| **Solid Merit (62–69)** | Working workflow (possibly minor issues); ≥2 models fitted with comparison metrics; Introduction covers biological context and hypotheses; Discussion acknowledges advanced methods; adequate report with all sections present; Computing Tools section included; reasonable display items; competent organisation. |
| **Pass (50–61)** | Partially working workflow; some model fitting and comparison attempted; report present with Introduction/Results/Discussion but lacking depth or narrative flow; limited advanced methods engagement; minimal display items; basic organisation; some Computing Tools documentation. |
| **Below Pass (<50)** | Workflow broken or absent; minimal model fitting; report missing, critically incomplete, or incoherent; no advanced methods engagement; poor project organisation; Computing workflow unclear. |

---

## Important Note: Ambition vs. Coherence Trade-off

While extra credit is available for attempting more challenging models (multiple nonlinear/mechanistic models), **choosing overly ambitious projects risks losing marks overall**. Students who spend excessive time on complex model fitting and run out of time to write a coherent, well-structured report with clear narrative flow will score lower than those who tackle a simpler problem well. **Coherence and completeness take priority over model complexity.** Start with a tractable problem (e.g., two linear models), establish a working workflow end-to-end, then iteratively add model complexity.

---

## Missing submissions policy

| Situation | Deduction |
| --------- | --------- |
| `run_MiniProject.*` absent or empty | Treat A2 as 0 |
| `MiniProject/` directory missing or misnamed | Up to −10 marks (A1) |
| LaTeX report absent | All B criteria scored 0 |
| Required report section absent | Up to −3 marks per section (B2–B5) |
| Results committed to repo | −2 marks (A1) |

> Partial credit is always available where effort is clearly demonstrated.
