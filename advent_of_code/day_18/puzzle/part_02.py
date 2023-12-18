"""Part 2 Module"""
from .area import get_area
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    instructions = parse_input(file_input, True)

    return get_area(instructions)
