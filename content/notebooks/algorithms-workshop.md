(algorithms-workshop)=
# Algorithms workshop: choose, test and defend an algorithm

In the [algorithms lecture and chapter](algorithms.md) you saw how the work done by a program grows with its input, and how a different data structure can change that growth. In this workshop you will do the reasoning yourself. You will complete two algorithms for the same problem, try to break your own tests, measure time and memory, and then decide what to use and why.

This workshop uses the **2-SUM** problem from the chapter: given a list of distinct integers, count the pairs of positions $i<j$ whose values sum to zero. You need Python, a text editor or VS Code, and a project folder containing `code/`, `data/` and `results/`. You do not need a notebook, an AI assistant or any package that is not already part of Python.

```{admonition} What you will produce
By the end you will have:

- a script with two completed, tested 2-SUM functions;
- a timing table and a memory table that you have measured yourself;
- a short note explaining what changes when the input is allowed to contain repeated values; and
- a paragraph that justifies your choice of algorithm for a stated situation, using evidence.

This is practice. It is not assessed and it does not change any issued assignment brief. Keep your notes in `results/algorithms_workshop_notes.md` so that you can come back to them.
```

## Plan for the session

| Time | Activity |
| --- | --- |
| 14:00 | Check your setup |
| 14:10 | Short lecture: the ideas you need |
| 14:40 | Part 1: predict and diagnose |
| 14:55 | Part 2: implement and test |
| 15:30 | Break |
| 15:40 | Part 3: measure time |
| 16:05 | Part 4: measure memory |
| 16:25 | Part 5: change the problem |
| 16:45 | Part 6: decide and defend |
| 17:00 | Finish |

Work in pairs if you wish, but each of you should write your own notes. If you fall behind, finish Part 6 before you finish Part 5: choosing an algorithm and explaining why is the aim of the day. The starred tasks are for you if you finish early.

## Check your setup

You are ready when the starter script starts and then stops with a message that you have not yet written the functions. That message is the expected result at this stage.

1. Open a terminal in your project folder and check your Python version:

   ```bash
   python3 --version
   ```

   You need Python 3.9 or later. If your system uses `python` or `py` instead of `python3`, use that name wherever this page says `python3`.
2. Download the {download}`partial Python scaffold <../code/algorithms_compare_starter.py>` and save it as `code/algorithms_compare_starter.py`.
3. From the project folder (not from inside `code/`), run:

   ```bash
   python3 code/algorithms_compare_starter.py
   ```

   You should see `Complete count_two_sum_brute before timing.` and nothing else. If you see a different error, ask for help now.

```{admonition} If you cannot run Python today
Download the {download}`prepared timing table <../data/algorithms_timing_example.csv>` and its {download}`measurement record <../data/algorithms_timing_example_metadata.md>`. You can still do Parts 1, 5 and 6 on paper, and you can use the prepared table for Part 3. Tell a member of staff, and pair with someone whose setup works for Parts 2 and 4.
```

## Part 1: predict and diagnose

Write your answers in your notes **before** you run any code. Wrong predictions are useful: they show you which part of the reasoning to repair.

1. A 3-SUM program tests every triple $i<j<k$. How many times does it test a sum when $n=10$? Use the formula from the chapter, and then say what you expect to happen to the running time when $n$ doubles.
2. A cubic-time program takes 2 seconds for 1000 values. What do you expect for 2000 values? What assumptions are you making?
3. Two plausible 2-SUM versions are wrong:
   - *adjacent only*: compare each value only with the next one; and
   - *every ordered pair*: compare every position $i$ with every position $j$, including $j=i$.

   For each, write down one small list on which it gives a **different** answer from the correct count, and say what the correct answer is. Do not run anything yet.
4. For the correct all-pairs algorithm and the set algorithm, predict the doubling ratio $T(2n)/T(n)$ that you expect to see for large $n$. Then say why you might not see exactly that number on a laptop.

## Part 2: implement and test

Open `code/algorithms_compare_starter.py` and complete `count_two_sum_brute` and `count_two_sum_set`. Use the pseudocode in the chapter's [2-SUM section](algorithms.md#sum-change-the-algorithm). Each function must return one non-negative integer and must not change the list it receives.

1. Complete the two functions, then run the script again. It checks five small cases before it times anything. Both functions should pass.
2. Add **one case of your own** to `check_small_cases` and write a comment saying which mistake it is designed to catch.
3. **Test your tests.** Copy each of the two wrong versions from Part 1 into a temporary function, put it in the `functions` dictionary in `main`, and run the script. Do the existing checks catch both? If one slips through, add a case that catches it. Then remove the wrong versions. A test that cannot fail is not telling you much.
4. Write one sentence for each case in `check_small_cases`: what mistake would it detect?

```{admonition} Stuck?
Trace a small list by hand and write down what each variable holds after every step. For the set version, check which operation comes first: testing whether $-x$ is already in the set, or adding $x$. Swapping them makes `[0]` wrong.
```

## Part 3: measure time

Run the comparison with the default sizes:

```bash
python3 code/algorithms_compare_starter.py
```

Open `results/algorithms_timings.csv`.

