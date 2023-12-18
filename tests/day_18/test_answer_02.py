"""test_answer_02 module (day 18)"""
import os

from advent_of_code.day_18.puzzle.part_02 import answer_02


def test_case_1():
    """
    Folllowing the dig instructions in HEX format
    the total area could be 952408144115
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_18.txt"
        )
    ) == 952408144115


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_18.txt"
        )
    ) == 96556251590677
