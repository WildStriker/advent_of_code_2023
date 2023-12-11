"""parse module"""
from typing import Set, Tuple


def parse_input(input_file: str, expansion: int) -> Set[Tuple[int, int]]:
    """parse input file and returns mapping coordinates of all galaxies

    Args:
        input_file (str): input file to parse
        expansion (int): how much to expand each row and column by

    Returns:
        Set[Tuple[int, int]]: mapping of galaxy coordinates
    """

    lines = open(input_file, encoding="utf-8").read().splitlines()

    rows_to_expands = set()
    columns_to_expand = set()

    for index, line in enumerate(lines):
        if "#" in line:
            continue

        rows_to_expands.add(index)

    total_columns = len(lines[0])
    for column in range(total_columns):
        is_empty = True
        for row, line in enumerate(lines):
            current_space = line[column]

            if current_space != ".":
                is_empty = False
                break

        if is_empty:
            columns_to_expand.add(column)

    galaxy_mapping = set()

    row_offset = 0
    galaxy_count = 0
    for row, line in enumerate(lines):
        if row in rows_to_expands:
            row_offset += expansion - 1
            continue

        column_offset = 0
        for column in range(total_columns):
            if column in columns_to_expand:
                column_offset += expansion - 1
                continue

            location = (column+column_offset, row+row_offset)
            space = lines[row][column]

            if space != ".":
                galaxy_count += 1
                galaxy_mapping.add(location)

    return galaxy_mapping
