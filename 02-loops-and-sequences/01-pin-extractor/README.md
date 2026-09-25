# PIN Extractor

A Python module that parses multiline text sequences to dynamically extract numerical PIN codes based on line indices and word lengths.

## Implementation Details

This project strictly relies on foundational Python concepts:

- **Sequence Traversal:** Iterates through collection blocks using standard `for` loops and tracks positional indices via `enumerate()`.
- **String Tokenization:** Applies `.split('\n')` to isolate line entries and `.split()` to parse individual words into list elements.
- **Conditional Index Validation:** Evaluates word lengths against line indices using `if/else` logic to generate valid PIN digits dynamically.

## How to Run

Execute the script directly via terminal:

```bash
python 02-loops-and-sequences/01-pin-extractor/pin_extractor.py