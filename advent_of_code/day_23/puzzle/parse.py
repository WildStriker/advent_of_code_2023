"""parse module"""
from dataclasses import dataclass
import enum
from typing import Tuple, Dict


class MapTile(enum.Enum):
    """Map Tiles"""
    PATH = 0
    NORTH_SLOPE = 1
    EAST_SLOPE = 2
    SOUTH_SLOPE = 3
    WEST_SLOPE = 4


TILE_MAP = {
    ".": MapTile.PATH,
    "^": MapTile.NORTH_SLOPE,
    ">": MapTile.EAST_SLOPE,
    "v": MapTile.SOUTH_SLOPE,
    "<": MapTile.WEST_SLOPE,
}


@dataclass
class Map:
    """Map Object containing paths and start / end locations"""
    start_location: Tuple[int, int]
    destination_location: Tuple[int, int]

    paths: Dict[Tuple[int, int], MapTile]


def parse_input(input_file: str) -> Map:
    """parse into file into a Map object

    Args:
        input_file (str): input file to parse

    Raises:
        ValueError: raised if start or desintation locations could not be found

    Returns:
        Map: _description_
    """

    rows = open(input_file, encoding="utf-8").read().splitlines()

    paths = {}

    # get the starting and ending locations
    start_location = None
    for index, tile in enumerate(rows[0]):
        if tile != "#":
            start_location = (0, index)
            paths[start_location] = MapTile.PATH
            break

    if not start_location:
        raise ValueError("Expected to find an opening path!")

    destination_location = None
    for index, tile in enumerate(rows[-1]):
        if tile != "#":
            destination_location = (len(rows) - 1, index)
            paths[destination_location] = MapTile.PATH
            break

    if not destination_location:
        raise ValueError("Expected to find an ending path!")

    # map out the rest of the paths
    for row_index, row in enumerate(rows[1:-1], 1):
        for column_index, tile in enumerate(row):
            if tile == "#":
                continue

            map_tile = TILE_MAP[tile]
            location = (row_index, column_index)

            paths[location] = map_tile

    return Map(start_location, destination_location, paths)
