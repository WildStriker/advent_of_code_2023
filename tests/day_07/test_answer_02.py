"""test_answer_02 module (day 7)"""
import os

from advent_of_code.day_07.puzzle.part_02 import answer_02


def test_case_1():
    """
    32T3K is still the only one pair; it doesn't contain any jokers,
    so its strength doesn't increase.
    KK677 is now the only two pair, making it the second-weakest hand.
    T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3,
    QQQJA gets rank 4, and KTJJT gets rank 5.

    With the new joker rule, the total winnings in this example are 5905.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_07.txt"
        )
    ) == 5905


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_07.txt"
        )
    ) == 250825971
