project:
  name: Functional Math CLI
  description: >
    A small command-line math toolkit written in Python to reinforce algebra and
    trigonometry concepts using functional programming principles.
    This project is intentionally designed as a learning tool, not production software.

purpose:
  goals:
    - Reinforce mathematical understanding (algebra, exponents, trigonometry)
    - Practice functional decomposition and pure functions
    - Maintain a clear separation between logic and input/output
    - Learn deliberately without relying on heavy external libraries
  philosophy: >
    Instead of relying on libraries like NumPy, core math logic is written
    explicitly to reinforce how the math actually works.

design_principles:
  - Pure functions for all math operations
  - Imperative shell for CLI input/output
  - No shared state
  - No premature optimization
  - GitHub Copilot intentionally disabled during development
  - Clarity and understanding prioritized over cleverness or performance

features:
  quadratic_solver:
    description: >
      Solves quadratic equations of the form x² + bx + c = 0
      using integer factoring (AC method).
    constraints:
      - a is assumed to be 1
      - Inputs are restricted to integers
    behavior:
      - Returns factored form when possible
      - Reports when not factorable over the integers

  exponent_rules:
    multiplication:
      law: "x^a · x^b = x^(a + b)"
      implementation: pure_function
    division:
      law: "x^a / x^b = x^(a - b)"
      implementation: pure_function

functions:
  main:
    type: orchestration
    purity: impure
    responsibility:
      - Display CLI menu
      - Collect user input
      - Route execution to appropriate handlers
      - Display results
    notes: >
      Acts as the imperative shell. Contains no mathematical logic and delegates
      all computation to pure functions.

  solve_quadratic:
    type: math_logic
    purity: pure
    signature: solve_quadratic(b: int, c: int) -> str
    description: >
      Attempts to factor the quadratic equation x² + bx + c = 0
      using the AC method.
    behavior:
      - Calls find_ac_pair to determine factorability
      - Returns a factored string representation if possible
      - Returns a descriptive message if not factorable
    assumptions:
      - Coefficient a is fixed at 1
      - b and c are integers

  find_ac_pair:
    type: helper
    purity: pure
    signature: find_ac_pair(b: int, c: int) -> tuple[int, int] | null
    description: >
      Searches for two integers m and n such that:
      m * n = c and m + n = b.
    behavior:
      - Iterates through integer factor pairs of c
      - Returns the first valid (m, n) pair found
      - Returns null if no valid pair exists
    usage: >
      Internal helper used exclusively by solve_quadratic.

  multiply_exponents:
    type: math_logic
    purity: pure
    signature: multiply_exponents(a: int, b: int) -> int
    description: >
      Implements the exponent law x^a · x^b = x^(a + b).
    behavior:
      - Returns the sum of the two exponents
    notes: >
      Does not perform base validation; assumes matching bases by definition.

  subtract_exponents:
    type: math_logic
    purity: pure
    signature: subtract_exponents(a: int, b: int) -> int
    description: >
      Implements the exponent law x^a / x^b = x^(a - b).
    behavior:
      - Returns the difference of the two exponents
    notes: >
      Negative results are allowed and represent reciprocal powers.

  clear_screen:
    type: utility
    purity: impure
    description: >
      Clears the terminal screen in a cross-platform manner.
    behavior:
      - Uses 'cls' on Windows systems
      - Uses 'clear' on Unix-based systems
    notes: >
      Side-effect-only helper used to improve CLI readability.

usage:
  run_command: "python main.py"
  instructions: >
    Run the program from the project directory and follow the on-screen menu prompts.

project_structure:
  - path: main.py
    purpose: CLI entry point, routing, and function definitions
  - path: README.yaml
    purpose: Project and API documentation

planned_extensions:
  - Quadratic formula fallback for non-factorable equations
  - Radical simplification
  - Trigonometry helpers
  - Unit circle values
  - Degree and radian conversion
  - Refactor CLI routing into handler functions
  - Basic test cases

notes:
  - This project prioritizes learning and correctness over performance
  - Inputs are currently restricted to integers for clarity
  - Refactoring is expected as understanding improves

author:
  description: >
    Built as a personal learning project to reinforce mathematics and
    functional programming fundamentals.
