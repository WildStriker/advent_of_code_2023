"""test_answer_02 module (day 1)"""
import os

from advent_of_code.day_01.puzzle.part_02 import answer_02


def test_case_1():
    """In this example, the calibration values are
    29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281."""
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_01_part2_case1.txt"
        )
    ) == 281
