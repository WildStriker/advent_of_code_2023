"""Part 2 Module"""
from .parse import parse_input, Direction
from .trace import get_pipe_loop


def answer_02(file_input: str):
    """Part 2"""

    mapping = parse_input(file_input)

    pipe_loop = get_pipe_loop(mapping)

    # outside count
    count = 0
    for row in range(mapping.total_rows):
        for column in range(mapping.total_columns):
            location = (column, row)
            if location in pipe_loop:
                continue

            # scanning left to right
            # count how many north directions there are
            # an odd number should indicate "inside" the loop
            north_count = 0
            for loop_column in range(column):
                loop_location = (loop_column, row)
                if loop_location not in pipe_loop:
                    continue
                pipe = pipe_loop[loop_location]

                if Direction.NORTH in pipe:
                    north_count += 1

            # even counts means outside there for 0
            count += north_count % 2

    return count
