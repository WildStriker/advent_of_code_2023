"""test_answer_01 module (day 6)"""
import os

from advent_of_code.day_06.puzzle.part_01 import answer_01


def test_case_1():
    """
    Since the current record for this race is 9 millimeters,
    there are actually 4 different ways you could win:
    you could hold the button for 2, 3, 4, or 5 milliseconds at the start of the race.

    In the second race,
    you could hold the button for at least 4 milliseconds and at most 11 milliseconds
    and beat the record, a total of 8 different ways to win.

    In the third race,
    you could hold the button for at least 11 milliseconds and no more than 19 milliseconds
    and still beat the record, a total of 9 ways you could win.

    To see how much margin of error you have,
    determine the number of ways you can beat the record in each race; in this example,
    if you multiply these values together, you get 288 (4 * 8 * 9).
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_06.txt"
        )
    ) == 288


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_06.txt"
        )
    ) == 220320
