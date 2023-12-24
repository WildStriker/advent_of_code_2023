"""test_answer_02 module (day 23)"""
import os

from advent_of_code.day_23.puzzle.part_02 import answer_02


def test_case_1():
    """This hike contains 154 steps if slopes are climbable"""
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_23.txt"
        )
    ) == 154


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_23.txt"
        )
    ) == 6230
