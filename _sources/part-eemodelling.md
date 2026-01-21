# Ecological & Evolutionary Modelling

This part focuses on building and analysing **mechanistic models** used in ecology and evolution.
Mechanistic models start from assumptions about biological processes (birth, death, competition, predation, infection, resource uptake) and turn them into mathematics and simulations that generate predictions.

You will learn how to move back and forth between:

- biological assumptions → equations
- equations → qualitative predictions (e.g., equilibria, stability, oscillations)
- predictions → data-informed interpretation and critique

## You will learn

- Translate biological assumptions into mathematical models
- Analyse model behaviour (equilibria, stability, interpretation)
- Use simulation to explore model dynamics when algebra is hard
- Connect models to data and biological questions (what would you measure, and why?)

## How to use this part

Most chapters are notebooks: read the narrative, run the code, and then do the embedded exercises.
Try to treat each model as a *hypothesis generator*:

- What assumptions are being made?
- Which parameters matter most for the predicted dynamics?
- What patterns would falsify the model?

```{tip}
If you feel shaky on calculus/algebra, do the [Pre-work exercises](notebooks/mqb-prework-exercises) alongside this part, and dip into the [Maths appendix](appendices/maths) as needed.
```

## Prerequisites

- Comfortable running notebooks and basic code (see [Computing](part-computing) if you need a refresh).
- Helpful: the [Pre-work](notebooks/mqb-prework-exercises) if you want a maths refresher.
- Recommended: basic regression intuition from [Basic Data Analyses and Statistics](part-basic-stats) (to help you think about models vs data).

## Do this first

1. Start with [Metabolic basis](notebooks/metabolic-basis)
2. Then [Populations](notebooks/populations)
3. Then [Interactions](notebooks/interactions)

## Suggested route

A typical sequence through this part is:

- [Metabolic basis](notebooks/metabolic-basis)
- [Populations](notebooks/populations) → practicals → [MiCRM to logistic](notebooks/micrm-to-logistic)
- [Interactions](notebooks/interactions)
- [Competitive dynamics](notebooks/competitive-dynamics) → practicals
- [Predator–prey](notebooks/predator-prey) → practicals
- [Epidemiology](notebooks/epidemiology) → practicals

## Where this goes next

Later, in [Advanced Data Analyses and Statistics](part-advanced-stats), you will fit models to data more formally (e.g., NLLS and MLE). The modelling instincts you build here will make those workflows feel much more meaningful.

## References

The book-wide references live in [References](references).
