# Git Lecture Plan

Design this as a 75-90 minute live-coding session in VS Code, with students following along in a disposable repository.

## 1. Why Git?

- Show the `final_v7_reallyfinal` problem.
- Explain Git versus GitHub.
- Introduce the four places:

  ```text
  working directory -> staging area -> local repository -> remote repository
  ```

## 2. Preflight

Check Git installation and identity:

```bash
git --version
git config --global user.name
git config --global user.email
```

Create a disposable practice repository:

```bash
mkdir -p ~/Documents/git-practice
cd ~/Documents/git-practice
git init -b main
```

Add a visible checkpoint so everyone is in the same directory.

## 3. Create the first snapshot

- Create `README.md`.
- Demonstrate that Git does not automatically track new files.
- Use the complete loop:

  ```text
  edit -> status -> diff -> add -> diff --staged -> commit -> log
  ```

- Have students predict what each command will show.

## 4. Explain the staging area

- Change two files.
- Stage only one.
- Show that the working directory and proposed commit can differ.
- Use:

  ```bash
  git diff
  git diff --staged
  ```

This is the most important conceptual demonstration.

## 5. Ignore files before broad staging

- Create `.gitignore` before using `git add -A`.
- Add a temporary file and show that Git ignores it.
- Explain that `.gitignore` does not remove files already committed.

## 6. Write useful commits

- Make one deliberately vague commit message.
- Improve it using an imperative, specific message.
- Show:

  ```bash
  git log --oneline
  ```

Keep commit-message advice practical rather than spending too long on formal rules.

## 7. Recover from mistakes

Demonstrate the least destructive commands first:

```bash
git restore file.txt
git restore --staged file.txt
git revert <commit>
```

Put this in a danger box:

```bash
git reset --hard HEAD
```

Emphasize: run `git status` before attempting recovery.

## 8. Branches as experiments

- Create and switch to a branch:

  ```bash
  git switch -c experiment
  ```

- Change and commit a file.
- Switch back to `main`.
- Show that the change is absent from `main`.
- Merge the branch and explain a fast-forward merge.

## 9. Create a remote

- Connect the local practice repository to GitHub.
- Explain `origin` as a nickname.
- Demonstrate:

  ```bash
  git remote -v
  git push -u origin main
  ```

- Explain the relationship between local `main` and `origin/main`.

## 10. Fetch versus pull

- Make or simulate a remote change.
- Show:

  ```bash
  git fetch origin
  git log --oneline --all
  git pull
  ```

Explain that `fetch` downloads information while `pull` fetches and integrates.

## 11. Small collaboration exercise

- Create a feature branch.
- Commit a focused change.
- Push it.
- Open a pull request.
- Explain review, merging and branch cleanup.

## 12. Practical handoff

Students should apply the workflow to their coursework repository only after practising:

- inspect the existing directory,
- create or review `.gitignore`,
- initialize or clone appropriately,
- make a first deliberate commit,
- push to GitHub,
- verify the remote repository, and
- record contributions in `README.md` and `CONTRIBUTIONS.md`.

## 13. Recovery slide

Keep this visible while students work:

```bash
pwd
git status
git log --oneline --decorate --graph
```

The standard response to confusion is:

> Stop, run `git status`, inspect the changes, and only then issue another command.

## Lecture design notes

- Use the revised Git chapter as reference material, but focus the live session on one practice repository and one repeatable local workflow.
- Keep object internals, hashes, large files, hooks and advanced collaboration commands in the chapter rather than competing for live-demo time.
- Use `::: notes` blocks for presenter guidance and visible checkpoint callouts for student instructions.
- Render the lecture after changes and verify that all embedded notebook fragments still resolve.
- Test every displayed command in a fresh temporary repository before delivering the lecture.
