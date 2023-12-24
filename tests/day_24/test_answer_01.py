"""test_answer_01 module (day 24)"""
import os

from advent_of_code.day_24.puzzle.part_01 import answer_01


def test_case_1():
    """
    2 hailstones' future paths cross inside the boundaries of the test area.
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_24.txt"
        ),
        7,
        27,
    ) == 2


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_24.txt"
        ),
        200000000000000,
        400000000000000,
    ) == 17906
