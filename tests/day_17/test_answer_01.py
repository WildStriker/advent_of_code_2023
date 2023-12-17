"""test_answer_01 module (day 17)"""
import os

from advent_of_code.day_17.puzzle.part_01 import answer_01


def test_case_1():
    """
    This path never moves more than three consecutive blocks in the same direction
    and incurs a heat loss of only 102.
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_17_case1.txt"
        )
    ) == 102


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_17.txt"
        )
    ) == 866
