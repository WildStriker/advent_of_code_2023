"""Part 2 Module"""
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    springs = parse_input(file_input, True)

    total = 0
    for spring in springs:
        total += spring.outcomes
    return total
