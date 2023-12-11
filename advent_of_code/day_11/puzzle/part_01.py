"""Part 1 Module"""
from .pairs import get_total_pair_distances
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    galaxy_mapping = parse_input(file_input, 2)

    total = get_total_pair_distances(galaxy_mapping)

    return total
