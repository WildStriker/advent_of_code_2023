"""test_answer_01 module (day 23)"""
import os

from advent_of_code.day_23.puzzle.part_01 import answer_01


def test_case_1():
    """This hike contains 94 steps"""
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_23.txt"
        )
    ) == 94


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_23.txt"
        )
    ) == 1930
