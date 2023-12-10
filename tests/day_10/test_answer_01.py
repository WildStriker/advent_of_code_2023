"""test_answer_01 module (day 10)"""
import os

from advent_of_code.day_10.puzzle.part_01 import answer_01


def test_case_1():
    """Traversing the pipes, the farthest point is 4"""
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_10_part1_case1.txt"
        )
    ) == 4


def test_case_2():
    """Traversing the pipes, the farthest point is 8"""
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_10_part1_case2.txt"
        )
    ) == 8


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_10.txt"
        )
    ) == 6768
