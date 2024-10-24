Coursework Assessment 
===================================================

In case your work on any of the TMQB materials is being assessed, here are the guidelines.

## Undergraduates

Assessment will typically be through team-based learning assignments as well as a computer-based test. You will be expected to be able to apply the concepts you have learned to address questions by using appropriate computer code (e.g., R) input and interpreting the output.

## Masters students

Both your practical computing work itself (including any writeups), and whether you are following good programming and workflow
practices will be assessed, usually on a weekly basis. 

The goal of the assessment is to gauge and provide feedback on how well you have learned the principles and implementation of good coding practices and keeping workflows/pipelines/software organised and reusable irrespective of of programming language; In particular (remember the [Zen of Python](https://peps.python.org/pep-0020/)!):

### 1. **Write Clear, Readable Code**
   - **Meaningful variable and function names**: Use names that clearly describe their purpose.
   - **Consistent naming conventions**: Stick to a single style (e.g., [camelCase](https://simple.wikipedia.org/wiki/CamelCase), [snake_case](https://en.wikipedia.org/wiki/Snake_case)).
   - **Commenting and Documentation**: Provide concise comments and document code sections to explain their logic, especially for complex parts.

### 2. **Modular Code**
   - **Single Responsibility Principle (SRP)**: Functions or methods should perform one task.
   - **Reusable functions**: Break down large tasks into smaller, reusable functions.
   - **DRY (Don't Repeat Yourself)**: Avoid duplicating code; encapsulate repetitive logic in functions.

### 3. **Error Handling**
   - **Graceful error handling**: Use `try-except` blocks or other error-handling mechanisms to anticipate failures and handle them without crashing the program.
   - **Meaningful error messages**: Provide messages that help developers understand what went wrong and how to fix it.

### 4. **Testing**
   - **Unit tests**: Write automated tests for individual units of code to ensure they behave as expected.
   - **Test early and often**: Test code during development to catch bugs before they become difficult to track.

### 5. **Version Control**
   - **Use Git or other version control systems**: Commit frequently, with clear commit messages describing the purpose of the changes.
   - **Branching strategies**: Develop new features or bug fixes in separate branches to avoid conflicts in the main branch.

### 6. **Code Optimization**
   - **Efficiency**: Write code that minimizes time and space complexity where possible.
   - **Avoid premature optimization**: Focus first on functionality, then optimize only where performance is actually a bottleneck.

### 7. **Consistent Code Style**
   - **Follow style guides**: Adhere to style guides (e.g., PEP 8 for Python) to keep code consistent.
   - **Code formatters and linters**: Use automated tools to enforce coding standards and detect errors.

### 8. **Code Reviews**
   - **Peer reviews**: Have others review your code to catch issues and get feedback on design and implementation.
   - **Collaborative improvement**: Use feedback to refine the code and learn better practices.

### 9. **Avoid Hardcoding Values**
   - **Use constants or configuration files**: Keep dynamic values and settings outside the code to avoid hardcoding values directly into the program.

### 10. **Refactor Code Regularly**
   - **Refactoring**: Continuously improve code by removing redundancies, simplifying logic, or improving structure without changing functionality.
   - **Code smell detection**: Watch for patterns that indicate poor design, such as overly complex functions or tightly coupled code, and address them.

Adhering to these practices  result in more maintainable, efficient, and scalable code, enhancing collaboration and reducing future technical load.

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

### The Weekly Feedback

Your weekly directories will be checked for how neat and organized they are in a logical workflow, and all the scripts tested, and screened for how well they adhere to the above good coding principles. 

A log file of the results will be pushed to your git repo. This file will contain "points" on a weekly basis to give you and the assessor a quantitative measure of how well you have done in that week. Here is the points scheme for this weekly feedback:

```{note} An *in-class script* is one that is either given to you in class, or which you built from code fragments used in class (typically by re-typing them verbatim) to illustrate one or more good programming concepts, or tools. An *assigned script* is one you have written yourself, either from scratch or by modifying one given to you to complete an assigned practical (always appearing under a "Practicals" subsection of a chapter).
```
* You would get 100 points if,
* All the in-class scripts  were in place (in the code directory in the respective week's directory) and functional when run on the assessor's (Linux) computer.
* All the assigned practicals / problems  were complete and functional, and give the right answers.
* The scripts are all up to the the mark in terms of internal documentation and commenting.
* There is a neat ``readme`` file for the overall repository and in each of the weekly directories.
* For every missing script or assigned practical/problem, 10 pts deducted (including groupwork scripts; see below)
* For every assigned practical/problem, 5 pts deducted for wrong answer if applicable (that is, script runs without error, but gives wrong numerical/text/graphical output).
* For every missing ``readme`` file, 1 pt deducted.
* For every extra, non-script file in ``code`` directory, 0.5 pt deducted.
* For every pre-existing file in the ``results`` directory, 0.5 pt deducted.
* For every *valid* script file in ``code`` directory lacking an appropriate extension file (``*.sh``,\ ``*.py``, etc), 0.5 pt deducted.
* For every in-class script that gives a syntax error, 5 pts deducted, and for every script that gives an error because of wrong path (e.g., absolute) assignment, 2 pts deducted.
* For every Python script *completely* lacking a docstring, 2 pts deducted. For every function in a Python script lacking a docstring, 0.5 pt deducted.
* For every result of a code/script run not saved to a separate results directory, 1 pt deducted. For example, the separate directory may be ``results`` for new results, or ``data``, if the scripts is for generating a new or modified dataset.

### Groupwork

#### Execution

* Each student group will assign a "scribe" to the group who will create a **new Groupwork repository** where all assigned groupwork practicals will be tackled collaboratively.
* The group members will collaborate to develop the solution by creating branches of the script as necessary.
    * The repo's git history will be used to gauge / quantify the relative contributions of group members.
    * Please read about git branching/merging the [Git Chapter](03-Git.ipynb) (including the Readings \& Resources given at the end of th chaptger). Also [see this article](https://www.gitkraken.com/blog/collaborate-on-github).
* Once the group has reached a solution only the main branch should remain.
* The groupwork practicals will will only be evaluated in the final assessment (below).

**Here Are Common Mistakes to avoid with Git Branching and Merging in Team Projects:**

1. **Working Directly on the Main Branch**
   - **Issue**: Making changes directly to the `main` or `master` branch without using feature branches.
   - **Why It's a Problem**: This practice can lead to a cluttered commit history and increases the risk of introducing unstable code into the main codebase, affecting all team members.

2. **Not Pulling Latest Changes Before Starting Work**
   - **Issue**: Forgetting to fetch and merge the latest changes from the remote repository before starting new work.
   - **Why It's a Problem**: Leads to working on outdated code and causes significant merge conflicts when pushing changes later.

3. **Improper Branching Practices**
   - **Issue**: Not creating separate branches for new features or bug fixes, or using inconsistent branch naming conventions.
   - **Why It's a Problem**: Makes it difficult to manage code changes, track progress, and collaborate effectively.

4. **Poor Commit Hygiene**
   - **Issue**: Making large, infrequent commits with vague messages like "Fixed stuff" or "Changes."
   - **Why It's a Problem**: Hinders the ability to trace specific changes, debug issues, and understand the project's evolution.

5. **Not Handling Merge Conflicts Properly**
   - **Issue**: Overwriting code, deleting others' work, or incorrectly resolving conflicts without understanding the implications.
   - **Why It's a Problem**: Can introduce bugs, cause loss of important code, and disrupt the functionality of the application.

6. **Overwriting Team Members' Changes**
   - **Issue**: Using `git push --force` or not merging the latest remote changes before pushing local commits.
   - **Why It's a Problem**: Leads to loss of others' work and creates confusion in the team's codebase.

7. **Ignoring the .gitignore File**
   - **Issue**: Committing unnecessary files like binaries, temporary files, or sensitive information.
   - **Why It's a Problem**: Clutters the repository, increases clone/download times, and poses security risks.

8. **Misusing Git Commands**
   - **Issue**: Incorrectly using commands like `git reset`, `git revert`, or rebasing public branches.
   - **Why It's a Problem**: Can rewrite commit history, cause loss of work, and confuse team members due to unexpected repository states.

9. **Lack of Communication and Coordination**
   - **Issue**: Not informing team members about new branches, changes, or issues encountered.
   - **Why It's a Problem**: Leads to duplicated work, merge conflicts, and a lack of cohesion in development efforts.

10. **Pushing Broken or Untested Code**
    - **Issue**: Committing untested code.
    - **Why It's a Problem**: Disrupts the workflow for others, especially if continuous integration pipelines fail due to the broken code.

11. **Confusion Between Local and Remote Branches**
    - **Issue**: Forgetting to push local branches to the remote repository or misunderstanding the state of branches.
    - **Why It's a Problem**: Causes discrepancies between local and remote repositories, leading to confusion and potential loss of work.

12. **Conflict Between Personal and Team Workflows**
    - **Issue**: Using personal Git configurations or workflows that don't align with the team's agreed-upon practices.
    - **Why It's a Problem**: Creates inconsistency and can cause issues with code integration and collaboration.

13. **Over-Reliance on GUI Tools Without Understanding Git Basics**
    - **Issue**: Using graphical interfaces without grasping the underlying Git commands.
    - **Why It's a Problem**: Limits the ability to troubleshoot issues and understand what's happening behind the scenes, leading to mistakes.

14. **Ignoring Merge Warnings and Errors**
    - **Issue**: Proceeding with merges without addressing warnings or errors.
    - **Why It's a Problem**: Can result in incomplete merges, broken code, and unresolved conflicts that affect the entire team.

15. **Not Keeping Branches Up-to-Date**
    - **Issue**: Failing to regularly merge or rebase the main branch into feature branches.
    - **Why It's a Problem**: Leads to large, complex merge conflicts when it's time to integrate changes back into the main branch.

16. **Mismanaging Merge Strategies**
    - **Issue**: Inappropriately using `git merge` vs. `git rebase` without understanding the consequences.
    - **Why It's a Problem**: Can create a confusing commit history and complicate collaboration efforts.

17. **Deleting Branches Prematurely**
    - **Issue**: Removing branches that others are still using or that contain unmerged changes.
    - **Why It's a Problem**: Causes loss of work and disrupts team members who are relying on those branches.

**Tips to Avoid These Mistakes:**

- **Educate Yourself**: Take time to learn Git fundamentals, including branching, merging, and resolving conflicts.
- **Use Feature Branches**: Create a new branch for each feature or bug fix to isolate your work.
- **Commit Often with Clear Messages**: Make small, incremental commits with descriptive messages.
- **Pull Frequently**: Regularly fetch and merge changes from the remote repository to stay up-to-date.
- **Communicate**: Keep open lines of communication with your team about what you're working on.
- **Test Before Committing**: Ensure your code compiles and passes tests before pushing.
- **Understand Git Commands**: Before using advanced commands like `git reset` or `git rebase`, make sure you understand their effects.
- **Use .gitignore Wisely**: Configure your `.gitignore` file to exclude unnecessary or sensitive files.
- **Review Pull Requests**: Participate in code reviews to catch issues early and share knowledge.
- **Follow Team Conventions**: Adhere to agreed-upon workflows, branch naming conventions, and commit message formats.

#### Assessment

* Every "Groupwork" question/script completed will be assessed using the same criteria as above, but in the final evaluation only. 
* If there are inconsistencies between a groupwork script/solution of a given group, 5 points will be deducted from **each** group member's total.    

## The final assessment of computing coursework

A written summative assessment of your overall performance (with your marks) will be sent at the end of your computing module (e.g., thr CMEE  computing bootcamp; please regfer to your course documentation for specific dates). For this, all the weeks scripts (including the Groupwork scripts) will be run / re-run (and logs and feedback returned). 

Using the points obtained by each student in each week based on the criteria given in the (*The Weekly Feedback* section), the assessor will exercise their judgment to deduct further marks if the weekly directory structure is disorganized, the code inadequately commented or insufficiently documented, the solution is not optimal or correct, or the written components of practicals are not up to the mark.

The weekly log files are to help you spot general, as well as programming language-specific issues with your computing coursework on a regular basis. You may and should fix bugs and other problems that the feedback logs bring to your attention. The assessor will have a look at how much you addressed the issues in the final assessment (by re-running all the weeks' scripts). The final assessment will necessarily be more subjective than the weekly assessments, because the goal is to provide an overall, summative picture of how you did and what you can improve on. You will get feedback if these issues needed to be addressed in the final written assessment. The final marks will be based upon the weekly points and your particular coursework marking criteria (please ask your course / module instructor and administrator for them). 

<!-- The contribution of each week to the overall marks will be up- or down-weighed based upon the difficulty level. -->

## Plagiarism

Students are encouraged to collaborate on these courses (e.g., CMEE). You may often exchange code snippets (solutions to sub-problems within the bigger problem, if you like) or blocks of code to test them. Also, two implementations of a coding solution / algorithm might often be very convergent and relatively similar. However, unless it is a groupwork practical (see above), extremely similar or identical scripts / code files will be reviewed carefully by markers. To this end, the assessment script will perform a diff on pairs of (non-groupwork) code files to detect "inordinate" degrees of similarity.

*Alright, full steam ahead then!*

<!-- You could make a separate directory called ``TestData`` as the default input and reference the main Data file in the ``.gitignore`` file (see the `Git Chapter <03-Git.ipynb>`__) -->
