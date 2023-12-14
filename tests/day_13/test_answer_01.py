"""test_answer_01 module (day 13)"""
import os

from advent_of_code.day_13.puzzle.part_01 import answer_01


def test_case_1():
    """Found reflections should summarize up to 405"""
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_13.txt"
        )
    ) == 405


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_13.txt"
        )
    ) == 34993
