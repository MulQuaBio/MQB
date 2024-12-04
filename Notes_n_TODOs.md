# ** TMQB Notes and TODOs**

**Date:** October 9, 2024  
**Time:** 2:03 PM  

**Attendees:**  
- Samraat Pawar
- James Rosindell  
- Bhavin Khatri  
- Ruben Perez-Carrasco  
- Tin-Yu Jonathan Hui  
- Francis Windram  

---

**Purpose:** Organize teaching and assessments for the second term of the Living Planet Masters Programme - CMEE stream.

1. **Key Topics:**
   - Changes in curriculum and assessments for 2024-25
   - Centralized teaching materials and use of GitHub for coursework
   - Discussion on module structures, assessment, and mini-project design
   - Collaboration and integration of high-performance computing (HPC) and data science teaching materials

### Discussion Points:

1. **Course Changes and Teaching Approach:**  
   - Focus on centralized teaching materials for computational fundamentals, modeling, and data science.
   - Usage of GitHub as the main platform for materials; Blackboard for administrative purposes only.
   - Transition from exams to coursework-based assessment through a **mini project**.

2. **Assessment Strategy:**  
   - ECTS credits for each module are clearly defined. High-performance computing (HPC), ecological and evolutionary theory, Bayesian, and machine learning modules to be assessed via a single mini project.
   - Mini project replaces exams and will test the cumulative knowledge across all topics.
   - Discussion around balancing complexity, auto-marking systems, and maintaining student engagement with the mini project.
  
3. **Student Engagement:**  
   - Concerns raised about low student engagement. Strategies discussed for increasing engagement, including potential pass/fail assessment components for coursework.
   - Importance of formative feedback throughout modules before the summative mini project.
  
4. **Mini Project Structure:**  
   - The mini project will cover data science, HPC, and modeling.
   - Possible inclusion of biological data, mathematical models (e.g., competition models), and likelihood-based inference as project options.
   - Concerns about project feasibility within the 3-week timeline.
  
5. **Collaboration on Teaching Materials:**  
   - Development of teaching materials in Jupyter Notebooks and LaTeX.
   - Contributions to centralized GitHub repositories discussed, including materials for HPC and Bayesian analysis.
   - Project-specific contributions by attendees, particularly around ecological modeling and Bayesian computation.

---

### Decisions Made:
- **Mini Project** will serve as the only summative assessment for Term 2 modules, replacing exams.
- **GitHub** will be the primary platform for teaching materials and assessments, supplemented by Blackboard for final submissions and student communication.
- Formative assessments will be used during teaching weeks to ensure students are progressing, especially given the removal of formal exams.

---

### Action Items / TODOs:
1. **Samraat**  
   - Finalize the structure and design of the mini project with input from module leads by January.
   - Coordinate GitHub repository access for teaching materials.
   - Set up meetings to develop the **Ecological and Evolutionary Theory** module with Yan, Bhavin and Vincent.
   - Organize a focused meeting on mini project integration of HPC materials with James (Done).

2. **Ruben**  
   - Integrate Bayesian and likelihood materials into the centralized repository.
   - Propose a project structure based on cell competition data for the mini project.

3. **Austin + Bhavin + Tin-Yu**
   - Collaborate on the evolutionary theory segment for the mini project and teaching materials.
   - Consider ABC projects for possible inclusion in the mini project.

4. **James Rosindell**  
   - Assist with HPC content integration into the mini project and GitHub repository.
   - Ensure HPC materials are compatible with both R and Python formats for students.

5. **Francis**  
   - Develop auto-marking scripts for assessing the mini project.
   - Provide feedback on how to streamline the assessment workflow using automated feedback systems.

6. **Tin-Yu**  
   - Align the malaria data used in teaching with the centralized materials.
   - Address data creation and privacy concerns for project examples.

---

#### **Date and Time:**  
- September 23, 2024, 1:03 PM

