"""test_answer_01 module (day 1)"""
import os

from advent_of_code.day_01.puzzle.part_01 import answer_01


def test_case_1():
    """In this example, the calibration values of these
    four lines are 12, 38, 15, and 77. Adding these together produces 142."""
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_01_part1_case1.txt"
        )
    ) == 142
