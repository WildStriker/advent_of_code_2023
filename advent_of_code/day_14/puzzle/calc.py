"""calc module"""
from typing import List


def calculate_totals(platform: List[List[str]]) -> int:
    """calculates the total load for the platform

    Args:
        platform (List[List[str]]): platform to calcualte

    Returns:
        int: total load calculation
    """
    total_rows = len(platform)
    total = 0
    for index, row in enumerate(platform):
        score = total_rows - index
        for column in row:
            if column != "O":
                continue
            total += score

    return total
