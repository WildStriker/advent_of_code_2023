"""test_answer_02 module (day 15)"""
import os

from advent_of_code.day_15.puzzle.part_02 import answer_02


def test_case_2():
    """
    rn: 1 (box 0) * 1 (first slot) * 1 (focal length) = 1
    cm: 1 (box 0) * 2 (second slot) * 2 (focal length) = 4
    ot: 4 (box 3) * 1 (first slot) * 7 (focal length) = 28
    ab: 4 (box 3) * 2 (second slot) * 5 (focal length) = 40
    pc: 4 (box 3) * 3 (third slot) * 6 (focal length) = 72

    So, the above example ends up with a total focusing power of 145
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_15.txt"
        )
    ) == 145


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_15.txt"
        )
    ) == 244461
