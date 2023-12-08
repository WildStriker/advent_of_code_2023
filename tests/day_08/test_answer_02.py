"""test_answer_02 module (day 8)"""
import os

from advent_of_code.day_08.puzzle.part_02 import answer_02


def test_case_1():
    """
    Step 0: You are at 11A and 22A.
    Step 1: You choose all of the left paths, leading you to 11B and 22B.
    Step 2: You choose all of the right paths, leading you to 11Z and 22C.
    Step 3: You choose all of the left paths, leading you to 11B and 22Z.
    Step 4: You choose all of the right paths, leading you to 11Z and 22B.
    Step 5: You choose all of the left paths, leading you to 11B and 22C.
    Step 6: You choose all of the right paths, leading you to 11Z and 22Z.

    So, in this example, you end up entirely on nodes that end in Z after 6 
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_08_part2.txt"
        )
    ) == 6


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_08.txt"
        )
    ) == 14935034899483
