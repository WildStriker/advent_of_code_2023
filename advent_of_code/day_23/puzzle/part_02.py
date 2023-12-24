"""Part 2 Module"""
from .parse import parse_input
from .path import get_longest_path_steps


def answer_02(file_input: str):
    """Part 2"""

    map_data = parse_input(file_input)

    longest_path_steps = get_longest_path_steps(map_data, True)
    return longest_path_steps
