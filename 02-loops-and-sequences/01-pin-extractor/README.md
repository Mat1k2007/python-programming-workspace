# PIN Extractor

A Python script that parses multiline text sequences to dynamically extract numerical PIN codes based on line indices and word lengths.

## Implementation Details
This project relies strictly on sequence iteration and string manipulation concepts covered in the curriculum:
- **Sequence Traversal:** Iterates through collections of text using `for` loops and tracks line indices via `enumerate()`.
- **String Tokenization:** Uses `.split('\n')` to extract individual lines and `.split()` to parse line words into list items.
- **Conditional Index Validation:** Compares available line word lengths against current line indices using `if/else` logic to generate PIN digits dynamically.

## File Hierarchy
- `02-loops-and-sequences/01-pin-extractor/pin_extractor.py`

## How to Run
Execute the script directly via terminal:
```bash
python 02-loops-and-sequences/01-pin-extractor/pin_extractor.py