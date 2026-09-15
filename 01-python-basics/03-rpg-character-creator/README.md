# RPG Character Creator

A Python module that validates character parameters and returns a formatted ASCII stat sheet.

## Implementation Details
This project relies strictly on foundational Python concepts:
- **Input Type Checking:** Uses `isinstance()` to ensure valid string and integer parameters.
- **Space Validation:** Checks for space characters by comparing string length variations via `len()` and `.replace()`.
- **Stat Calculations:** Enforces allocation limits (1 to 4 per attribute, total sum equal to 7).
- **Formatting:** Constructs the visual stat sheet with string multiplication and multi-line f-strings.

## File Hierarchy
- `01-python-basics/03-rpg-character-creator/rpg_character.py`

## How to Run
Execute the script directly via terminal:
```bash
python 01-python-basics/03-rpg-character-creator/rpg_character.py