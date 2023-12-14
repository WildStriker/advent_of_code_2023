"""move module"""
from typing import List, Tuple


def _get_movable_round(
    platform: List[List[str]],
    start_coords: Tuple[int, int],
    offset: Tuple[int, int],
):
    new_coords = (
        start_coords[0] + offset[0],
        start_coords[1] + offset[1],
    )

    tile = platform[start_coords[0]][start_coords[1]]
    if tile == ".":
        last_known_free = start_coords
    else:
        last_known_free = None

    while True:
        if (
            new_coords[0] >= len(platform)
            or new_coords[1] >= len(platform[0])
            or new_coords[0] < 0
            or new_coords[1] < 0
        ):
            return None

        tile = platform[new_coords[0]][new_coords[1]]
        if last_known_free is None and tile == ".":
            last_known_free = new_coords
        elif tile == "#":
            last_known_free = None
        elif tile == "O" and last_known_free:
            return new_coords, last_known_free

        new_coords = (
            new_coords[0] + offset[0],
            new_coords[1] + offset[1],
        )

    return None


def move_free(platform: List[List[str]], start_coords: Tuple[int, int], offset: Tuple[int, int]):
    """moves all round rocks to the next available tile

    Args:
        platform (List[List[str]]): platform to search
        start_coords (Tuple[int, int]): starting location
        offset (Tuple[int, int]): offset is movement
        (in the opposite direct) to search for available round rocks / free tiles
    """
    round_rock = start_coords
    while True:
        found = _get_movable_round(platform, round_rock, offset)

        if found is None:
            return

        round_rock, free_space = found

        platform[free_space[0]][free_space[1]] = "O"
        platform[round_rock[0]][round_rock[1]] = "."

        round_rock = (
            free_space[0] + offset[0],
            free_space[1] + offset[1],
        )
