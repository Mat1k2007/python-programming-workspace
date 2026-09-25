# PIN Extractor

A Python module that parses a collection of multiline text blocks (poems) to dynamically extract numerical PIN codes based on word lengths matching positional line indices.

## Implementation Details

This project strictly relies on foundational Python concepts:

- **Collection & Sequence Traversal:** Iterates over a list of multiline string items using nested `for` loops and tracks positional line indices via `enumerate()`.
- **String Tokenization:** Utilizes `.split('\n')` to isolate line elements and `.split()` to parse lines into word lists.
- **Index-Based Boundary Extraction:** Evaluates word availability against current line indices using standard conditional logic (`if/else`) and positional list indexing (`words[line_index]`).
- **Dynamic Accumulation:** Accumulates stringified word lengths or fallback boundary digits (`'0'`) into a secret code, returning a structured list of extracted PINs.

## How to Run

Execute the script directly via terminal:

```bash
python 02-loops-and-sequences/01-pin-extractor/pin_extractor.py