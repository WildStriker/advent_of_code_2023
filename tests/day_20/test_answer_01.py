"""test_answer_01 module (day 20)"""
import os

from advent_of_code.day_20.puzzle.part_01 import answer_01


def test_case_1():
    """
    The same thing happens every time the button is pushed: 8 low pulses and 4 high pulses are sent.
    So, after pushing the button 1000 times, 8000 low pulses and 4000 high pulses are sent.
    Multiplying these together gives 32000000
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_20_part1_case1.txt"
        )
    ) == 32000000


def test_case_2():
    """
    After pushing the button 1000 times, 4250 low pulses and 2750 high pulses are sent.
    Multiplying these together gives 11687500
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_20_part1_case2.txt"
        )
    ) == 11687500


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_20.txt"
        )
    ) == 812609846
