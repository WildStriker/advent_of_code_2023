"""Part 2 Module"""
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    cards = parse_input(file_input)

    total = 0

    for card in cards.values():
        total += card.instance_count
        winning_count = 0
        for number_have in card.values_have:
            if number_have in card.winner_values_required:
                winning_count += 1

        for count in range(1, winning_count + 1):
            cards[card.card_num + count].instance_count += card.instance_count

    return total
