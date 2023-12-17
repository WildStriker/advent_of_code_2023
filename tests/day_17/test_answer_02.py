"""test_answer_02 module (day 17)"""
import os

from advent_of_code.day_17.puzzle.part_02 import answer_02


def test_case_1():
    """
    An ultra crucible would incur the minimum possible heat loss of 94
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_17_case1.txt"
        )
    ) == 94


def test_case_2():
    """
    This route causes the ultra crucible to incur the minimum possible heat loss of 71
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_17_case2.txt"
        )
    ) == 71


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_17.txt"
        )
    ) == 1010
