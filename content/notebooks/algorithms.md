# Algorithms: solving problems with computation

Suppose you have written a program to analyse some biological data. It gives
the answer you expect for eight observations. What happens when you give it
eight million? Before leaving it running overnight, you need to understand
how much work you have asked the computer to do.

This is where algorithms become useful. An **algorithm** is a precise procedure
for solving a specified problem: the idea that your code implements. Two
programs can give the same correct answer while doing very different amounts
of work. Sometimes a different procedure removes calculations that appeared
unavoidable, making a previously impractical scientific question feasible.

We will develop this reasoning through three related examples. We start with
**3-SUM** to see how running time changes as the input grows. We then use the
simpler **1-SUM** to learn how to count operations, before turning to **2-SUM**
to compare two algorithms and their use of time and memory. The examples draw
on Stanislav (Stanley) Modrak's *Analysis of algorithms* lecture and Sedgewick
and Wayne's *Algorithms*, especially Section 1.4
{cite}`SedgewickWayne2011Algorithms,SedgewickWayneSection14`.

```{admonition} Learning goals and prerequisites
By the end, you should be able to state a computational problem precisely,
check a proposed solution, and explain how its work changes with input size.
You should also be able to interpret timing measurements and justify a choice
between algorithms using correctness, clarity, time and memory.

You will use functions, loops and basic containers from [Python](python.ipynb)
or [R](r.ipynb), together with small examples whose answers you have worked out
by hand. Sets are introduced below. The practical needs Python and its standard
library; you can run it as a script without a notebook or profiling tool.
```

## Why study algorithms?

Why spend time on algorithms when you could be learning more Python or R?
There are several good reasons:

- **To solve otherwise inaccessible problems.** Changing how you formulate a
  calculation can make it feasible even when faster hardware would not.
- **To become a proficient programmer.** Thinking about the procedure makes you
  ask what needs to be calculated, stored and repeated before writing the code.
- **For intellectual stimulation.** There is considerable satisfaction in
  discovering that a seemingly complicated task has a much simpler solution.
- **For their broad impact.** Algorithms shape transport, communication,
  medicine, public services and everyday life online.
- **To investigate life and the universe.** Comparing sequences, analysing
  images and interpreting telescope signals all require computational ideas.
- **For profit.** Search, routing and recommendation algorithms have considerable
  commercial value. Commercial success does not establish scientific validity.

We will concentrate on performance here, but keep the scientific purpose in
view. The aim is to choose a procedure that answers your question reliably
with the data and computing resources you actually have.

## Specify the problem before writing the program

| Term | Meaning |
| --- | --- |
| Problem | The question, including inputs, required output and assumptions. |
| Algorithm | A precise procedure for solving that problem. |
| Data structure | A way to organise information and support useful operations. |
| Implementation | The algorithm expressed in a language and computing environment. |

These distinctions help us see what we are changing. You might implement the
same algorithm in Python and R, or use a different algorithm in the same
language. You might also organise the data differently: lists, vectors, sets
and dictionaries support different operations, and that can change the
procedure available to you.

Before comparing speed, work out the answer to a small example by hand. If two
implementations agree, that is useful evidence, but they could share a mistake.
An independently expected answer gives you something to test them against.
Testing checks the answer; timing measures a particular run; algorithm analysis
explains how the required work grows. Together, they help you make a reasoned
choice.

## 3-SUM: make growth visible

### What exactly are we counting?

Given a list of **distinct integers**, count triples of positions $(i,j,k)$
such that $i<j<k$ and $x_i+x_j+x_k=0$. Return one non-negative integer. Inputs
with fewer than three elements return zero. Here $n$ means the number of input
integers.

Try the list `[30, -40, -20, -10, 40, 0, 10, 5]` by hand. It contains
**four** qualifying triples:

| Positions, starting at zero | Values | Sum |
| --- | --- | --- |
| (0, 1, 6) | 30, -40, 10 | 0 |
| (0, 2, 3) | 30, -20, -10 | 0 |
| (1, 4, 5) | -40, 40, 0 | 0 |
| (3, 5, 6) | -10, 0, 10 | 0 |

