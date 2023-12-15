"""Part 1 Module"""
from .parse import parse_input
from .hash import get_hash_value

def answer_01(file_input: str):
    """Part 1"""

    hashes = parse_input(file_input)

    totals = 0
    for current_hash in hashes:
        totals += get_hash_value(current_hash)

    return totals
