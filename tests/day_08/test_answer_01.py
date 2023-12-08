"""test_answer_01 module (day 8)"""
import os

from advent_of_code.day_08.puzzle.part_01 import answer_01


def test_case_1():
    """
    Starting with AAA, you need to look up the next element based on the next
    left/right instruction in your input. In this example,
    start with AAA and go right (R) by choosing the right element of AAA, CCC.
    Then, L means to choose the left element of CCC, ZZZ.
    By following the left/right instructions, you reach ZZZ in 2 steps
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_08_part1_case1.txt"
        )
    ) == 2


def test_case_2():
    """
    If you run out of left/right instructions, repeat the whole sequence of instructions
    as necessary: RL really means RLRLRLRLRLRLRLRL... and so on.
    For example, here is a situation that takes 6 steps to reach ZZZ
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_08_part1_case2.txt"
        )
    ) == 6


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_08.txt"
        )
    ) == 15517
