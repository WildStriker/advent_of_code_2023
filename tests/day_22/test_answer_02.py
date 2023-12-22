"""test_answer_02 module (day 22)"""
import os

from advent_of_code.day_22.puzzle.part_02 import answer_02


def test_case_1():
    """
    Disintegrating brick A would cause all 6 other bricks to fall.
    Disintegrating brick F would cause only 1 other brick, G, to fall.

    Disintegrating any other brick would cause no other bricks to fall.
    So, in this example, the sum of the number of other bricks that would
    fall as a result of disintegrating each brick is 7.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_22.txt"
        )
    ) == 7


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_22.txt"
        )
    ) == 61297