1. For each algorithm, look at the `median_seconds` and `doubling_ratio` columns. Do they agree with your Part 1 predictions? Where do they not, and what could explain it?
2. Run the script again, without changing anything. Which numbers moved, and by how much? What does this tell you about how much to trust a single measurement?
3. Extend the series so that the largest size is 8192:

   ```bash
   python3 code/algorithms_compare_starter.py --sizes 128 256 512 1024 2048 4096 8192 --output results/algorithms_timings_large.csv
   ```

   This can take a few seconds or longer on a slow machine; stop it with `Ctrl+C` if it takes more than a minute. Do the ratios become clearer at larger sizes? Why might that be?
4. Use your table to estimate how long the all-pairs function would take for $n=100\,000$. Say which assumption your estimate depends on. Do not run it.

## Part 4: measure memory

The set made the algorithm faster by remembering values. What did that cost? Python's `tracemalloc` module records the memory that a function allocates while it runs. Create `code/algorithms_memory.py`:

```python
import tracemalloc

from algorithms_compare_starter import count_two_sum_brute, count_two_sum_set, make_input


def peak_bytes(function, values):
    """Peak extra memory, in bytes, allocated while function runs."""
    tracemalloc.start()
    function(values)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


print("n,brute_bytes,set_bytes")
for n in [256, 512, 1024, 2048, 4096, 8192]:
    values = make_input(n, seed=1)  # the list already exists, so it is not counted
    print(n, peak_bytes(count_two_sum_brute, values), peak_bytes(count_two_sum_set, values), sep=",")
```

Run it with `python3 code/algorithms_memory.py` and copy the table into your notes.

1. What happens to the all-pairs function's memory as $n$ grows? What happens to the set's? Relate each pattern to the auxiliary space in the chapter's [comparison table](algorithms.md#compare-time-memory-and-practical-suitability).
2. The set's memory does not grow smoothly: it jumps and then stays level. Suggest why a set might allocate memory in steps rather than one value at a time.
3. The snippet measures memory allocated **during** the call. Why does it not include the list that you pass in? When would you need to count that list as well?
4. Estimate the set's memory for $n=10^8$ values. Would that matter on your laptop?

````{admonition} ★ Stretch: a third algorithm
Sort a copy of the list, then use two positions that start at the two ends and move inwards: add 1 to the count and move both when the values sum to zero, move the lower one if the sum is negative, and move the upper one otherwise. Implement it as `count_two_sum_sorted` and add it to your checks. Then answer:

- What is its running time, and what dominates it?
- Does it satisfy the rule that the function must not change its input? What does that rule cost you in memory?
- Measure its time and memory next to the other two. Where would you use it?
````

## Part 5: change the problem

Everything so far assumed that the values are **distinct**. Real data rarely are. Does your set function still answer the same question when a value can occur more than once?

1. Work out by hand how many pairs of positions $i<j$ sum to zero in `[1, 1, -1]` and in `[0, 0, 0]`. Then run the all-pairs function and the set function on both lists. Which function agrees with your hand count, and where do they disagree?
2. Instead of guessing a failing example, search for one. Add this to a scratch script that imports your two functions:

   ```python
   import random

   rng = random.Random(1)
   for _ in range(2000):
       values = [rng.randint(-2, 2) for _ in range(rng.randint(0, 8))]
       if count_two_sum_brute(values) != count_two_sum_set(values):
           print(values, count_two_sum_brute(values), count_two_sum_set(values))
           break
   ```

   Here the slow, easy-to-check function is acting as a trusted reference for the faster one. Why can that be a sensible way to test an optimised algorithm? What does it not tell you?
3. Explain in a sentence why remembering only that a value *has* appeared loses information that the count needs.
4. Write `count_two_sum_repeated`, which uses a dictionary that records **how many times** each value has appeared so far. For each value $x$, add the number of earlier occurrences of $-x$ to the count, and then record $x$. Check it against the all-pairs function on 2000 random lists with repeated values.
5. Has the time or memory comparison changed? Write down which of your Part 3 and Part 4 conclusions still hold, and which now need a qualification.

## Part 6: decide and defend

Use your own tables, not recollections of the lecture.

Choose one situation:

- **A.** You check 5000 pairs of lists, each with about 200 values, once.
- **B.** You process lists of about $10^7$ integers, many times, on a shared server where each job has a small memory allowance.
- **C.** You process a few lists of about $10^5$ values, which may contain repeated values, on your own laptop.

Write about 150 words in your notes stating which algorithm you would use and why. Your answer should use correctness (does it solve the problem you actually have?), time, memory, the expected input size and how easy the code is to understand and maintain. Name one measurement from your tables, and say what additional evidence would change your mind.

## Check your understanding

Answer these in your notes without looking at the chapter. Staff will go through them at the end of the session.

1. What is the difference between an algorithm and its implementation?
2. Why can two programs that give the same answer be very different in the work they do?
3. A measured doubling ratio of 3.6 appeared for a function you expected to be quadratic. Name two explanations that you would check before concluding that the function is not quadratic.
4. In what sense is the set version "faster", and what did it cost?
5. You test an optimised function against a simple one on random inputs and they always agree. What have you shown, and what have you not shown?

## Keep and reuse

Keep your script, `results/algorithms_timings.csv`, your memory table and your notes. They are a worked example of how to compare algorithms using evidence, and the same pattern applies when you compare code that you or an AI assistant has written. Before you accept a faster version of anything, ask whether it solves the same problem, whether you can check it independently, and what it costs.

If an explanation in the chapter or this page was unclear, or something took much longer than the plan suggests, tell us. We will use that to improve the next version.
