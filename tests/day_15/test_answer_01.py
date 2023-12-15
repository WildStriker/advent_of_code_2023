"""test_answer_01 module (day 15)"""
import os

from advent_of_code.day_15.puzzle.part_01 import answer_01


def test_case_1():
    """The sum of these results is 1320"""
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_15.txt"
        )
    ) == 1320


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_15.txt"
        )
    ) == 514025
