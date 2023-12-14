"""Part 1 Module"""
from .parse import parse_input
from .reflection import calculate_found_reflection, find_reflection


def answer_01(file_input: str):
    """Part 1"""

    reflections = parse_input(file_input)

    total = 0
    for reflection in reflections:
        total += calculate_found_reflection(find_reflection(reflection))

    return total
