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
| System activity | Snapshot of running work | Use Activity Monitor or `ps` locally; process list not captured in this draft |

A process is a running program or task. A PID is its numeric process identifier, used by the OS to distinguish processes. Examples include a browser and a text editor.

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
`sw_vers` reports macOS details; `df -h` reports filesystem capacity; `ps` or Activity Monitor can show processes; `pwd`, `cd` and `ls -l` help inspect paths and permissions. Verify observations on the computer used for submission.

## 4. My understanding
The OS coordinates applications and hardware. Processes are active instances of programs; permissions describe what actions users can take. Absolute paths identify a location from the root, while relative paths depend on where navigation starts.

## 5. Difficulties faced
The process snapshot and file permission observation have not been captured for this draft.

## 6. How I resolved them
Use Activity Monitor or `ps` and `ls -l` inside the repository practice area, then record privacy-safe observations.

## 7. Evidence / files
This README; add a redacted process and permission observation if required by your instructor.

## 8. Commit details
Suggested message: `Document operating system and file management`. Push and verify on GitHub.
