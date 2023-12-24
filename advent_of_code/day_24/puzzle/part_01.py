"""Part 1 Module"""
import itertools

from .parse import parse_input


def answer_01(file_input: str, min_range: int, max_range: int):
    """Part 1"""

    hailstones = parse_input(file_input)

    intersections = 0
    for hailstone_1, hailstone_2 in itertools.combinations(hailstones, 2):

        coords = hailstone_1.line_intersect_2d(hailstone_2)

        if not coords:
            continue

        if (
            coords[0] < min_range or coords[0] > max_range
            or coords[1] < min_range or coords[1] > max_range
        ):
            continue

        if hailstone_1.is_past(coords) or hailstone_2.is_past(coords):
            continue

        intersections += 1

    return intersections
