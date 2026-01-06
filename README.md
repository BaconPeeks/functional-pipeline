# Functional Math CLI

A small command-line math toolkit written in Python to reinforce algebra and
trigonometry concepts using functional programming principles.

This project is intentionally designed as a **learning tool**, not production software.

---

## Purpose

This project exists to:
- Reinforce mathematical understanding (algebra, exponents, trigonometry)
- Practice functional decomposition and pure functions
- Maintain a clear separation between logic and input/output
- Learn deliberately without relying on heavy external libraries

Instead of relying on libraries like NumPy, core math logic is written explicitly
to reinforce how the math actually works.

---

## Design Principles

- Pure functions for all math operations
- Imperative shell for CLI input/output
- No shared state
- No premature optimization
- GitHub Copilot intentionally disabled during development
- Clarity and understanding prioritized over cleverness or performance

---

## Features

### Quadratic Solver (a = 1)

Solves quadratic equations of the form:

x² + bx + c = 0

using integer factoring (AC method).

**Constraints**
- Coefficient `a` is assumed to be `1`
- Inputs are restricted to integers

**Behavior**
- Returns factored form when possible
- Reports when not factorable over the integers

---

### Exponent Rules

**Multiplication**
x^a · x^b = x^(a + b)

**Division**
x^a / x^b = x^(a - b)


All exponent logic is implemented as pure functions.

---

## Functions

### `main()`
- Acts as the CLI orchestration layer
- Displays the menu
- Collects user input
- Routes execution to the appropriate handlers
- Displays results

Contains **no mathematical logic**.

---

### `solve_quadratic(b: int, c: int) -> str`
Attempts to factor the quadratic equation:

x² + bx + c = 0



using the AC method.

- Calls `find_ac_pair` to determine factorability
- Returns a factored string if possible
- Returns a descriptive message if not factorable

Assumptions:
- `a = 1`
- `b` and `c` are integers

---

### `find_ac_pair(b: int, c: int) -> tuple[int, int] | None`
Searches for integers `m` and `n` such that:

m * n = c
m + n = b


- Iterates through integer factor pairs of `c`
- Returns the first valid `(m, n)` pair
- Returns `None` if no valid pair exists

---

### `multiply_exponents(a: int, b: int) -> int`
Implements:
x^a · x^b = x^(a + b)


Returns the resulting exponent.

---

### `subtract_exponents(a: int, b: int) -> int`
Implements:
x^a / x^b = x^(a - b)


Negative results are allowed and represent reciprocal powers.

---

### `clear_screen()`
Utility function to clear the terminal screen:
- Uses `cls` on Windows
- Uses `clear` on Unix-based systems

---

## How to Run

```bash
python main.py
```