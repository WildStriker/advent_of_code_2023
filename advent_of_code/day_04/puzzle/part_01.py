"""Part 1 Module"""
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    cards = parse_input(file_input)

    total = 0

    for card in cards.values():
        score = 0
        for number_have in card.values_have:
            if number_have in card.winner_values_required:
                if score:
                    score *= 2
                else:
                    score = 1
        total += score
    return total
