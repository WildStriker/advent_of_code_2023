"""reflection module"""
from dataclasses import dataclass
from typing import Optional

from .parse import Reflection


@dataclass
class Found:
    """Found info"""
    is_row: bool
    index: int


def _check_reflections(visuals, left_index, right_index):
    if left_index < 0:
        return True

    if right_index >= len(visuals):
        return True

    if visuals[left_index] != visuals[right_index]:
        return False

    return _check_reflections(visuals, left_index-1, right_index + 1)


def calculate_found_reflection(found: Found) -> int:
    """calculates the value for the found reflection

    Args:
        found (Found): reflection to calculate

    Returns:
        int: calculated value
    """
    if not found:
        return 0

    if found.is_row:
        return (found.index + 1) * 100
    else:
        return found.index + 1


def find_reflection(reflection: Reflection, original_found: Found = None) -> Optional[Found]:
    """finds the reflections position

    must only have ONE result

    Args:
        reflection (Reflection): map to find reflections in
        original_found (Found, optional): if given, we do not want to consider this
                                          when finding reflections.
                                          Defaults to None.

    Returns:
        Optional[Found]: the found reflection point
    """
    already_found = False
    found = None
    for index, row in enumerate(reflection.by_row[:-1]):
        # skip this reflection we dont want to count it
        if original_found and original_found.is_row and original_found.index == index:
            continue

        next_row = reflection.by_row[index + 1]
        if row == next_row:
            reflection_found = _check_reflections(
                reflection.by_row, index - 1, index + 2)
            if reflection_found:
                if already_found:
                    return None
                already_found = True
                found = Found(True, index)

    for index, column in enumerate(reflection.by_column[:-1]):
        # skip this reflection we dont want to count it
        if original_found and not original_found.is_row and original_found.index == index:
            continue

        next_column = reflection.by_column[index + 1]
        if column == next_column:
            reflection_found = _check_reflections(
                reflection.by_column, index - 1, index + 2)
            if reflection_found:
                if already_found:
                    return None
                already_found = True
                found = Found(False, index)

    return found
