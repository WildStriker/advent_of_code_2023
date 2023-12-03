"""test_answer_01 module (day 3)"""
import os

from advent_of_code.day_03.puzzle.part_01 import answer_01


def test_case_1():
    """In this schematic, two numbers are not part numbers because
    they are not adjacent to a symbol: 114 (top right) and 58 (middle right).
    Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_03.txt"
        )
    ) == 4361
