"""test_answer_01 module (day 22)"""
import os

from advent_of_code.day_22.puzzle.part_01 import answer_01


def test_case_1():
    """
    Brick A cannot be disintegrated safely;
    if it were disintegrated,bricks B and C would both fall.
    Brick B can be disintegrated;
    the bricks above it (D and E) would still be supported by brick C.

    Brick C can be disintegrated;
    the bricks above it (D and E) would still be supported by brick B.

    Brick D can be disintegrated;
    the brick above it (F) would still be supported by brick E.

    Brick E can be disintegrated;
    the brick above it (F) would still be supported by brick D.

    Brick F cannot be disintegrated;
    the brick above it (G) would fall.

    Brick G can be disintegrated;
    it does not support any other bricks.

    So, in this example, 5 bricks can be safely disintegrated.
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_22.txt"
        )
    ) == 5


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_22.txt"
        )
    ) == 405
