# Mission 6 — Git and GitHub

## 1. Task / objective
Explain Git’s basic workflow, branches and Pull Requests, and document the command glossary.

## 2. Work completed
| Git operation | Explanation |
|---|---|
| Initialize | `git init` starts tracking a project as a repository. |
| Check status | `git status` shows changed, staged and untracked files. |
| Stage selected changes | `git add path` selects changes for the next commit. |
| Commit | `git commit -m "message"` records staged changes in local history. |
| View history | `git log --oneline` lists recent commits. |
| Create/list branches | `git branch update-about` creates a branch; `git branch` lists branches. |
| Switch branches | `git switch update-about` changes the working branch. |
| Publish changes | `git push` sends local commits to a remote repository. |
| Retrieve remote changes | `git pull` fetches and integrates remote changes. |

Staging is a preparation area where selected edits are gathered. A commit records those staged edits as a named point in local history. A branch is an independent line of changes. A Pull Request asks collaborators to review proposed branch changes before merging them.

Suggested “My Learning” section for the root README: “I learned how input becomes processed output, how Python can convert between number bases, and how Git records changes. I also learned that a Pull Request gives people a place to review a proposed change.” Rewrite this in your own words and add it on the `update-about` branch.

Pull Request title: `Add My Learning section to the project README`.

## 3. Commands / tools used
`git status`, `git add`, `git commit`, `git log`, `git branch`, `git switch`, `git push` and `git pull` are the core operations. GitHub hosts the remote repository and Pull Request review.

## 4. My understanding
Git commits are local records until they are pushed to a remote. Branches let someone work separately, and a Pull Request presents the change for review. The `main` and `update-about` branches were pushed to the supplied remote. A Pull Request still needs to be opened and its actual URL and status recorded.

## 5. Difficulties faced
The branches were published successfully; the Pull Request has not been created because GitHub CLI authentication is unavailable in this environment.

## 6. How I resolved them
Open the compare link for `update-about` into `main`, create the Pull Request, and record its actual URL and status here. Merge only if the instructor requests it.

## 7. Evidence / files
This README; add the real Pull Request URL or a privacy-safe screenshot after creating it.

## 8. Commit details
Commit: `Complete Git and GitHub collaboration mission`. Mission commit and branch push completed; Pull Request remains pending.
