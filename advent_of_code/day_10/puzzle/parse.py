"""parse module"""
import enum
from dataclasses import dataclass
from typing import Dict, Tuple


class Direction(enum.Flag):
    """Direction flags for each pipe"""
    START = enum.auto()
    NORTH = enum.auto()
    SOUTH = enum.auto()
    EAST = enum.auto()
    WEST = enum.auto()


@dataclass
class Map:
    """Map object"""
    starting_point: Tuple[int, int]
    pipes: Dict[Tuple[int, int], Direction]
    total_rows: int
    total_columns: int


@dataclass
class Entrance:
    """Entrance and its entry offset"""
    offset: Tuple[int, int]
    entrance: Direction


MAPPING = {
    "|": Direction.NORTH | Direction.SOUTH,
    "-": Direction.EAST | Direction.WEST,
    "L": Direction.NORTH | Direction.EAST,
    "J": Direction.NORTH | Direction.WEST,
    "7": Direction.SOUTH | Direction.WEST,
    "F": Direction.SOUTH | Direction.EAST,
}

ENTRANCE_CONNECTIONS = {
    Direction.NORTH: Entrance((0, -1), Direction.SOUTH),
    Direction.SOUTH: Entrance((0, 1), Direction.NORTH),
    Direction.EAST: Entrance((1, 0), Direction.WEST),
    Direction.WEST: Entrance((-1, 0), Direction.EAST),
}


def parse_input(input_file: str) -> Map:
    """returns a parsed Map object that contains all pipes, starting location and map size

    Args:
        input_file (str): input file to parse

    Returns:
        Map: parsed map object
    """

    lines = open(input_file, encoding="utf-8").read().splitlines()
    total_rows = len(lines)
    total_columns = len(lines[0])

    starting_point = None
    pipes = {}
    for row, line in enumerate(lines):

        for column, character in enumerate(line):

            if character == ".":
                continue

            location = (column, row)

            if character == "S":
                starting_point = location
                continue

            pipes[location] = MAPPING[character]

    pipe = _get_staritng_pipe(starting_point, pipes)
    pipes[starting_point] = pipe

    return Map(starting_point, pipes, total_rows, total_columns)


def _get_staritng_pipe(starting_point, pipes):

    directions = Direction.START
    for exit_direction, entrance in ENTRANCE_CONNECTIONS.items():
        current_position = (
            starting_point[0] + entrance.offset[0],
            starting_point[1] + entrance.offset[1],
        )

        if current_position not in pipes:
            continue

        current_pipe = pipes[current_position]
        if entrance.entrance in current_pipe:
            directions |= exit_direction

    return directions
