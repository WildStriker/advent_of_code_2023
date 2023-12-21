"""test_answer_02 module (day 20)"""
import os

from advent_of_code.day_20.puzzle.part_02 import answer_02


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_20.txt"
        )
    ) == 245114020323037
