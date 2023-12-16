"""Part 2 Module"""
from .beam import Direction, trace_beam
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    grid = parse_input(file_input)

    total_rows = len(grid)
    total_columns = len(grid[0])

    best_result = 0

    # check all possible configurations starting EAST / WEST
    for row in range(total_rows):
        best_result = max(
            best_result,
            trace_beam(
                grid,
                [((row, 0), Direction.EAST)]),
        )
        best_result = max(
            best_result,
            trace_beam(
                grid,
                [
                    (
                        (row, total_columns - 1),
                        Direction.WEST,
                    )
                ]
            ),
        )

    # check all possible configurations starting NORTH / SOUTH
    for column in range(total_columns):
        best_result = max(
            best_result,
            trace_beam(
                grid,
                [((0, column), Direction.SOUTH)]
            ),
        )
        best_result = max(
            best_result,
            trace_beam(
                grid,
                [((total_rows - 1, column), Direction.NORTH)]
            ),
        )

    return best_result
