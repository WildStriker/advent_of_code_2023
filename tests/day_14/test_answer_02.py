"""test_answer_02 module (day 14)"""
import os

from advent_of_code.day_14.puzzle.part_02 import answer_02


def test_case_1():
    """
    After 1000000000 cycles, the total load on the north support beams is 64.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_14.txt"
        )
    ) == 64


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_14.txt"
        )
    ) == 96447
