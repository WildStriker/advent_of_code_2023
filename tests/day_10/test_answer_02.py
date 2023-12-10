"""test_answer_02 module (day 10)"""
import os

from advent_of_code.day_10.puzzle.part_02 import answer_02


def test_case_1():
    """Scanning the map, there should only be 4 locations contains inside the loop"""
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_10_part2_case1.txt"
        )
    ) == 4


def test_case_2():
    """Scanning the map, there should only be 8 locations contains inside the loop"""
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_10_part2_case2.txt"
        )
    ) == 8


def test_case_3():
    """Scanning the map, there should only be 10 locations contains inside the loop"""
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_10_part2_case3.txt"
        )
    ) == 10


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_10.txt"
        )
    ) == 351