#### **Attendees:**  
- **Pawar Samraat**  
- **Nelson Rhodri B**

#### **Key Discussion Points:**

1. **Overview of Automated Assessment Framework:**
   - Rhodri demonstrated the assessment framework using **GitHub Classroom**.
   - Assignments are distributed via GitHub, creating repositories for students.
   - Tests and sample solutions are organized in specific folders for the AI assistant to analyze.
   - The framework supports both student assessments and internal testing of solutions.

2. **Automated Feedback Generation:**
   - Nelson showed how the framework uses **LLM (Large Language Models)** to generate feedback for student submissions.
   - The system processes student code, test outputs, and assignment specifications to produce detailed feedback in markdown format.
   - The goal is to provide feedback beyond error codes, addressing code quality and optimization.

3. **GitHub Actions for Automation:**
   - GitHub Actions are used to automate the process of fetching student repositories, running tests, and generating feedback.
   - Pawar raised questions about the role of AI in the feedback process and how it integrates with the automated system.

4. **Documentation and Setup:**
   - Pawar asked if there was documentation or a minimum working example to follow.
   - Nelson acknowledged the lack of formal documentation and offered to provide guidance on setup and adjustments.

5. **Next Steps for Pawar’s Implementation:**
   - Pawar plans to implement both automated assessment and chatbot functionalities.
   - He will integrate shell scripts, Python, and R into his GitHub Classroom for a three-week boot camp.
   - There will be a focus on creating documentation on his end, aiming to run automated assessments within two weeks.

6. **Long-Term Vision:**
   - Nelson discussed plans to scale the project to other departments and potentially involve teams from **Mechanical Engineering (MeckEng)**, **EEE**, and **Medicine**.
   - Nelson will meet with stakeholders in November to present progress and results.

7. **Collaboration Opportunities:**
   - Pawar has added 2-3 more people to his team, including a GTA and postdoc, who may reach out with questions.
   - Nelson is open to collaboration, particularly on making the system more user-friendly and generalized.

#### **Decisions Made:**
- **Automated feedback generation** using LLM will be integrated into both Nelson’s and Pawar’s frameworks.
- Pawar will start testing the system with shell scripts in his GitHub Classroom, followed by Python and R.
- Further documentation will be created by Pawar for his team’s use.

#### **Action Items:**

1. **Pawar Samraat:**
   - Implement the GitHub Classroom framework for the boot camp (first week: shell scripts, second week: Python, third week: R).
   - Prepare documentation to explain the setup to his team (GTA and postdoc).
   - Reach out to Nelson for help with GitHub Actions if necessary.
   - Begin automated assessments within two weeks.

2. **Nelson Rhodri B:**
   - Provide guidance to Pawar and his team on setting up the framework.
   - Plan a meeting in November with potential stakeholders in **Medicine** and other departments.
   - Consider tweaking the "generate feedback" script and GitHub Actions based on testing needs.

3. **Both:**
   - Collaborate on developing a more generalized and user-friendly version of the framework, possibly extending it to other departments.


Here are the structured meeting notes and action items based on the transcript provided.

---

**Meeting Notes**  
**Date**: September 23, 2024  
**Time**: 1:32 PM  
**Attendees**:  
- Yang Wenxia  
- Pawar Samraat  
- Windram Francis A  
- Modrak Stanislav

### Key Discussion Points:
1. **Overview of the Chatbot Project** (Yang Wenxia):
   - The chatbot is developed to support computational thinking skills, allowing students to interact with course materials.
   - It allows uploading materials, including lectures, which can be used to generate responses.

2. **Implementation and Features of the Chatbot**:
   - Basic functions include login/logout and interaction with pre-loaded lectures.
   - It uses OpenAI's GPT-4 for generating answers, incorporating the uploaded lecture materials.
   - Students can upload small documents to interact with them through the chatbot.
   - Implementation involves FastAPI for request handling and LangChain for orchestrating responses.

