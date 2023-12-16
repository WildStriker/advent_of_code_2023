"""parse module"""
import enum
from typing import List


class TileType(enum.Enum):
    """Tile Type"""
    EMPTY = 0
    VERTICAL_SPLITER = 1
    HORIZONTAL_SPLITER = 2
    NORTH_EAST_MIRROR = 3
    NORTH_WEST_MIRROR = 4

def parse_input(input_file: str) -> List[List[TileType]]:
    """parse input file into a grid of tile types

    Args:
        input_file (str): input file to parse

    Returns:
        List[List[TileType]]: usable grid format
    """
    grid = []
    with open(input_file, encoding="utf-8") as file_input:
        for line in file_input:
            row = []
            grid.append(row)
            for character in line.strip():
                if character == "|":
                    tile_type = TileType.VERTICAL_SPLITER
                elif character == "-":
                    tile_type = TileType.HORIZONTAL_SPLITER
                elif character == "/":
                    tile_type = TileType.NORTH_EAST_MIRROR
                elif character == "\\":
                    tile_type = TileType.NORTH_WEST_MIRROR
                else:
                    tile_type = TileType.EMPTY

                row.append(tile_type)

    return grid
