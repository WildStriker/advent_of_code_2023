"""test_answer_02 module (day 4)"""
import os

from advent_of_code.day_04.puzzle.part_02 import answer_02


def test_case_1():
    """
    Card 1 has four matching numbers, so you win one copy each of the next four cards:
    cards 2, 3, 4, and 5.
    Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
    Your copy of card 2 also wins one copy each of cards 3 and 4.
    Your four instances of card 3 (one original and three copies) have two matching numbers,
    so you win four copies each of cards 4 and 5.
    Your eight instances of card 4 (one original and seven copies) have one matching number,
    so you win eight copies of card 5.
    Your fourteen instances of card 5 (one original and thirteen copies) have no matching
    numbers and win no more cards.
    Your one instance of card 6 (one original) has no matching numbers and wins no more cards.

    Once all of the originals and copies have been processed, you end up with 1 instance of
    card 1, 2 instances of card 2, 4 instances of card 3, 8 instances of
    card 4, 14 instances of card 5, and 1 instance of card 6. In total,
    this example pile of scratchcards causes you to ultimately have 30 scratchcards!
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_04.txt"
        )
    ) == 30