3. **Deployment and Future Plans**:
   - Yang is deploying the chatbot locally on a server; students access it through the local network.
   - The team is considering cloud deployment for better scalability.
   - Deployment instructions will be shared with Pawar for integration into his course starting next week.

4. **Next Steps for Integration into Teaching** (Pawar Samraat):
   - Pawar is preparing to integrate the chatbot with Jupyter notebooks for his course.
   - 25 students are expected to use the chatbot starting next week.
   - Pawar seeks detailed deployment instructions and support for implementing the chatbot.

5. **Skepticism and Concerns** (Francis Windram):
   - Francis expressed some skepticism about the chatbot’s capabilities and raised concerns about its effectiveness.

6. **Automated Assessment**:
   - Automated assessments were discussed but are not yet integrated into the chatbot. This is planned for future work based on Rodri's framework.

### Action Items (TODOs):
1. **Yang Wenxia**:
   - Share deployment documentation and shell scripts for deploying the chatbot on a cloud/server by **Thursday, September 26, 2024**.
   - Integrate Pawar's Jupyter notebooks and materials into the chatbot and create a new GitHub repository for them.
   - Provide user account setup for the 25 students by **Thursday, September 26, 2024**.

2. **Pawar Samraat**:
   - Provide the list of student usernames to Yang by **Thursday, September 26, 2024**.
   - Update course materials and share with Yang for chatbot integration.
   - Prepare a guide for students to access the chatbot by **Monday, September 30, 2024**.

3. **Francis and Stanley**:
   - Review the chatbot implementation and provide feedback on its potential for improving student engagement.

======================================================

# TODOS

### General

* Include a Glossary as an appendix to reduce repetition across chapters/languages (e.g., oop, data structure, function, module, etc)

* For deployment of the notebooks online: https://tljh.jupyter.org/en/latest/install/azure.html (<100 students); Jupyterhub on Kubernetes scales better: https://zero-to-jupyterhub.readthedocs.io/en/latest/microsoft/step-zero-azure.html (from Florian J Song, Chemistry)

* Outline coding principles in a general way right at the start of the Intro or Unix chapter
    * Explain steps in the way to writing a program: outline steps/agorithm, write pseudocode, write functions, etc  

* Assessments - create
  * e.g, Course material is put into the desired repo, we create student github teams and then give them access to the appropriate repos. They then clone this to get the material.
  * For real time comms we use Teams / slack etc with channels for groups  / modules / etc    

### The Miniproject

* Make clear where the "rule of thumb" of a difference of 2 in AIC/AICc comes from. It is indeed a bit fuzzy. We will use a simple rule of thumb for the purposes of the miniproject. Students should be aware that the rule of thumb of 2 is a (somewhat) conservative way to pick models using AIC, but they should acknowledge its limitations. 

This is a useful post: https://stats.stackexchange.com/questions/349883/what-is-the-logic-behind-rule-of-thumb-for-meaningful-differences-in-aic

* Restrict usage of packages, by showing students how to keep things simpler.

### NLLS: 

  * Explain what some of the common NLLS fitting error messages (like singular gradient matrix) mean, with examples.
  * Illustrate approaches for getting starting values and the difference between sampling start values vs and bounding parameters.
  * Show graphical illustrations of how NLLS parameter searching works and what local minima mean intuitively. 

### Unix

* Explain what colors of items returned by ls mean (directory/file type and permissions): https://unix.stackexchange.com/questions/94498/what-causes-this-green-background-in-ls-output (green background means all users have w permission on that directory (and its contents)) - explain the implications of this in words.

