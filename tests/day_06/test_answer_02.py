"""test_answer_02 module (day 6)"""
import os

from advent_of_code.day_06.puzzle.part_02 import answer_02


def test_case_1():
    """
    In this example, the race lasts for 71530 milliseconds and the
    record distance you need to beat is 940200 millimeters.

    You could hold the button anywhere from 14 to 71516 milliseconds
    and beat the record, a total of 71503 ways!
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_06.txt"
        )
    ) == 71503


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_06.txt"
        )
    ) == 34454850
