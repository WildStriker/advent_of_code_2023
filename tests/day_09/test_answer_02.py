"""test_answer_02 module (day 9)"""
import os

from advent_of_code.day_09.puzzle.part_02 import answer_02


def test_case_1():
    """Calculate the inverse sequence previous number and add the totals
    in the test input this should equate to 2
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_09.txt"
        )
    ) == 2


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_09.txt"
        )
    ) == 1041
