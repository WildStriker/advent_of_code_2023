"""test_answer_02 module (day 13)"""
import os

from advent_of_code.day_13.puzzle.part_02 import answer_02


def test_case_1():
    """Found reflections should summarize up to 405"""
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_13.txt"
        )
    ) == 400


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_13.txt"
        )
    ) == 29341
