"""trace module"""
from typing import Dict, Tuple

from .parse import ENTRANCE_CONNECTIONS, Direction, Map


def get_pipe_loop(mapping: Map) -> Dict[Tuple[int, int], Direction]:
    """given Map object, returns a mapping of the pipe loop (all connected pipes)

    Args:
        mapping (Map): mapping object to find loop in

    Returns:
        Dict[Tuple[int,int], Direction]: the loop coordinates and pipe directions
    """

    current_location = mapping.starting_point
    entrace_direction = list(mapping.pipes[mapping.starting_point])[1]
    pipe_loop = {}
    while True:
        pipe_loop[current_location] = mapping.pipes[current_location]
        current_location, entrace_direction = _get_next_pipe(
            mapping,
            current_location,
            entrace_direction,
        )

        if current_location == mapping.starting_point:
            break

    return pipe_loop


def _get_next_pipe(
    mapping: Map,
    location: Tuple[int, int],
    exit_direction: Direction,
) -> Tuple[Tuple[int, int], Direction]:
    entrance = ENTRANCE_CONNECTIONS[exit_direction]

    current_position = (
        location[0] + entrance.offset[0],
        location[1] + entrance.offset[1],
    )

    current_pipe = mapping.pipes[current_position]

    for direction in current_pipe:
        if direction != entrance.entrance:
            return current_position, direction
