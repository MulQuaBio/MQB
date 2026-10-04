# Bayesian inference for biological data

```{admonition} Learning goals
By the end of this chapter, you should be able to:

- Explain how prior information and data combine to form a posterior distribution
- Derive and interpret a Beta-Binomial posterior
- Distinguish a credible interval from a frequentist confidence interval
- Use posterior predictions to describe plausible future observations
- Recognise when computational methods such as Markov chain Monte Carlo (MCMC) are needed
```

## From likelihood to posterior

A likelihood describes how compatible observed data are with each possible parameter value. Bayesian inference combines this likelihood with a prior distribution, which represents information about the parameter before these data are observed:

$$
p(\theta \mid y) = \frac{p(y \mid \theta)p(\theta)}{p(y)} \propto p(y \mid \theta)p(\theta).
$$

Here, $p(\theta)$ is the prior, $p(y \mid \theta)$ is the likelihood, and $p(\theta \mid y)$ is the posterior. The evidence $p(y)$ is the normalizing constant that makes the posterior integrate to one. The posterior is conditional on the model, prior, and observed data; it does not remove the need to question those assumptions.

For how the likelihood is constructed and maximized without a prior, see the [maximum-likelihood chapter](mle). Bayesian inference uses that same likelihood but combines it with a prior, producing a distribution over plausible parameter values rather than just the likelihood-maximizing estimate.

## Worked example: a binomial proportion

Suppose 7 of 10 sampled seeds germinate. Let $p$ be the probability that a seed germinates. A binomial likelihood is appropriate if the trials are independent and share the same probability:

$$
X \mid p \sim \operatorname{Binomial}(n,p), \qquad p \sim \operatorname{Beta}(\alpha,\beta).
$$

The Beta prior is conjugate to the binomial likelihood, so the posterior has a simple form:

$$
p \mid X=x \sim \operatorname{Beta}(\alpha+x,\;\beta+n-x).
$$

Use a $\operatorname{Beta}(2,2)$ prior. It is centered at 0.5 and gives less weight to probabilities near 0 or 1 than a uniform prior. With $x=7$ germinated seeds out of $n=10$, the posterior is $\operatorname{Beta}(9,5)$.

```r
successes <- 7
trials <- 10
alpha_prior <- 2
beta_prior <- 2

alpha_posterior <- alpha_prior + successes
beta_posterior <- beta_prior + trials - successes

posterior_mean <- alpha_posterior / (alpha_posterior + beta_posterior)
credible_interval <- qbeta(c(0.025, 0.975), alpha_posterior, beta_posterior)
probability_p_above_half <- 1 - pbeta(0.5, alpha_posterior, beta_posterior)

c(mle = successes / trials,
  posterior_mean = posterior_mean,
  probability_p_above_half = probability_p_above_half)
credible_interval
```

The maximum-likelihood estimate is $7/10=0.70$; the posterior mean is $9/14\approx0.64$. The prior pulls the estimate toward 0.5, with a larger effect when the sample is small or the prior is more concentrated. The 95% credible interval from `qbeta` is an interval containing 95% of the posterior probability for $p$, given this model, prior, and data. It is not a statement about 95% of intervals from repeated samples containing a fixed parameter.

Plot the prior and posterior to see how the data update the distribution:

```r
curve(dbeta(x, alpha_prior, beta_prior), from = 0, to = 1,
      lty = 2, xlab = "Germination probability (p)", ylab = "Density")
curve(dbeta(x, alpha_posterior, beta_posterior), add = TRUE,
      col = "steelblue", lwd = 2)
legend("topright", c("Prior", "Posterior"),
       lty = c(2, 1), col = c("black", "steelblue"), bty = "n")
```

## Predicting future observations

A posterior prediction includes both uncertainty about $p$ and the binomial variability of future observations. Draw parameter values from the posterior, then draw future counts conditional on each value:

```r
set.seed(1)
p_draws <- rbeta(10000, alpha_posterior, beta_posterior)
future_successes <- rbinom(10000, size = trials, prob = p_draws)
quantile(future_successes, c(0.025, 0.5, 0.975))
```

These quantiles summarize plausible counts in a new sample of 10 seeds under the same assumptions. They describe future data, not uncertainty in the parameter itself.

## When computation is needed

Some models have no convenient closed-form posterior. Markov chain Monte Carlo (MCMC) methods then generate dependent draws whose long-run distribution approximates the posterior. Check trace plots for chains that explore the same range without persistent trends, and assess mixing and effective sample size before summarizing draws. Also compare replicated data from the fitted model with the observations; a well-sampled posterior cannot rescue a model that poorly describes the data.

For further biological examples, see the course lectures on [Bayesian probability theory](../lectures/bayesian_inference/BayesianInference_1_ProbabilityTheory.pdf), [MCMC and populations](../lectures/bayesian_inference/BayesianInference_2_MCMC_Populations.pdf), and [hypothesis testing and phylogeny](../lectures/bayesian_inference/BayesianInference_3_HypothesisTesting_Phylogeny.pdf).
