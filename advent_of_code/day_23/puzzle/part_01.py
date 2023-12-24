"""Part 1 Module"""
from .parse import parse_input
from .path import get_longest_path_steps


def answer_01(file_input: str):
    """Part 1"""

    map_data = parse_input(file_input)

    longest_path_steps = get_longest_path_steps(map_data, False)
    return longest_path_steps
