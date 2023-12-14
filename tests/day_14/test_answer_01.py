"""test_answer_01 module (day 14)"""
import os

from advent_of_code.day_14.puzzle.part_01 import answer_01


def test_case_1():
    """
    The total load is the sum of the load caused by all of the rounded rocks.
    In this example, the total load is 136
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_14.txt"
        )
    ) == 136


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_14.txt"
        )
    ) == 108614