* grep -r -n -w -l '.' -e 'ecology and evolution*'
 
    -r or -R is recursive, -n gives  line number where the pattern occurs, -w makes sure that the whole pattern is matched, and -l gives just the name of files containing the pattern.

    Along with these, --exclude, --include, --exclude-dir flags can be used for fine tuning the search. For example, 

    This will only search through those files which have .pdf or .txt extensions:

    grep --include=\*.{pdf,txt} -r -n -w -l '.' -e 'Ecology*'

    You can also exclude one or more directories using the `--exclude-dir` parameter. For example, to exclude `dir1` or `dir2` :

    grep --exclude-dir={dir1,dir2} -rnwl '/path/to/somewhere/' -e "pattern"

* makefiles


### Git 
* git chapter to be updated with most common/useful scenarios
* https://gist.github.com/digitaljhelms/4287848
* https://www.red-gate.com/simple-talk/sysadmin/devops/git-anatomy/ 
* To add to the chapter: Please `git fetch` and then `git merge`, or if you are brave (or "pullhardy" (ha!)) `git pull`  directly. See this blog:  https://longair.net/blog/2009/04/16/git-fetch-and-merge/​​​​​​​

### Python

* https://johnsbutler.netlify.app/talk/primaryschooltalk2019/
* https://towardsdatascience.com/6-simple-tips-for-prettier-and-customised-plots-in-seaborn-python-22f02ecc2393
* Make list comprehensions clearer (esp. operations in loops ) 

### R/Python

* When you use `rm(list = ls())`

* Explain `lapply` / `sapply` more clearly (coercion) - and when or whether *apply function 

* Debugging include `options(error = browser)` for entering interactive debugging

* boxplot() and plot() not equivalent in some R versions?

* https://stats.stackexchange.com/questions/798/calculating-optimal-number-of-bins-in-a-histogram



### Stats

* In the Data exploration chapter, link to explanations of distributions that appears in GLM chapter. 

* t & F tests: Explain that the default of na.action in t.test is to
omit - you can check that by using getOption("na.action").  Have a look at
https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/t.test 

* Perhaps it would be could to edit the notebooks to put diff <- mean.gs[[1]][1] - mean.gs[[2]][1] to avoid confusion? 

* Clarify SD vs SE: The standard deviation (often SD) is a measure of
variability. When we calculate the standard deviation of a sample, we are using
it as an estimate of the variability of the population from which the sample was
drawn. For data with a normal distribution,2 about 95% of individuals will have
values within 2 standard deviations of the mean, the other 5% being equally
scattered above and below these limits. Contrary to popular misconception, the
standard deviation is a valid measure of variability regardless of the
distribution. About 95% of observations of any distribution usually fall within
the 2 standard deviation limits, though those outside may all be at one end. We
may choose a different summary statistic, however, when data have a skewed
distribution. 

When we calculate the sample mean we are usually interested not in the mean of this particular sample, but in the mean for individuals of this type—in statistical terms, of the population from which the sample comes. We usually collect data in order to generalise from them and so use the sample mean as an estimate of the mean for the whole population. Now the sample mean will vary from sample to sample; the way this variation occurs is described by the “sampling distri# TODO: 
 deviation, confusion is understandable. Another way of considering the standard error is as a measure of the precision of the sample mean.

The standard error of the sample mean depends on both the standard deviation and the sample size, by the simple relation SE = SD/√(sample size). The standard error falls as the sample size increases, as the extent of chance variation is reduced—this idea underlies the sample size calculation for a controlled trial, for example. By contrast the standard deviation will not tend to change as we increase the size of our sample.


So, if we want to say how widely scattered some measurements are, we use the standard deviation. If we want to indicate the uncertainty around the estimate of the mean measurement, we quote the standard error of the mean. The standard error is most useful as a means of calculating a confidence interval. For a large sample, a 95% confidence interval is obtained as the values 1.96×SE either side of the mean. We will discuss confidence intervals in more detail in a subsequent Statistics Note. The standard error is also used to calculate P values in many circumstances.


Standard deviations and standard errors
Douglas G Altman, professor of statistics in medicine and J Martin Bland, professor of health statistics

Additional article information

