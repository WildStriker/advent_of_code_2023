"""Part 2 Module"""
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    parts = parse_input(file_input)
    total = 0
    for _coords, part in parts.items():

        # this is not a gear with only two part numbers skip it!
        if part.symbol != "*" or len(part.numbers) != 2:
            continue

        gear_ratio = 1
        for number in part.numbers:
            gear_ratio *= number
        total += gear_ratio

    return total
