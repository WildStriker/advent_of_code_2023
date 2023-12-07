"""test_answer_01 module (day 7)"""
import os

from advent_of_code.day_07.puzzle.part_01 import answer_01


def test_case_1():
    """

    32T3K is the only one pair and the other hands are all a stronger type,
    so it gets rank 1.
    KK677 and KTJJT are both two pair. Their first cards both have the same label,
    but the second card of KK677 is stronger (K vs T),
    so KTJJT gets rank 2 and KK677 gets rank 3.
    T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card,
    so it gets rank 5 and T55J5 gets rank 4.

    Now, you can determine the total winnings of this set of hands by adding up
    the result of multiplying each hand's bid with its rank
    (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5).
    So the total winnings in this example are 6440.
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_07.txt"
        )
    ) == 6440


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_07.txt"
        )
    ) == 251216224
