"""test_answer_01 module (day 18)"""
import os

from advent_of_code.day_18.puzzle.part_01 import answer_01


def test_case_1():
    """Folllowing the dig instructions the total area could be 62"""
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_18.txt"
        )
    ) == 62


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_18.txt"
        )
    ) == 50603
