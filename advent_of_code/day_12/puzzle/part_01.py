"""Part 1 Module"""
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    springs = parse_input(file_input, False)

    total = 0
    for spring in springs:
        total += spring.outcomes
    return total
