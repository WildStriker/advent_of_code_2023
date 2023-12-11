"""Part 2 Module"""
from .pairs import get_total_pair_distances
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    galaxy_mapping = parse_input(file_input, 1000000)

    total = get_total_pair_distances(galaxy_mapping)

    return total
