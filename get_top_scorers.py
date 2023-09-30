"""
Ninety-One Interview Submission

This module contains a set of functions designed for parsing and processing data
from a file to identify and display the top scorers. Specifically, it provides
utilities to load data from a file, parse that data into a convenient format,
and analyze it to determine the highest score and identify all the individuals
who attained it.

Functions:
    - load_file(file_path: str) -> str
        Load a file and return its content as a string.

    - parse_file(file_data: str) -> List[Tuple[str, int]]
        Parse a string containing file data into a list of tuples containing
        name and score data.

    - find_top_scorers(parsed_data: List[Tuple[str, int]]) -> Tuple[int, List[str]]
        Find and return the highest score and a list of names who achieved
        that score from the provided parsed data.
"""


from typing import List, Tuple


def load_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("The specified file could not be found.")


def parse_file(data: str) -> List[Tuple[str, int]]:
    lines = data.strip().split('\n')[1:]
    parsed_data = []
    for line in lines:
        first_name, second_name, score = line.split(',')
        full_name = f"{first_name} {second_name}"
        parsed_data.append((full_name, int(score)))
    return parsed_data


def find_top_scorers(parsed_data: List[Tuple[str, int]]) -> Tuple[int, List[str]]:
    top_score = max(parsed_data, key=lambda x: x[1])[1]
    top_scorers = sorted(name for name, score in parsed_data if score == top_score)
    return top_score, top_scorers


def print_top_scorers(top_score: int, top_scorers: List[str]) -> None:
    print("\n".join(top_scorers))
    print(f"Score: {top_score}")


try:
    file_path = "TestData.csv"
    file_data = load_file(file_path)

    parsed_data = parse_file(file_data)
    top_score, top_scorers = find_top_scorers(parsed_data)
    print_top_scorers(top_score, top_scorers)

except Exception as e:
    print(f"An error occurred: {str(e)}")
