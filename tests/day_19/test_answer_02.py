"""test_answer_02 module (day 19)"""
import os

from advent_of_code.day_19.puzzle.part_02 import answer_02


def test_case_1():
    """TODO"""
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_19.txt"
        )
    ) == 167409079868000


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_19.txt"
        )
    ) == 135506683246673
