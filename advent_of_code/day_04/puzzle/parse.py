"""parse module"""
from dataclasses import dataclass
from typing import Set, Iterator, Dict


@dataclass
class Card:
    """Cards data for each round"""
    card_num: int
    instance_count: int
    winner_values_required: Set[int]
    values_have: Iterator[int]


def parse_input(input_file: str) -> Dict[int, Card]:
    """parse input file to dictioanry of cards

    Args:
        input_file (str): puzzle input

    Returns:
        Dict[int, Card]: parsed game card info
    """
    cards = {}
    with open(input_file, encoding="utf-8") as file_input:
        for line in file_input:
            card_num, lists = line.split(":")
            card_num = int(card_num.split()[-1])
            winner_values, values_have = lists.strip().split("|")
            winner_values = set(
                map(
                    int,
                    winner_values.split()
                )
            )
            values_have = map(
                int,
                values_have.split()
            )

            cards[card_num] = Card(card_num, 1, winner_values, values_have)

    return cards