The terms “standard error” and “standard deviation” are often confused.1 The contrast between these two terms reflects the important distinction between data description and inference, one that all researchers should appreciate.

The standard deviation (often SD) is a measure of variability. When we calculate the standard deviation of a sample, we are using it as an estimate of the variability of the population from which the sample was drawn. For data with a normal distribution,2 about 95% of individuals will have values within 2 standard deviations of the mean, the other 5% being equally scattered above and below these limits. Contrary to popular misconception, the standard deviation is a valid measure of variability regardless of the distribution. About 95% of observations of any distribution usually fall within the 2 standard deviation limits, though those outside may all be at one end. We may choose a different summary statistic, however, when data have a skewed distribution.3

When we calculate the sample mean we are usually interested not in the mean of this particular sample, but in the mean for individuals of this type—in statistical terms, of the population from which the sample comes. We usually collect data in order to generalise from them and so use the sample mean as an estimate of the mean for the whole population. Now the sample mean will vary from sample to sample; the way this variation occurs is described by the “sampling distribution” of the mean. We can estimate how much sample means will vary from the standard deviation of this sampling distribution, which we call the standard error (SE) of the estimate of the mean. As the standard error is a type of standard deviation, confusion is understandable. Another way of considering the standard error is as a measure of the precision of the sample mean.

The standard error of the sample mean depends on both the standard deviation and the sample size, by the simple relation SE = SD/√(sample size). The standard error falls as the sample size increases, as the extent of chance variation is reduced—this idea underlies the sample size calculation for a controlled trial, for example. By contrast the standard deviation will not tend to change as we increase the size of our sample.

So, if we want to say how widely scattered some measurements are, we use the standard deviation. If we want to indicate the uncertainty around the estimate of the mean measurement, we quote the standard error of the mean. The standard error is most useful as a means of calculating a confidence interval. For a large sample, a 95% confidence interval is obtained as the values 1.96×SE either side of the mean. We will discuss confidence intervals in more detail in a subsequent Statistics Note. The standard error is also used to calculate P values in many circumstances.

The principle of a sampling distribution applies to other quantities that we may estimate from a sample, such as a proportion or regression coefficient, and to contrasts between two samples, such as a risk ratio or the difference between two means or proportions. All such quantities have uncertainty due to sampling variation, and for all such estimates a standard error can be calculated to indicate the degree of uncertainty.

In many publications a ± sign is used to join the standard deviation (SD) or standard error (SE) to an observed mean—for example, 69.4±9.3 kg. That notation gives no indication whether the second figure is the standard deviation or the standard error (or indeed something else). A review of 88 articles published in 2002 found that 12 (14%) failed to identify which measure of dispersion was reported (and three failed to report any measure of variability).4 The policy of the BMJ and many other journals is to remove ± signs and request authors to indicate clearly whether the standard deviation or standard error is being quoted. All journals should follow this practice.

* Regression - add explanation of standard error of coefficients and calculation of CI's

* ### F-test vs ANOVA 
 
 - Defn 1: the ratio of the variance calculated across the samples (groups) (the null hypothesis) to the variance within the samples (groups).
 
    This definition is about using the F-statistic in an ANOVA to check the hypothesis that two or more groups are drawn from populations with the same mean value.
  
    Defn 2: ratio of the mean sum of squares explained by the linear model to the mean sum of squares about the linear model (the variance not explained by the linear model).
 
    Here, imagine you've run a linear model on some sample data, to obtain a line (y intercept + gradient) that you hope is a good predictor for how some variables are related. Maybe the line fits well in the sense of having a low RSS, but it doesn't account for much of the variance in your data, because something else is going on that your model isn't capturing. I've drawn an example of such a situation below. The linear model (diagonal blue line) has a low RSS (i.e. is a "good fit"), but because the data actually consists of two clearly different subpopulations with different means but the same gradient, there is a lot of variance in the data that the linear model fit isn't able to capture (I've tried to show this with the difference between the two vertical lines to the right of the plot).
 
    So Defn 2 is about using the F-test in an ANOVA to determine how much of the variance in your sample can be explained by a particular linear model.
 
    You can hopefully see how this is sort of similar to the case for Defn 1; which explicitly checks if two or more specified samples are drawn from populations with the same mean. Defn 2 is about asking the same kind of question in a slightly different way - if the whole sample is drawn from populations with the same mean then the line should explain a good proportion of the variance, if in fact your sample is composed of various populations with different means, then no single line (even if it has a minimal RSS) will ever be able to explain much of the variance.
 
    In summary, both definitions are essentially asking the same question, but to different ends. One is a straightforward comparison between groups to compare their underlying means, another is a diagnostic test using the same idea in order to determine how well a linear model actually explains the data on which it's been fit.

