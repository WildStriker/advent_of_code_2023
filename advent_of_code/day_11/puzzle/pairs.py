"""pairs module"""
from typing import Set, Tuple


def get_total_pair_distances(galaxy_mapping: Set[Tuple[int, int]]) -> int:
    """gets the total distance between all pairs

    Args:
        galaxy_mapping (Set[Tuple[int, int]]): _description_

    Returns:
        int: all total difference between each pair
    """
    total = 0
    while len(galaxy_mapping) > 1:
        coord = galaxy_mapping.pop()

        for other_coord in galaxy_mapping:
            # Taxicab geometry calculations
            distance = (
                abs(coord[0] - other_coord[0])
                + abs(coord[1] - other_coord[1])
            )
            total += distance

    return total
