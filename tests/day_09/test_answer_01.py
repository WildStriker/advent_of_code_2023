"""test_answer_01 module (day 9)"""
import os

from advent_of_code.day_09.puzzle.part_01 import answer_01


def test_case_1():
    """Calculate all diffs until 0 remain between each seqeunce
    by adding these together we get the next sequence number
    in the test input this should equate to 114
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_09.txt"
        )
    ) == 114


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_09.txt"
        )
    ) == 1939607039
