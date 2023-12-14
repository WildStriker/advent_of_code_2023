"""Part 1 Module"""
from .calc import calculate_totals
from .move import move_free
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    platform = parse_input(file_input)
    total_columns = len(platform[0])
    for column in range(total_columns):
        move_free(platform, (0, column), (1, 0))

    return calculate_totals(platform)
