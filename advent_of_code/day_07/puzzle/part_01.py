"""Part 1 Module"""
from .game import calculate_winnings
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    hands = parse_input(file_input)

    total = calculate_winnings(hands, False)

    return total
