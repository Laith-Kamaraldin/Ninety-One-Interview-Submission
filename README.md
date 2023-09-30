# Ninety-One Interview Submission

## Overview
This codebase contains solutions for an interview task assigned which involves extracting and processing data from 
a CSV file to identify top scorers. The problem statement can be found in PDF file problem_statement.pdf in the same directory.

## Prerequisites
- Python 3.x

## Usage

### Files
- `get_top_scorers.py`: Includes functions to parse the CSV and identify top scorers.
- `test_top_scorers.py`: Contains unittests for the functions in `get_top_scorers.py`.

### Running the Script
```
python get_top_scorers.py
```

### Running the unit tests
```
python -m unittest test_top_scorers.py
```

###Design Choices and Assumptions

#####Functional Approach: 
Chose a simple, straightforward script with distinct functions (load_csv, parse_csv, find_top_scorers) instead of a class-based approach to avoid unnecessary complexity.
Separation of Concerns: Each function handles a single task, ensuring simplicity and adherence to the Single Responsibility Principle.
Data Format: Utilized a list of tuples to store parsed data, with each tuple containing a full name (string) and score (integer) for easy handling.
Exception Handling: Basic error management is included to handle common issues like file not found or incorrect data format.

#####Assumptions:
Data Format: Assumes file data is structured as (first name, second name, score) and score is an integer.
Data Validity: Assumes that the provided data is clean and does not require extensive validation.

######Why Not a Class?
A class might bring additional complexity without clear benefits for this simple, linear flow of operations. A functional approach offers clear, readable, and easily testable code.
If the script grows in functionality in the future (e.g., additional filtering, handling various data formats), considering a class structure might be revisited.