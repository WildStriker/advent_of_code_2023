"""parse module"""
from dataclasses import dataclass
from typing import List


@dataclass
class Hand:
    """Hand info"""
    cards: str
    bid: int


def parse_input(input_file: str) -> List[Hand]:
    """parse input file and returns a list of hands

    Args:
        input_file (str): input file to parse

    Returns:
        List[Hand]: list of hands
    """

    hands = []
    with open(input_file, encoding="utf-8") as file_input:
        for line in file_input:
            cards, bid = line.strip().split()
            bid = int(bid)
            hands.append(Hand(cards, bid))

    return hands
