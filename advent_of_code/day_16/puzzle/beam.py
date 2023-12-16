"""beam module"""
import enum
from typing import List, Tuple

from .parse import TileType


class Direction(enum.Enum):
    """Travel Direction"""
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3


def trace_beam(
    grid: List[List[TileType]],
    beam_ends: List[Tuple[Tuple[int, int], Direction]],
) -> int:
    """trace all beam paths and calculate totals

    Args:
        grid (List[List[TileType]]): grid that beam will traverse
        beam_ends (List[Tuple[Tuple[int, int], Direction]]): all possible beam locations

    Returns:
        int: total energized tiles
    """
    total_rows = len(grid)
    total_columns = len(grid[0])

    all_traveled = set()

    is_energized = set()

    while beam_ends:
        traveled = beam_ends.pop()
        if traveled in all_traveled:
            continue

        all_traveled.add(traveled)

        beam_coord, direction = traveled
        # no where left for the beam to go
        if (
            beam_coord[0] < 0
            or beam_coord[1] < 0
            or beam_coord[0] >= total_rows
            or beam_coord[1] >= total_columns
        ):
            continue

        this_tile = grid[beam_coord[0]][beam_coord[1]]
        is_energized.add(beam_coord)

        if this_tile == TileType.EMPTY:
            if direction == Direction.NORTH:
                next_coord = (beam_coord[0] - 1, beam_coord[1])
            elif direction == Direction.SOUTH:
                next_coord = (beam_coord[0] + 1, beam_coord[1])
            elif direction == Direction.EAST:
                next_coord = (beam_coord[0], beam_coord[1] + 1)
            elif direction == Direction.WEST:
                next_coord = (beam_coord[0], beam_coord[1] - 1)

            beam_ends.append((next_coord, direction))
            continue

        if this_tile == TileType.NORTH_EAST_MIRROR:
            if direction == Direction.NORTH:
                next_coord = (beam_coord[0], beam_coord[1] + 1)
                next_direction = Direction.EAST
            elif direction == Direction.SOUTH:
                next_coord = (beam_coord[0], beam_coord[1] - 1)
                next_direction = Direction.WEST
            elif direction == Direction.EAST:
                next_coord = (beam_coord[0] - 1, beam_coord[1])
                next_direction = Direction.NORTH
            elif direction == Direction.WEST:
                next_coord = (beam_coord[0] + 1, beam_coord[1])
                next_direction = Direction.SOUTH

            beam_ends.append((next_coord, next_direction))
            continue

        if this_tile == TileType.NORTH_WEST_MIRROR:
            if direction == Direction.NORTH:
                next_coord = (beam_coord[0], beam_coord[1] - 1)
                next_direction = Direction.WEST
            elif direction == Direction.SOUTH:
                next_coord = (beam_coord[0], beam_coord[1] + 1)
                next_direction = Direction.EAST
            elif direction == Direction.EAST:
                next_coord = (beam_coord[0] + 1, beam_coord[1])
                next_direction = Direction.SOUTH
            elif direction == Direction.WEST:
                next_coord = (beam_coord[0] - 1, beam_coord[1])
                next_direction = Direction.NORTH

            beam_ends.append((next_coord, next_direction))
            continue

        if this_tile == TileType.VERTICAL_SPLITER:
            if direction == Direction.NORTH:
                next_coord = (beam_coord[0] - 1, beam_coord[1])
                beam_ends.append((next_coord, direction))
            elif direction == Direction.SOUTH:
                next_coord = (beam_coord[0] + 1, beam_coord[1])
                beam_ends.append((next_coord, direction))
            elif direction == Direction.EAST or direction == Direction.WEST:
                next_coord = (beam_coord[0] - 1, beam_coord[1])
                beam_ends.append((next_coord, Direction.NORTH))
                next_coord = (beam_coord[0] + 1, beam_coord[1])
                beam_ends.append((next_coord, Direction.SOUTH))

            continue

        if this_tile == TileType.HORIZONTAL_SPLITER:
            if direction == Direction.NORTH or direction == Direction.SOUTH:
                next_coord = (beam_coord[0], beam_coord[1] - 1)
                beam_ends.append((next_coord, Direction.WEST))
                next_coord = (beam_coord[0], beam_coord[1] + 1)
                beam_ends.append((next_coord, Direction.EAST))
            elif direction == Direction.EAST:
                next_coord = (beam_coord[0], beam_coord[1] + 1)
                beam_ends.append((next_coord, direction))
            elif direction == Direction.WEST:
                next_coord = (beam_coord[0], beam_coord[1] - 1)
                beam_ends.append((next_coord, direction))

            continue

    totals = 0
    for row in range(total_rows):
        for column in range(total_columns):
            if (row, column) in is_energized:
                totals += 1

    return totals
