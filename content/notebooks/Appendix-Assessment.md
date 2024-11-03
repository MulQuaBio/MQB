# TMQB Coursework Assessment

Here are the guidelines for assessment of any coursework based on the TMQB materials.

Assessment may be through computer-based tests, or individual or group/team-based practicals.

In computer-based tests, you will be expected to be able to apply the concepts and techniques you have learned to address the questions by using appropriate computer code input and interpreting the output.

## Assessment of Practicals

Both, the correctness and quality of your practical work / solutions, and whether you are following good programming & workflow practices will be assessed: how well you have learned the principles and implementation of **keeping workflows/pipelines/software organised and reusable** and **good coding practices**, _irrespective of programming language_ (please refer back to the start of the [UNIX](01-Unix.html) and [Python](#./05-Python_I.ipynb) chapters in particular).

```{Note}
Lowercase for directory names below is a suggestion - just be consistent with whatever you choose, such as [CamelCase](https://en.wikipedia.org/wiki/Camel_case); for example, you may choose to name your `code` directory, `Code` instead.
```

The basic rules you must follow, irrespective of a Week or project's content are:

* All code/scripts go to a `code` directory
    
* All data go to a `data` directory
    
* All results go to `results` directory. The results directory should be empty when you submit your week's work, as it will be populated automatically when the assessment script runs.
    
* If you have files that don't fit in these categories, put them additional, meaningfully named directories. For example, you can create a `sandbox` directory to hold your experimental work (and perhaps [`.gitignore`](03-Git.html) it).
    
* No single file should be greater than 100 mb, either data or script/code. If a script needs a data file, but the example data file is >100 mb, reduce it to a minimum working dataset and upload that, keeping the main data file(s) under `.gitignore`. Keep all your data backed up elsewhere, of course!
    
* Most importantly, all scripts should run without errors, taking in data and spitting out the results as necessary.
    
When necessary, more specific, module-specific details on weekly coursework and assessment will be given when relevant.

### Pre-submission practicals wrap-up

Do this as after you finish with an assignment, and before submission:

* Review and make sure you can run all the commands, code fragments, and named scripts you have built till then and get the expected outputs.
    
* Review your code files and annotate/comment code lines as much and as often as necessary using `#`.
    
* Check that all code, data and results files organized as instructed above in you weekly directory.
    
* `git add`, `commit` and `push` your work after every major change to your weekly work, and make a final push by the given deadline.
    

```{Note}
An _in-class script_ is one that is either given to you in class, or which you built from code fragments used in class (typically by re-typing them verbatim) to illustrate one or more good programming concepts, or tools. An _assigned script_ is one you have written yourself, either from scratch or by modifying one given to you to complete an assigned practical (always appearing under a "Practicals" subsection of a chapter).
```

### Code testing and feedback

Your project (e.g., weekly) directories will be checked for how neat and organized they are in a logical workflow, and all the scripts tested & screened for how well they adhere to good project structure and coding principles; in particular that:

* All in-class and assigned scripts are in the appropriate `code` directory.
    
* All code/script files are functional (no errors, correct output) when run on the assessor's (Linux) computer.
    
* The scripts are all up to the the mark in terms of internal documentation (e.g., docstrings in the case of Python) and commenting.
    
* There is a good `readme` file for the overall repository and in each of the weekly directories.
    
* The `results` directory is empty (no pre-existing results).
    
* All _valid_ script files in `code` directory have an appropriate extension (`*.sh`,\\ `*.py`, etc).
    
* All results of a code/script run are saved to a separate `results` directory.
    

### Groupwork execution

* Each student group will assign a "scribe" to the group who will create a **new Groupwork repository** where all assigned groupwork practicals will be tackled collaboratively.
    
* The group members will collaborate to develop the solution by creating branches of the script as necessary.
    
    * The repo's git history will be used to gauge / quantify the relative contributions of group members.
        
* Once the group has reached a solution only the main branch should remain.
    
* The groupwork practicals will will only be evaluated in the final assessment (below).
    

```{Note}
Please read about git branching and merging during teamwork in the [Git Chapter](03-Git.html), including the "**Common Mistakes to avoid…**" listed there. Please also check the Readings & Resources at the end of the chapter.
```

#### Groupwork assessment

Every "Groupwork" question / script completed will be assessed using the same criteria as above.

### Final assessment of computing coursework

A written summative assessment of your overall performance will be sent at the end of your computing module or course (e.g., the CMEE computing bootcamp; please refer to your course documentation for specific dates). For this, all the weeks scripts (including the Groupwork scripts) will be run / re-run (and logs and feedback returned).

Using the testing results, the assessor will exercise their judgment to deduct marks if the weekly directory structure is disorganized, the code inadequately commented or insufficiently documented, the solution is not optimal or correct, or the written components of practicals are not up to the mark (see _The Weekly Feedback_ section).

The weekly log files are provided to help you spot general, as well as programming language-specific issues with your computing coursework. You may and should fix bugs and other problems that the feedback logs bring to your attention. The assessor will have a look at how much you addressed the issues in the final assessment (by re-running all the weeks' scripts). The final assessment will necessarily be more subjective than the weekly assessments, because the goal is to provide an overall, summative picture of how you did and what you can improve on. You will get feedback if these issues needed to be addressed in the final written assessment. The final marks will be based upon your particular coursework marking criteria (please ask your course / module instructor and administrator for them).

## Plagiarism

Students are encouraged to collaborate for learning, including on the practicals. You may often exchange code snippets (solutions to sub-problems within the bigger problem, if you like) or blocks of code to test them. Also, two implementations of a coding solution / algorithm might often be very convergent and relatively similar. However, unless it is a groupwork practical (see above), extremely similar or identical scripts / code files will be reviewed carefully by assessors. To this end, the assessment script will perform a diff on pairs of (non-groupwork) code files to detect "inordinate" degrees of similarity.

### Appropriate usage of AI for coding

Artificial Intelligence (AI) tools such as ChatGPT have become valuable resources for learning and coding assistance. However, it's important to use them responsibly to enhance your learning experience without violating academic integrity and undermining your actual learning.

Here are some guidelines to help you make appropriate use of AI in your coding journey.

1. **Use AI as a Learning Aid, Not a Crutch**

Leverage AI to understand concepts and get unstuck, but avoid relying on it to do the work for you.

*Example:* If you're struggling to understand how a recursive function (recall the [Python Chapter](05-Python.html)) works, you might ask an AI tool to explain the concept or provide a simple example. Use this information to deepen your understanding and then attempt to write your own recursive function.

2. **Understand and Verify AI-Generated Code**

Always read and comprehend any code provided by AI to ensure you understand how it works.

*Example:* Suppose an AI tool suggests a solution for sorting a list. Before using it, go through each line of code to understand the sorting algorithm implemented. Try to explain it in your own words or comment the code to reinforce your understanding.

3. **Avoid Plagiarism and Uphold Academic Integrity**

Do not submit AI-generated code as your own in assignments or projects where external assistance is not permitted.

*Example:* If your assignment requires you to implement a function without outside help, avoid copying code from an AI tool. Instead, use the AI to clarify concepts if allowed, but write the code independently to ensure it reflects your understanding.

4. **Follow Your Institution's Policies on AI Usage**

Be aware of and comply with your institution, school or university's rules regarding AI assistance.

*Example:* If your course syllabus states that using AI tools is prohibited for homework assignments, refrain from using them. Violating these policies can lead to serious academic consequences.

5. **Use AI to Enhance Problem-Solving Skills**

Employ AI to practice coding challenges and improve your skills, not just to get answers.

*Example:* When practicing coding problems, you might attempt a problem on your own first. If you get stuck, use the AI to get hints or alternative approaches, then try solving the problem again without directly copying the solution.

6. **Cite AI Assistance When Required**

Acknowledge the use of AI tools in your work if your academic or professional guidelines require it.

*Example:* In a project report, you might include a section like: "Portions of the code were developed with the assistance of AI tools such as ChatGPT." Alternatively, add comments in your code where AI assistance was used.

7. **Develop Independent Coding Skills**

Strive to solve coding problems on your own to build confidence and proficiency.

*Example:* Before consulting AI, spend time brainstorming and coding your solution. Use AI only after you've made a genuine effort, which helps reinforce learning and retention.

8. **Be Aware of AI's Limitations**

Recognize that AI tools can sometimes provide incorrect or suboptimal solutions.

*Example:* If an AI suggests a piece of code, test it thoroughly. Suppose the AI provides a function that doesn't handle edge cases properly; identifying and correcting this strengthens your debugging skills.

9. **Protect Sensitive Information**

Do not input confidential or personal data into AI tools.

*Example:* If you're working on a project with proprietary code or sensitive data, avoid sharing that code with an AI tool. Instead, abstract the problem or create a simplified version that doesn't disclose sensitive information.

10. **Collaborate Ethically in Team Projects**

Ensure all team members agree on the use of AI tools and properly attribute any AI-generated contributions.

*Example:* In a group project, discuss with your team whether to use AI assistance. If you collectively decide to use it, make sure to document where and how it was used, following any required citation practices.

11. **Avoid Overreliance on AI**

Balance the use of AI with traditional learning resources like textbooks, lectures, and discussions with peers or instructors.

*Example:* If you are learning a new programming language, use official documentation and tutorials as your primary resources. Supplement your learning with AI explanations when needed, but don't let it replace foundational learning methods.

12. **Contribute to the Learning Community**

Share your insights and understanding gained from AI assistance with classmates, fostering a collaborative learning environment.

*Example:* If an AI tool helped you grasp a difficult concept, consider explaining it to study group members or participating in class discussions to help others benefit from your newfound understanding.

By following these guidelines, you can make the most of AI tools to enhance your coding skills while maintaining academic integrity and personal growth. Remember, the goal of using AI in coding is to support your learning journey, *not* to replace the valuable process of learning through practice and problem-solving.

---
*Alright, full steam ahead then!*