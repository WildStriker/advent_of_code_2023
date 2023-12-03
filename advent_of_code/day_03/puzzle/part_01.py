"""Part 1 Module"""
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    parts = parse_input(file_input)
    total = 0
    for coords, part in parts.items():

        # this has no symbols, skip it!
        if coords is None:
            continue

        for number in part.numbers:
            total += number

    return total
