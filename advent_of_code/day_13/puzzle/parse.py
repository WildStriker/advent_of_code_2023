"""parse module"""
from dataclasses import dataclass
from typing import List


@dataclass
class Reflection:
    """Reflection mapping by row and columns"""
    by_row: List[List[str]]
    by_column: List[List[str]]


def _to_columns(by_row):
    by_column = []
    for _ in by_row[0]:
        by_column.append([])

    for row in by_row:
        for index, column in enumerate(row):
            by_column[index].append(column)

    return by_column


def parse_input(input_file: str) -> List[Reflection]:
    """parse input file into usable reflection maps

    Args:
        input_file (str): input to parse

    Returns:
        List[Reflection]: reflection mappings
    """

    reflections = []
    with open(input_file, encoding="utf-8") as file_input:
        by_row = []
        for line in file_input:
            line = line.strip()
            if not line:
                reflections.append(
                    Reflection(by_row, _to_columns(by_row))
                )
                by_row = []
                continue

            by_row.append([*line,])

        reflections.append(
            Reflection(by_row, _to_columns(by_row))
        )

    return reflections
