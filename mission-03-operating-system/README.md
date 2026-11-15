# Mission 3 — Understand the operating system

## 1. Task / objective
Explore the OS, processes, storage, paths and permissions, and describe OS responsibilities.

## 2. Work completed
### Safe system observations
| Information | What it tells you | Privacy-safe observation in this environment |
|---|---|---|
| OS / system | Platform and release | macOS 27.2 (observed here) |
| Current account | Which user is active | Not included to avoid publishing an account name |
| Storage | Used and available space | About 111 GiB used and 323 GiB available on the observed volume; may change over time |
| System activity | Snapshot of running work | `ps -ax` showed system processes such as `launchd` (PID 1) and `logd` (PID 529); process names recorded without account details |

A process is a running program or task. A PID is its numeric process identifier, used by the OS to distinguish processes. The snapshot included `launchd` and `logd`, which are background system processes.

An absolute path starts at the filesystem root, such as `/Users/<account>/Downloads/digital-detective-8427/mission-03-operating-system/`. A relative path is interpreted from the current folder, such as `mission-03-operating-system/` when starting from the repository root.

| Permission | Meaning | Example |
|---|---|---|
| `r` | Read contents | Open a text file |
| `w` | Change contents | Edit a note |
| `x` | Run a file (or traverse a directory) | Run an executable script |

### OS responsibilities
| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Shares CPU time among running programs. | Switching between browser and editor |
| Memory management | Gives programs working memory and tracks its use. | Keeping an open document available |
| Device management | Coordinates hardware through drivers and services. | Sending a page to a printer |
| File management | Organizes files and storage locations. | Saving a document in a folder |
| User interface / shell | Lets a person give commands and see results. | Finder or Terminal |
| Security and permissions | Controls access to accounts, files and devices. | Restricting edits to an owned file |

## 3. Commands / tools used
`sw_vers` reported macOS 27.2; `df -h` showed about 111 GiB used and 323 GiB available; `ps -ax | head -n 8` showed the process snapshot. `pwd` and `cd ..` showed the working location change from `.../mission-02-terminal/terminal-practice` to `.../mission-02-terminal`. `ls -l` showed mode `-rw-r--r--` for the practice text file: its owner can read and write, but not execute it.

## 4. My understanding
The OS coordinates applications and hardware. Processes are active instances of programs; permissions describe what actions users can take. Absolute paths identify a location from the root, while relative paths depend on where navigation starts.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
This README; process and permissions were observed in the repository practice area.

## 8. Commit details
Commit: `Document operating system and file management`. The mission commit was pushed to GitHub.
