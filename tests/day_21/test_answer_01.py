"""test_answer_01 module (day 21)"""
import os

from advent_of_code.day_21.puzzle.part_01 import answer_01


def test_case_1():
    """
    if the Elf's goal was to get exactly 6 more steps today,
    he could use them to reach any of 16 garden plots
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_21.txt"
        ),
        6
    ) == 16

def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_21.txt"
        ),
        64
    ) == 3858

