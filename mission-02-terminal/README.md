# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Practise safe file operations, understand command options and pipes, and explain package managers.

## 2. Work completed
| Operation | Command | What it does / observation |
|---|---|---|
| Current directory | `pwd` | Prints the absolute location of the working folder. |
| List files | `ls` | Shows visible names in the current folder. |
| Detailed listing | `ls -l` | Adds permissions, owner, size and modification time. |
| Parent folder | `cd ..` | Moves one directory upward. |
| Create directory | `mkdir practice` | Creates a new directory. |
| Empty file | `touch practice/notes.txt` | Creates an empty file if it does not exist. |
| Copy file | `cp practice/notes.txt practice/copy.txt` | Makes a second file with the same initial contents. |
| Rename / move | `mv practice/copy.txt practice/renamed.txt` | Moves a file or changes its name. |
| Display contents | `cat practice/notes.txt` | Prints the file contents. |

File practice: `terminal-practice/notes.txt` contains two sample lines; a backup copy is included. Appending adds text after existing content (for example `>>`); replacing writes new content over what was there (for example `>`). Copying leaves the original in place; moving relocates the file or changes its name.

`ls -lah` includes hidden entries (`-a`), uses a long listing (`-l`), and displays readable sizes (`-h`). In `ls -l | head`, the pipe passes the listing output into `head`, which prints only the first few lines.

A package manager such as Homebrew installs, updates and removes software while managing dependencies. It can help keep command-line tools consistent. Homebrew version observed: 7.0.12. No package was installed or removed.

## 3. Commands / tools used
`pwd` (location), `ls` (listing), `cd` (navigation), `mkdir` (directory), `touch` (empty file), `cp` (copy), `mv` (move/rename), `cat` (read file), `head` (first lines), `|` (pipe), `brew --version` (version check).

## 4. My understanding
The current directory tells commands where they act. Listings help inspect that location before changing files. Flags modify a command’s output, and pipes connect one command’s output to another command’s input. Work should stay in the assignment practice folder.

## 5. Difficulties faced
No major difficulties in the documented examples. Re-run the commands in your repository and record any actual errors or differences.

## 6. How I resolved them
Not applicable; confirm by performing the practice on the intended computer.

## 7. Evidence / files
`terminal-practice/notes.txt` and `terminal-practice/notes-backup.txt`.

## 8. Commit details
Suggested message: `Complete Terminal and file management mission`. Push and verify on GitHub.
