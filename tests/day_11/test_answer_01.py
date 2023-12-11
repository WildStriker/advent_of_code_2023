"""test_answer_01 module (day 11)"""
import os

from advent_of_code.day_11.puzzle.part_01 import answer_01


def test_case_1():
    """
    after expanding the universe,
    the sum of the shortest path between all 36 pairs of galaxies is 374
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_11.txt"
        )
    ) == 374


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_11.txt"
        )
    ) == 9418609
