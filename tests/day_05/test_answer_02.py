"""test_answer_02 module (day 5)"""
import os

from advent_of_code.day_05.puzzle.part_02 import answer_02


def test_case_1():
    """
    This line describes two ranges of seed numbers to be planted in the garden.
    The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92.
    The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

    Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

    In the above example, the lowest location number can be obtained from seed number 82,
    which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46,
    and location 46. So, the lowest location number is 46.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_05.txt"
        )
    ) == 46


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_05.txt"
        )
    ) == 148041808