#############

Some questions that are arising:

* How can the Tukey Honest Significant Difference test ensure a probability of 0.05 of a type I error across all tested pairs? What is different with an ordinary t-test?

    - Regarding the Tukey HSD test: You can actually think of it as a special kind of t-test, since the test statistic is very similar:

    - For the t-statistic we take the difference of the sample mean and the hypothesised mean, and divide by the standard error.

    - For the Tukey statistic we are no longer comparing a single variable's sample mean to a hypothesised true mean. Instead we have multiple groups (think of the herbivores, omnivores and carnivores in the Jupyter notebook). The Tukey test looks at all pairwise combinations of your groups (in your case: Herb-Omni, Herb-Carni and Omni-Carni) and reports whether the difference in any of their group means is larger than expected.

    - The test statistic it uses for this is philosophically very similar to the Student's t-test; we take a difference between means and divide it by a standard error. How is it different from the t-test you know and love?

    - We no longer have a "hypothesised" true mean to compare against, instead we separately take the difference between each of the pairwise group means for our numerator. For the denominator, rather than the standard error of the sample mean, we take the standard error of the sum of the group means.

    - You can think of this as a t-test that corrects for a "family-wise" error rate, which is how the type I error applies to the entire testing of all group means against each other, rather than to each comparison individually.

    - Family-wise error rate In statistics, family-wise error rate (FWER) is the probability of making one or more false discoveries, or type I errors when performing multiple hypotheses tests.

### Feedback Script

* Bug: week 1, but also 10 will end up being assessed if it exists
* Allow Week to be set to 0 for only git checking out
* Call a warning a warning and error an error
* Count up lines of code in each script and report it
* Include a weekly list of expected code files to check against?
* Include "using repository state at time..."
* Allocate points to each expected and independent code file as weighted
  percent of 100, weight determined by number of code lines; Update marking
criteria accordingly; Total baseline points are weighted average of these
two, from   which additional points are deleted for poor project
organization, readme,  etc.
* 		########## block for accessing git log - to be finished ########### 
		## Store gits codes, along with the corresponding field names in two lists:
		# GIT_COMMIT_FIELDS = ['id', 'author_name', 'author_email', 'date', 'message']
		# GIT_LOG_FORMAT = ['%H', '%an', '%ae', '%ad', '%s']
		##join the format fields together with "\x1f" (ASCII field separator) and delimit the records by "\x1e" (ASCII record separator)
		# GIT_LOG_FORMAT = '%x1f'.join(GIT_LOG_FORMAT) + '%x1e' 
		# p, log, err, time_used = run_popen('git log --format="%s"', timeout)
		# (log, _) = p.communicate()
		# log = log.strip('\n\x1e').split("\x1e")
		# log = [row.strip().split("\x1f") for row in log]
		# log = [dict(zip(GIT_COMMIT_FIELDS, row)) for row in log]
		###################################################################

### Write-up / report gudelines

* For Methods section: "Include an overview paragraph that explains your overall methodological strategy in a few lines, so that the reader can more easily make sense of the logic and content of the sequence of sections that come later."
