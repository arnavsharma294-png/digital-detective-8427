# Mission 4 — How programs run

## 1. Task / objective
Run a simple Python program and compare compiled and interpreted execution.

## 2. Work completed
Created `hello.py`, which prints `Hello from Python`.

| Point | Compiler | Interpreter |
|---|---|---|
| When translation/execution happens | Translates a program before execution | Reads and executes instructions at runtime |
| Typical output | Translated machine code or another target form | Often no separate native executable is required for a simple run |
| Example | C compiler such as Clang | Python runtime (CPython executes bytecode internally) |
| One advantage | Can produce a standalone program and optimize it | Fast feedback while developing and testing |

A compiler translates a program before it is run, often producing a separate output. An interpreter runs instructions as the program executes. The distinction is a useful starting point, although real language implementations can combine compilation and interpretation. CPython, for example, compiles source to bytecode and executes it in its runtime.

## 3. Commands / tools used
`python3 hello.py` runs the Python file using Python 3. `print()` displays a message.

## 4. My understanding
A source file contains instructions; the Python runtime processes them and sends the printed result to the terminal. Compiler and interpreter describe execution approaches, and implementations may use both.

## 5. Difficulties faced
No major difficulties expected; run the script locally to confirm the output.

## 6. How I resolved them
Not applicable; check the actual result in Terminal.

## 7. Evidence / files
`hello.py`.

## 8. Commit details
Suggested message: `Compare compilers and interpreters`. Push and verify on GitHub.
