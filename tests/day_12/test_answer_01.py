"""test_answer_01 module (day 12)"""
import os

from advent_of_code.day_12.puzzle.part_01 import answer_01


def test_case_1():
    """Total arrangements of 21"""
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_12.txt"
        )
    ) == 21


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_12.txt"
        )
    ) == 7490
