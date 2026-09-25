# Number Pattern Generator

A lightweight Python module that generates formatted numerical string sequences based on strict type validation and integer bounds.

## Implementation Details
This project enforces sequence generation and control flow fundamentals:
- **Type Safety:** Validates integer instances using `isinstance()` to reject non-integer parameters.
- **Boundary Checking:** Ensures input bounds ($n \ge 1$) before executing loop logic.
- **Sequence Iteration:** Constructs numerical sequences via standard `for` loops and `range()` bounds.
- **String Formatting:** Concatenates stringified integers using `' '.join()`.

## File Hierarchy
- `02-loops-and-sequences/02-number-pattern-generator/number_pattern_generator.py`

## How to Run
Execute the script directly via terminal:
```bash
python 02-loops-and-sequences/02-number-pattern-generator/number_pattern_generator.py