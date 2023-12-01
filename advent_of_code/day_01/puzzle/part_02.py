"""Part 2 Module"""
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    calibration_values = parse_input(file_input, False)
    return sum(calibration_values)
