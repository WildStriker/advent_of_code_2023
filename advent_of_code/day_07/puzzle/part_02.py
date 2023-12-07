"""Part 2 Module"""
from .game import calculate_winnings
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    hands = parse_input(file_input)

    total = calculate_winnings(hands, True)

    return total
