"""Part 1 Module"""
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    calibration_values = parse_input(file_input, True)
    return sum(calibration_values)
