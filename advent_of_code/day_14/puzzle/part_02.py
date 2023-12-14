"""Part 2 Module"""
from typing import List, Optional

from .calc import calculate_totals
from .move import move_free
from .parse import parse_input

MAX_CYCLE = 1000000000


def _find_pattern(totals: List[int])-> Optional[List[int]]:
    """Try to find repeating sequences of totals

    Args:
        totals (List[int]): current list of known totals

    Returns:
        Optional[List[int]]: returns repeating section, if found
    """
    max_len = len(totals) // 2
    for to_index in range(2, max_len):
        if totals[-to_index:] == totals[2*to_index:-to_index]:
            return totals[-to_index:]

    return None


def answer_02(file_input: str):
    """Part 2"""

    platform = parse_input(file_input)
    total_rows = len(platform)
    total_columns = len(platform[0])

    totals = []
    for cycle in range(1, MAX_CYCLE + 1):
        # all columns north
        for column in range(total_columns):
            move_free(platform, (0, column), (1, 0))

        # all rows west
        for row in range(total_rows):
            move_free(platform, (row, 0), (0, 1))

        # all columns south
        for column in range(total_columns):
            move_free(platform, (total_rows-1, column), (-1, 0))

        # all rows west
        for row in range(total_rows):
            move_free(platform, (row, total_columns-1), (0, -1))

        total = calculate_totals(platform)
        totals.append(total)
        pattern = _find_pattern(totals)

        # totals are repeating!
        # calculate the last used total
        # in the patternto skip running
        # remaining cycles
        if pattern:
            remainder = MAX_CYCLE - cycle
            remainder = remainder % len(pattern)
            final_total = pattern[remainder - 1]
            break

    return final_total
