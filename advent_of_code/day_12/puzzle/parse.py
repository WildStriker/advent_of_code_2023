"""parse module"""
import functools
from dataclasses import dataclass
from typing import List


@dataclass
class Spring:
    """Spring data"""
    pattern: str
    values: List[int]
    outcomes: int


@functools.lru_cache
def count_outcomes(pattern: str, values: List[int], current_count: int = 0) -> int:
    """count all possible outcomes

    Args:
        pattern (str): pattern to evaluate
        values (List[int]): list of expected groups of numbers
        current_count (int, optional): current count to compare with first value in values.
                                       Defaults to 0.

    Returns:
        int: total solutions founds
    """
    if not values:
        return "#" not in pattern

    if not pattern:
        return values[0] == current_count and len(values) == 1

    outcomes = 0

    possible = pattern[0]
    if possible == "?":
        possible = "#."

    for char in possible:
        if char == "#":
            if current_count < values[0]:
                outcomes += count_outcomes(
                    pattern[1:],
                    values,
                    current_count + 1,
                )
            continue

        # "." char

        # count completed
        if values and values[0] == current_count:
            outcomes += count_outcomes(pattern[1:], values[1:])
            continue

        # keep searching if not currently counting
        if not current_count:
            outcomes += count_outcomes(pattern[1:], values)

    return outcomes


def parse_input(input_file: str, unfold: bool) -> List[Spring]:
    """Parse input file into list of springs with possible outcomes

    Args:
        input_file (str): input file to parse
        unfold (bool): if true, will unfold pattern into a larger set

    Returns:
        List[Spring]: list of springs with outcomes
    """

    springs = []
    with open(input_file, encoding="utf-8") as file_input:
        for line in file_input:
            pattern, values = line.strip().split()
            values = tuple(map(int, values.split(",")))

            if unfold:
                pattern = "?".join((pattern, ) * 5)
                values *= 5

            outcomes = count_outcomes(pattern, values)

            springs.append(Spring(pattern, values, outcomes))

    return springs