The most direct approach is to examine every allowed triple:

```text
count = 0
for i from 0 to n - 3:
    for j from i + 1 to n - 2:
        for k from j + 1 to n - 1:
            if x[i] + x[j] + x[k] equals zero:
                increase count by 1
return count
```

Before running any code, trace the loops for a list of four elements. You
should reach `(0,1,2)`, `(0,1,3)`, `(0,2,3)` and `(1,2,3)`. Notice what
the increasing indices achieve: each group is examined once, and no element
can appear twice in the same triple. A loop with an empty range simply performs
no iterations.

The <a href="../lectures/algorithms/algorithms.html">lecture</a> gives the Python
implementation. Its [optional external
animation](https://smith558.github.io/cmee-algorithms/) can help visualise the
loops; the trace above provides a starting point without the website.

### Measure equivalent work

How should we time this? The result will depend on the input, implementation,
hardware and whatever else the machine is doing. We can make the comparison
more useful by giving both algorithms the same input and checking their answers
first. Construct or read that input before starting the clock, and print the
result after stopping it. Otherwise, you are also measuring work that you did
not intend to compare.

For a deterministic function that leaves its argument unchanged:

```python
from statistics import median
from time import perf_counter

def elapsed_seconds(function, values, repetitions=5):
    function(values)  # untimed warm-up
    times = []
    for _ in range(repetitions):
        start = perf_counter()
        function(values)
        times.append(perf_counter() - start)
    return median(times)
```

Make one untimed call to warm up, then time at least five calls and take the
median. Record the runtime version, machine, how you constructed the input,
its size and the number of repetitions. This gives someone else enough
information to interpret your measurements.

The median reduces the influence of an occasional slow run, although systematic
effects remain. Also check whether a function changes its input. If it does,
you will need fresh equivalent inputs for repeated calls, prepared consistently
so that you are still comparing the same work.

### Predict what happens when input doubles

Now suppose doubling $n$ makes the program take roughly eight times as long.
What kind of growth would explain that observation? Consider the ratio:

$$
\frac{(2n)^3}{n^3}=8.
$$

Our observation is consistent with cubic growth, suggesting the empirical
model $T(n)\approx an^3$, with $T$ measured in seconds. We can check how well
that model describes the measured sizes. To explain *why* the algorithm behaves
this way, we will also need to examine the code.

More generally, $T(n)\approx an^b$ can describe polynomial scaling over a
useful range. Other patterns, such as $n\log n$ or exponential growth, need
different descriptions. The actual input can change how much work occurs,
while caches, memory limits and implementation choices affect the pattern we
measure. A faster machine may shorten the run without changing how many
triples the algorithm examines.

## Explain the work with a cost model

The timings suggest a pattern. To explain it, we need to connect elapsed time
with what the program actually does.

In principle, we could account for the frequency and cost of every operation.
That soon becomes tedious. Instead, we choose an operation that represents
the main repeated work and count how often it occurs. This simplification is
our **cost model**.

### 1-SUM: start with an easy count

Let us put 3-SUM aside briefly and count zeroes instead. This simpler problem,
sometimes called 1-SUM, lets us see how an operation count works without getting
lost in nested loops:

```text
count = 0
for each value x in the input:
    if x equals zero:
        increase count by 1
return count
```

Choose comparison with zero as the operation to count. How many comparisons
will a list of $n$ values require? Exactly $n$: every value is checked once,
whether none, some or all of the values are zero. The number of increments
changes with the data, but the overall work remains linear under this model.

Here we treat operations on our small integers as taking constant time. Keep
that assumption in mind if you later work with arbitrarily large Python
integers, whose arithmetic costs can grow with their size.

### Return to 3-SUM

We can now apply the same reasoning to 3-SUM. Count how often the innermost
sum test is reached. Since each group of three positions is examined once,
the number of tests is

$$
\binom{n}{3}
=\frac{n(n-1)(n-2)}{6}
=\frac{n^3}{6}-\frac{n^2}{2}+\frac{n}{3}.
$$

Check the expression against our small examples. At $n=4$, it gives the four
candidate triples we traced. At $n=8$, it gives 56 candidates, even though only
four match in our example. Finding four answers does not mean that we performed
only four tests!

As $n$ grows, the cubic term dominates. The ratio of test counts when $n$
doubles therefore approaches eight, although it can be quite different for
small inputs. We now have a mathematical explanation for the timing pattern,
as well as an empirical observation.

## Describe orders of growth

### Big Theta and Big O

Writing $T(n)\in\Theta(g(n))$ means that, for sufficiently large $n$, $T(n)$
is bounded above and below by positive constant multiples of $g(n)$. This is a
**tight asymptotic growth class**.

For example, $4n^3+2n^2+16$ is in $\Theta(n^3)$. Keeping the dominant term
and setting aside its coefficient identifies the growth class. To predict a
runtime in seconds, we would still need information about the implementation
and machine.

Big O supplies an asymptotic **upper bound**. Linear work is both $O(n)$ and
$O(n^2)$, but only the first is tight. Use Theta when claiming a tight growth
class, and say whether the claim concerns expected or worst-case behaviour.

Why set those terms aside if they affect the answer? We are asking how work
grows when inputs become large. For the sizes you actually use, constants and
smaller terms may still determine which implementation is faster. This is
why mathematical analysis and measurement belong together.

### Common growth classes

| Growth class | Example under a suitable cost model | Multiplier $T(2n)/T(n)$ for the named function |
| --- | --- | --- |
| $\Theta(1)$ | Index one list element | 1 |
| $\Theta(\log n)$ | Binary search in a sorted array, worst case | $\log(2n)/\log n$, approaching 1 |
| $\Theta(n)$ | Count zeroes | 2 |
| $\Theta(n\log n)$ | Mergesort | $2\log(2n)/\log n$, approaching 2 |
| $\Theta(n^2)$ | Check all pairs | 4 |
| $\Theta(n^3)$ | Check all triples | 8 |
| $\Theta(2^n)$ | Enumerate all subsets with constant work per subset | $2^n$ |

The ratios apply to the displayed functions; measured times include other
costs. When $T(n)=2^n$, doubling the input gives $T(2n)=2^{2n}$ and a
multiplier $2^n$. It does not merely double the time.

Resist the temptation to assign a power of $n$ simply by counting nested loops.
A loop that halves its remaining work behaves differently from one that visits
every element. Follow the iterations and count the important operation.

### Optional: why a log–log plot can be useful

If $T(n)\approx an^b$, taking logarithms gives

$$
\log T(n)\approx\log a+b\log n.
$$

If the model fits, plotting $\log T$ against $\log n$ gives an approximately
straight line with slope $b$. Use the same logarithm base throughout: an
intercept $c$ gives $a=2^c$ in base two, or $a=e^c$ with natural logs. Use
positive, unrounded timings, and examine how well the model fits. A line can
look convincing over a short range even when it will not describe larger inputs.

Another notation you may encounter is $f(n)\sim g(n)$, meaning
$f(n)/g(n)\to1$. Thus $\binom n3\sim n^3/6$: unlike Theta, this approximation
retains the leading coefficient.

## 2-SUM: change the algorithm

So far, we have explained the growth of a given procedure. Can we change the
procedure itself to do less work? We will use 2-SUM to compare two algorithms
for the **same problem**, and see how a different data structure helps.

### State the problem for both algorithms

Given a list of **distinct integers**, count index pairs $(i,j)$ with $i<j$
and $x_i+x_j=0$. Return one non-negative integer; fewer than two elements
give zero. There can be at most one zero, which cannot pair with itself.
Neither implementation should modify the input.

For `[3, -3, 5, 8, -8]`, the answer is two: positions `(0,1)` and `(3,4)`.
Both timed functions assume that you supply distinct integers; they do not
check this condition themselves. We will consider repeated values separately.

### First, diagnose two plausible mistakes

Before looking at a correct solution, try to catch a mistake. Predict what each
of these approaches would return:

1. Check only adjacent elements. Would that find the pair in `[-2, 5, 2]`?
2. Check every ordered pair, including `i == j`. What happens for `[-3, 3]`,
   or for `[0]`?

The first returns zero instead of one because the matching values are separated.
The second counts both orders of a pair and allows a position to pair with
itself. A test is useful here because you can explain exactly which mistake it
would detect.

### Compare every pair

```text
count = 0
for each position i:
    for each later position j:
        if x[i] + x[j] equals zero:
            increase count by 1
return count
```

The sum test occurs $n(n-1)/2$ times, giving $\Theta(n^2)$ running time
under our unit-cost model. The only things kept in addition to the input are
indices and counters. Their storage does not grow with the list length, so the
**auxiliary space** is $\Theta(1)$.

### Remember earlier values in a set

For each value $x$, we are looking for $-x$. Do we really need to revisit
every earlier value to find it? A set records which values are present, allowing
us to test directly whether the complement has already appeared:

```text
seen = empty set
count = 0
for each value x:
    if -x is in seen:
        increase count by 1
    add x to seen
return count
```

Trace `[3, -3, 5]` and watch what the set remembers. We first add 3.
When -3 arrives, its complement 3 is already there, so the count becomes one.
When 5 arrives, -5 is absent. Each qualifying pair is counted when we reach its
second member. The order of operations matters: checking before adding prevents
a zero from pairing with itself.

Assuming average constant-time hash lookup and insertion, the expected runtime
is $\Theta(n)$. This describes expected behaviour rather than an unconditional
worst-case guarantee. We have also stored information to avoid searching again:
the set can hold $n$ values, giving $\Theta(n)$ auxiliary space.

### Optional extension: allow repeated values

What changes if the problem permits repeated values but still counts pairs of
positions? For `[1, -1, -1]` the answer is two; for `[0, 0, 0]` it is three.
A set remembers whether a value appeared, but forgets how often it appeared.

Use a frequency map instead:

```text
frequency = empty map, with missing keys interpreted as zero
count = 0
for each value x:
    add frequency[-x] to count
    increase frequency[x] by 1
return count
```

For three zeroes, successive additions to the count are 0, 1 and 2. Trace these
updates and check why the current position never pairs with itself. Allowing
repeated values has broadened the problem, so a comparison must account for
that change in assumptions.

## Compare time, memory and practical suitability

| Algorithm, distinct inputs | Running time under the stated model | Auxiliary space |
| --- | --- | --- |
| Check every pair | $\Theta(n^2)$ | $\Theta(1)$ |
| Remember values in a hash set | Expected $\Theta(n)$ | $\Theta(n)$ |

The set has saved time by storing information. To judge that trade-off, be clear
about what you are counting as memory. Auxiliary space excludes the input:
both algorithms still need the supplied list, whose storage grows with $n$.
Peak total memory also includes the language runtime and any inputs or outputs
held at the same time. Creating a generator, copy or large array outside the
timed region does not remove its memory cost.

Which would you choose? For a small list processed once, the simple pair loop
may be quite sufficient. For large repeated calculations, avoiding those
comparisons may justify the set's extra memory. Use the expected input sizes,
measurements and need for clear, maintainable code to explain your decision.
A shorter or vectorised expression still needs the same scrutiny: inspect
how much work it does.

## Practical: predict, test, measure and explain

Work in pairs if convenient, with a project containing `code/`, `data/` and
`results/`. Download the {download}`partial Python scaffold
<../code/algorithms_compare_starter.py>` to `code/algorithms_compare_starter.py`.
The starter script handles input construction, timing and CSV writing so that
you can concentrate on the algorithm comparison. Complete its two marked
functions using the procedures above. If you need help with the Python syntax,
consult the lecture implementations and trace what each line does.

1. Before running the functions, predict their growth classes and what should
   happen to the time when input size doubles.
2. Work out small expected answers independently. Include an empty input, a zero
   and a separated pair; add one case of your own and explain what it checks.
3. Complete the functions and run the shared checks before timing anything.
4. Run from the project root:

   ```bash
   python3 code/algorithms_compare_starter.py
   ```

5. Inspect `results/algorithms_timings.csv`. Compare median seconds and doubling
   ratios across sizes, then explain whether they support your predictions.
6. Explain the extra memory used by the set and one circumstance in which you
   would choose the simpler loop.

For each size, the starter constructs a shuffled list of all nonzero integers
from $-m$ to $m$. It therefore contains $n=2m$ distinct values and exactly $m$
qualifying pairs. Work out why: every positive value has exactly one negative
partner. This gives us an expected answer independently of either counting
function. Both receive the same list, with construction, checking and CSV
writing outside the timer.

Start with the default sizes, 128, 256, 512 and 1024, and five measured runs
after an untimed warm-up. Establish what happens at these sizes before trying
larger ones; the brute-force calculation can soon take a long time. The output
records Python/platform details, the seed, repetition count and timing method.
Add useful hardware details to your notes.

If you cannot run the comparison, use the {download}`prepared example table
<../data/algorithms_timing_example.csv>` and its
{download}`measurement record <../data/algorithms_timing_example_metadata.md>`.
These measurements describe one machine. Use them to examine the ratios and
compare the algorithms, rather than as target speeds for your computer. You
can still make predictions, explain the checks and reason about memory.

Keep the script, timing table and a short explanation of your choice. If the
measurements surprise you, investigate: are you seeing noise, a mistake, a
change in the problem, or a change in the amount of work? Explain what evidence
supports your interpretation.

## Algorithms can change what science is feasible

Now return to the biological motivation. Genome-assembly methods organise
relationships between sequence fragments using graphs. Ecological null models
and simulations can sometimes update only the quantities affected by a change,
rather than recalculating the whole system. In each case, how we organise the
calculation can remove repeated or unnecessary work.

To make a complexity claim for one of these examples, we would need to specify
the stage being analysed, how the input is represented and what output is
required. A whole field cannot be assigned one linear or quadratic growth rate.

There is a wider responsibility here too. An algorithm embodies choices about
objectives, data and acceptable errors. What is being optimised? Which
observations are missing? How would you detect a plausible but wrong answer,
and who would bear the consequences? Speed alone cannot answer those questions.

### Parallelism and HPC

Once you have a suitable algorithm, can more computing resources help?
**Parallelism** means performing independent work at the same time.
**High-performance computing (HPC)** provides larger or specialised resources,
including many CPU cores, GPUs and high-memory nodes.

Independent simulations may parallelise well. A calculation in which each
stage needs the previous result is harder to divide up, and coordinating work
or moving data also takes time. Think about these dependencies before expecting
more processors to shorten a run. A better algorithm and suitable hardware
can both contribute.

For implementation details, consult [Python profiling](python.ipynb#the-need-for-speed-profiling-code),
[R vectorisation](r.ipynb#vectorization), and
[Performance, Scaling, and Compute](../appendices/performance.md).
Vectorisation, parallel execution and a change in algorithm are different
choices; none automatically supplies the others.

## Return to the opening question

Will your procedure give the intended answer and handle the intended input?
You now have several ways to investigate: state the problem precisely, work
through small cases, count the repeated operations and measure comparable runs.
Use that evidence to explain your choice of algorithm, including its memory
cost and how clearly somebody else could understand it.

If a colleague or AI tool suggests an improvement, you can ask the same
questions of it. The important skill is being able to reason about the
calculation and its result.

Before moving on, explain:

- Why can 3-SUM return four matches after examining 56 candidate triples?
- Why does a lower runtime on one input not establish a better growth class?
- Why does the set solve our distinct-input 2-SUM problem, and what changes
  when repeated values count as different positions?
- What extra information would you need before recommending parallel hardware?

The <a href="../lectures/algorithms/algorithms.html">companion lecture</a> follows the same
route with Python implementations and prediction questions. It is an MQB
adaptation of Stanley Modrak's lecture, itself adapted from Sedgewick and Wayne.
