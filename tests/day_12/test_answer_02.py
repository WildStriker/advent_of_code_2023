"""test_answer_02 module (day 12)"""
import os

from advent_of_code.day_12.puzzle.part_02 import answer_02


def test_case_1():
    """Total arrangements of 525152"""
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_12.txt"
        )
    ) == 525152


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_12.txt"
        )
    ) == 65607131946466
