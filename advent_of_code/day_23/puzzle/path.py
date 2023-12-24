"""shortest module"""
import copy
import enum
import queue
from typing import List, Tuple

from .parse import Map, MapTile


class Direction(enum.Enum):
    """Direction Crucible is currently traveling / facing"""
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3


def _get_neighbors(
    original_coords: Tuple[int, int],
    current_direction: Direction,
    map_data: Map,
) -> List[Tuple[Tuple[int, int], MapTile]]:
    """Returns all walkable neighbours

    Returns:
        List[Tuple[int, int]]: list of coodinates to return
    """
    neighbors = []

    up_coord = (original_coords[0]-1, original_coords[1])
    if current_direction != Direction.SOUTH and up_coord in map_data.paths:
        neighbors.append((up_coord, Direction.NORTH, map_data.paths[up_coord]))

    left_coord = (original_coords[0], original_coords[1] - 1)
    if current_direction != Direction.EAST and left_coord in map_data.paths:
        neighbors.append((left_coord, Direction.WEST,
                         map_data.paths[left_coord]))

    right_coord = (original_coords[0], original_coords[1] + 1)
    if current_direction != Direction.WEST and right_coord in map_data.paths:
        neighbors.append((right_coord, Direction.EAST,
                         map_data.paths[right_coord]))

    down_coord = (original_coords[0]+1, original_coords[1])
    if current_direction != Direction.NORTH and down_coord in map_data.paths:
        neighbors.append((down_coord, Direction.SOUTH,
                         map_data.paths[down_coord]))

    return neighbors


def get_longest_path_steps(
    map_data: Map,
    can_climb_slope: bool,
) -> int:
    """gets the total steps it would take to travel the longest path

    Args:
        map_data (Map): map to find longest path from start to finish
        can_climb_slope (bool): if true slopes are climable and can be passed in either direction

    Returns:
        int: max step count to reach the end
    """

    frontier = queue.Queue()

    start_state = (map_data.start_location, Direction.SOUTH)
    frontier.put(start_state)

    graph_map = {}
    while not frontier.empty():
        current_position, current_direction = frontier.get()

        result = _get_next_node(
            current_position,
            current_direction,
            map_data,
            can_climb_slope,
        )

        # this path cannot be traveled on in this direction
        if not result:
            continue

        next_position, neighbors, steps, has_slope = result

        if current_position not in graph_map:
            graph_map[current_position] = {}

        if next_position not in graph_map:
            graph_map[next_position] = {}

            for _neighbor, neighbor_direction, _tile in neighbors:

                start_state = (next_position, neighbor_direction)
                frontier.put(start_state)

        graph_map[current_position][next_position] = steps
        # we can only map both ways if there is no slopes
        if not has_slope:
            graph_map[next_position][current_position] = steps

    max_steps = _get_max_steps(
        graph_map,
        map_data.start_location,
        map_data.destination_location,
        0,
        set(),
    )
    return max_steps


def _get_max_steps(graph_map, target, end, counting_steps, traveled):
    if target == end:
        return counting_steps

    max_steps = 0
    traveled.add(target)
    for next_node, steps in graph_map[target].items():
        if next_node in traveled:
            continue

        max_steps = max(max_steps, _get_max_steps(
            graph_map, next_node, end, counting_steps + steps, copy.copy(traveled)))

    return max_steps


def _get_next_coordinate(current_position: Tuple[int, int], current_direction: Direction):
    if current_direction == Direction.NORTH:
        next_coord = (current_position[0]-1, current_position[1])
    elif current_direction == Direction.WEST:
        next_coord = (current_position[0], current_position[1] - 1)
    elif current_direction == Direction.EAST:
        next_coord = (current_position[0], current_position[1] + 1)
    else:
        next_coord = (current_position[0]+1, current_position[1])

    return next_coord


def _get_next_node(
    current_position: Tuple[int, int],
    current_direction: Direction,
    map_data: Map,
    can_climb_slope: bool,
):
    has_slope = False
    steps = 0

    next_coord = _get_next_coordinate(
        current_position,
        current_direction,
    )

    next_direction = current_direction
    while True:
        steps += 1
        neighbors = _get_neighbors(
            next_coord,
            next_direction,
            map_data,
        )

        if len(neighbors) != 1:
            return next_coord, neighbors, steps, has_slope

        next_coord, next_direction, tile = neighbors[0]

        if not can_climb_slope:
            while tile != MapTile.PATH:
                has_slope = True

                # This path cannot be traversed if coming from the opposite direction!
                if (
                    tile == MapTile.NORTH_SLOPE and next_direction == Direction.SOUTH
                    or tile == MapTile.WEST_SLOPE and next_direction == Direction.EAST
                    or tile == MapTile.EAST_SLOPE and next_direction == Direction.WEST
                    or tile == MapTile.SOUTH_SLOPE and next_direction == Direction.NORTH
                ):
                    return None

                if tile == MapTile.NORTH_SLOPE:
                    next_coord = (next_coord[0] - 1, next_coord[1])
                elif tile == MapTile.WEST_SLOPE:
                    next_coord = (next_coord[0], next_coord[1] - 1)
                elif tile == MapTile.EAST_SLOPE:
                    next_coord = (next_coord[0], next_coord[1] + 1)
                else:
                    next_coord = (next_coord[0] + 1, next_coord[1])

                # we can travel down this slope, so increment weight
                # and move on to the next tile
                tile = map_data.paths[next_coord]
                steps += 1
