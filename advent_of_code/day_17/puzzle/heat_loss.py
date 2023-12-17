"""shortest module"""
import enum
import queue
from typing import Dict, Tuple, List


class Direction(enum.Enum):
    """Direction Crucible is currently traveling / facing"""
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


def _get_neighbors(
    original_coords: Tuple[int, int],
    direction: Direction,
    straight_count: int,
    min_straight: int,
    max_straight: int,
) -> List[Tuple[Tuple[int, int], Direction, int]]:
    neighbors = []

    # north
    if (
        direction in {Direction.WEST,
                      Direction.EAST} and straight_count >= min_straight
        or direction == Direction.NORTH and straight_count < max_straight
    ):
        if direction == Direction.NORTH:
            neighbor_straight_count = straight_count + 1
        else:
            neighbor_straight_count = 1
        up_coord = (original_coords[0]-1, original_coords[1])
        neighbors.append((up_coord, Direction.NORTH, neighbor_straight_count))

    # west
    if (
        direction in {Direction.NORTH,
                      Direction.SOUTH} and straight_count >= min_straight
        or direction == Direction.WEST and straight_count < max_straight
    ):
        if direction == Direction.WEST:
            neighbor_straight_count = straight_count + 1
        else:
            neighbor_straight_count = 1
        left_coord = (original_coords[0], original_coords[1] - 1)
        neighbors.append((left_coord, Direction.WEST, neighbor_straight_count))

    # east
    if (
        direction in {Direction.NORTH,
                      Direction.SOUTH} and straight_count >= min_straight
        or direction == Direction.EAST and straight_count < max_straight
    ):
        if direction == Direction.EAST:
            neighbor_straight_count = straight_count + 1
        else:
            neighbor_straight_count = 1
        right_coord = (original_coords[0], original_coords[1] + 1)
        neighbors.append(
            (right_coord, Direction.EAST, neighbor_straight_count))

    # south
    if (
        direction in {Direction.WEST,
                      Direction.EAST} and straight_count >= min_straight
        or direction == Direction.SOUTH and straight_count < max_straight
    ):
        if direction == Direction.SOUTH:
            neighbor_straight_count = straight_count + 1
        else:
            neighbor_straight_count = 1
        down_coord = (original_coords[0]+1, original_coords[1])
        neighbors.append(
            (down_coord, Direction.SOUTH, neighbor_straight_count))

    return neighbors


def get_lowest_heat_loss_path(
    start: Tuple[int, int],
    end: Tuple[int, int],
    path: Dict[Tuple[int, int], int],
    min_straight: int,
    max_straight: int,
) -> int:
    """find the path that loses the least heat

    Args:
        start (Tuple[int, int]): starting location to travel from
        end (Tuple[int, int]): target destination to get to with least amount of heat loss
        path (Dict[Tuple[int, int], int]): _description_
        min_straight (int): minimum travel required in a straight line
        max_straight (int): max travel allowe din a straight line

    Returns:
        int: least amount of heat loss found
    """
    frontier = queue.PriorityQueue()

    start_state = (start, Direction.EAST, 1)
    frontier.put((0, start_state))

    came_from = {
        start_state: None
    }
    cost_so_far = {
        start_state: 0
    }

    while not frontier.empty():
        _, current = frontier.get()

        current_position = current[0]
        direction = current[1]
        straight_count = current[2]

        if current_position == end and straight_count >= min_straight:
            return cost_so_far[current]

        for neighbor, direction, straight_count in _get_neighbors(
            current_position,
            direction,
            straight_count,
            min_straight,
            max_straight,
        ):
            if neighbor not in path:
                continue

            weight = path[neighbor]

            neighbor_state = (neighbor, direction, straight_count)
            new_cost = cost_so_far[current] + weight
            if neighbor_state not in cost_so_far or new_cost < cost_so_far[neighbor_state]:
                cost_so_far[neighbor_state] = new_cost
                priority = new_cost
                frontier.put((priority, neighbor_state))
                came_from[neighbor_state] = current
