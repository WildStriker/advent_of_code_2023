"""Part 1 Module"""
from .area import get_area
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    instructions = parse_input(file_input, False)

    return get_area(instructions)
