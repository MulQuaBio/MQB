Coursework Assessment 
===================================================

In case your work on any of the TMQB materials is being assessed, here are the guidelines.

## Undergraduates

Assessment will typically be through team-based learning assignments as well as a computer-based test. You will be expected to be able to apply the concepts you have learned to address questions by using appropriate computer code (e.g., R) input and interpreting the output.

## Masters students

Both your practical computing work itself (including any writeups), and whether you are following good programming and workflow practices will be assessed, usually on a weekly basis. 

The goal of the assessment is to gauge and provide feedback on how well you have learned the principles and implementation of **keeping workflows/pipelines/software organised and reusable** and **good coding practices**, *irrespective of programming language* (please refer back to the start of the [UNIX](./01-Unix.ipynb) and [Python](./05-Python_I.ipynb) chapters in particular).

```{note}
Lowercase for directory names below is a suggestion - just be consistent with whatever you choose, such as [CamelCase](https://en.wikipedia.org/wiki/Camel_case); for example, you may choose to name your `code` directory, `Code` instead. 
```

The basic rules you must follow, irrespective of a Week or project's content are:

* All code/scripts go to a ``code`` directory
* All data go to a ``data`` directory
* All results go to ``results`` directory. The results directory should be empty when you submit your week's work, as it will be populated automatically when the assessment script runs.
* If you have files that don't fit in these categories, put them additional, meaningfully named directories. For example, you can create a ``sandbox`` directory to hold your experimental work (and perhaps [`.gitignore`](./03-Git.ipynb) it).
* No single file should be greater than 100 mb, either data or script/code. If a script needs a data file, but the example data file is >100 mb, reduce it to a minimum working dataset and upload that, keeping the main data file(s) under `.gitignore`. Keep all your  data backed up elsewhere, of course!
* Most importantly, all scripts should run without errors, taking in data and spitting out the results as necessary.

When necessary, more specific, module-specific details on weekly coursework and assessment will be given when relevant.

### Pre-submission practicals wrap-up

Do this as after you finish with an assignment, and at the end of every week / module, before submission :

* Review and make sure you can run all the commands, code fragments, and named scripts you have built till then and get the expected    outputs.
* Review your code files and annotate/comment code lines as much and as often as necessary using ``#``.
* Check that all code, data and results files organized as instructed above in you weekly directory.
* `git add`, `commit` and `push` your work after every major change to your weekly work, and make a final push by the given deadline.

```{note} An *in-class script* is one that is either given to you in class, or which you built from code fragments used in class (typically by re-typing them verbatim) to illustrate one or more good programming concepts, or tools. An *assigned script* is one you have written yourself, either from scratch or by modifying one given to you to complete an assigned practical (always appearing under a "Practicals" subsection of a chapter).
```

### The weekly code tests and feedback

Your weekly directories will be checked for how neat and organized they are in a logical workflow, and all the scripts tested & screened for how well they adhere to good project structure and coding principles; in particular: 

* That all in-class and assigned scripts are in the appropriate `code` directory. 
* All code/script files are functional (no errors, correct output) when run on the assessor's (Linux) computer.
* The scripts are all up to the the mark in terms of internal documentation (e.g., docstrings in the case of Python) and commenting.
* There is a good ``readme`` file for the overall repository and in each of the weekly directories.
* The ``results`` directory is empty (no pre-existing results).
* All *valid* script files in ``code`` directory have an appropriate extension (``*.sh``,\ ``*.py``, etc).
* All results of a code/script run are saved to a separate `results` directory.

### Groupwork

* Each student group will assign a "scribe" to the group who will create a **new Groupwork repository** where all assigned groupwork practicals will be tackled collaboratively.
* The group members will collaborate to develop the solution by creating branches of the script as necessary.
    * The repo's git history will be used to gauge / quantify the relative contributions of group members.
* Once the group has reached a solution only the main branch should remain.
* The groupwork practicals will will only be evaluated in the final assessment (below).

```{note}
Please read about git branching and merging during teamwork in the [Git Chapter](03-Git.ipynb), including the "**Common Mistakes to avoid...**" listed there. Please also check the Readings \& Resources at the end of the chapter.
```
#### Assessment

* Every "Groupwork" question/script completed will be assessed using the same criteria as above, but in the final evaluation only. 

## The final assessment of computing coursework

A written summative assessment of your overall performance (with your marks) will be sent at the end of your computing module (e.g., thr CMEE  computing bootcamp; please regfer to your course documentation for specific dates). For this, all the weeks scripts (including the Groupwork scripts) will be run / re-run (and logs and feedback returned). 

Using the weekly testing results, the assessor will exercise their judgment to deduct further marks if the weekly directory structure is disorganized, the code inadequately commented or insufficiently documented, the solution is not optimal or correct, or the written components of practicals are not up to the mark  (see *The Weekly Feedback* section).

The weekly log files are to help you spot general, as well as programming language-specific issues with your computing coursework on a regular basis. You may and should fix bugs and other problems that the feedback logs bring to your attention. The assessor will have a look at how much you addressed the issues in the final assessment (by re-running all the weeks' scripts). The final assessment will necessarily be more subjective than the weekly assessments, because the goal is to provide an overall, summative picture of how you did and what you can improve on. You will get feedback if these issues needed to be addressed in the final written assessment. The final marks will be based upon your particular coursework marking criteria (please ask your course / module instructor and administrator for them). 

<!-- The contribution of each week to the overall marks will be up- or down-weighed based upon the difficulty level. -->

## Plagiarism

Students are encouraged to collaborate on these courses (e.g., CMEE). You may often exchange code snippets (solutions to sub-problems within the bigger problem, if you like) or blocks of code to test them. Also, two implementations of a coding solution / algorithm might often be very convergent and relatively similar. However, unless it is a groupwork practical (see above), extremely similar or identical scripts / code files will be reviewed carefully by markers. To this end, the assessment script will perform a diff on pairs of (non-groupwork) code files to detect "inordinate" degrees of similarity.

*Alright, full steam ahead then!*

<!-- You could make a separate directory called ``TestData`` as the default input and reference the main Data file in the ``.gitignore`` file (see the `Git Chapter <03-Git.ipynb>`__) -->
