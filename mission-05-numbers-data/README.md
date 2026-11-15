# Mission 5 — Numbers and data

## 1. Task / objective
Convert numbers among decimal, binary and hexadecimal, verify with Python, build a converter and explain text encoding.

## 2. Work completed
### Manual conversions
- Decimal 13: 13 = 8 + 4 + 1, so binary is `1101`.
- Decimal 25: 25 = 16 + 8 + 1, so binary is `11001`.
- Binary `1010`: 1×8 + 0×4 + 1×2 + 0×1 = 10.
- Binary `1101`: 1×8 + 1×4 + 0×2 + 1×1 = 13.
- Hex `A`: A represents 10 in decimal.
- Hex `1F`: 1×16 + 15 = 31.
- Binary `1111`: four 1-bits represent decimal 15, which is hexadecimal `F`.

### Python verification
| Expression | Result | Matches? |
|---|---:|---|
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `hex(13)` | `0xd` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `int('A', 16)` | `10` | Yes |

### Converter sample runs
| Input | Binary | Hexadecimal |
|---:|---|---|
| 13 | `1101` | `d` |
| 25 | `11001` | `19` |
| 42 | `101010` | `2a` |

Python’s `bin()` returns a binary string with a `0b` prefix, and `hex()` returns a hexadecimal string with a `0x` prefix. The program removes those prefixes for concise display.

### Text encoding
The ASCII decimal code for uppercase `A` is 65; lowercase `a` is 97. An encoding standard gives computers a shared mapping between characters and numbers, so text can be stored and interpreted consistently. A snowman (`☃`) is not part of basic ASCII.

## 3. Commands / tools used
`python3` runs the converter; `input()` reads a value, `int()` converts it to an integer, `bin()` and `hex()` format the number, and `print()` displays results. `ord('A')` and `ord('a')` return 65 and 97.

## 4. My understanding
Binary uses powers of two and hexadecimal uses powers of sixteen. Hexadecimal is compact because one hex digit represents four binary bits. Character encoding maps text symbols to numeric data.

## 5. Difficulties faced
No major difficulties; sample values were verified with Python.

## 6. How I resolved them
Compared built-in conversion results with the hand calculations.

## 7. Evidence / files
`number_converter.py` and the calculations and sample cases in this README.

## 8. Commit details
Suggested message: `Build number converter and practise data representation`. Push and verify on GitHub.
