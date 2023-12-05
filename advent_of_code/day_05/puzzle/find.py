"""find module"""
import sys
from typing import List, Tuple

from .parse import MappingRange


def find_value(value, mappings: List[MappingRange]) -> Tuple[int, int]:
    """finds value in given mapping

    Args:
        value (_type_): value to look for
        mappings (List[MappingRange]): mapping lists to search

    Returns:
        Tuple[int, int]: returns value, and range to the next mapping
    """
    range_of_mapping = sys.maxsize
    for mapping in mappings:
        difference = mapping.source - value

        if difference > 0:
            min(range_of_mapping, difference)

        if value >= mapping.source and value <= mapping.source + mapping.length - 1:
            return (
                mapping.destination + value - mapping.source,
                mapping.source - value + mapping.length - 1
            )

    return value, range_of_mapping
