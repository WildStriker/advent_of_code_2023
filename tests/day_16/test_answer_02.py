"""test_answer_01 module (day 16)"""
import os

from advent_of_code.day_16.puzzle.part_02 import answer_02


def test_case_1():
    """
    the beam could start on any tile in the top row (heading downward),
    any tile in the bottom row (heading upward),
    any tile in the leftmost column (heading right),
    or any tile in the rightmost column (heading left). 

    To produce lava, you need to find the configuration that energizes as many tiles as possible.
    51 is the highest configuration
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_16.txt"
        )
    ) == 51


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_16.txt"
        )
    ) == 8335
