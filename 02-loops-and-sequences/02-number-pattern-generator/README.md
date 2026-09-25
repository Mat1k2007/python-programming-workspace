# Number Pattern Generator

A lightweight Python module that generates formatted numerical string sequences based on strict type validation and integer bounds.

## Implementation Details

This project strictly relies on foundational Python concepts:

- **Type Safety:** Validates integer instances using `isinstance()` to reject non-integer parameters prior to execution.
- **Boundary Checking:** Ensures positive input bounds ($n \ge 1$) before initializing loop constructs.
- **Sequence Iteration:** Constructs numerical sequences via standard `for` loops and `range()` boundary limits.
- **String Formatting:** Concatenates stringified integers into a space-separated format using `' '.join()`.

## How to Run

Execute the script directly via terminal:

```bash
python 02-loops-and-sequences/02-number-pattern-generator/number_pattern_generator.py