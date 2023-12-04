"""test_answer_01 module (day 4)"""
import os

from advent_of_code.day_04.puzzle.part_01 import answer_01


def test_case_1():
    """
    Card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have
    (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have,
    four of them (48, 83, 17, and 86) are winning numbers!
    That means card 1 is worth 8 points
    (1 for the first match, then doubled three times for each of the three matches after the first).

    Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
    Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
    Card 4 has one winning number (84), so it is worth 1 point.
    Card 5 has no winning numbers, so it is worth no points.
    Card 6 has no winning numbers, so it is worth no points.

    So, in this example, the Elf's pile of scratchcards is worth 13 points.
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_04.txt"
        )
    ) == 13


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_04.txt"
        )
    ) == 25651
