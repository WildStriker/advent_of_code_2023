"""parse module"""
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Part:
    """Part Extract from Schematics"""
    numbers: List[int]
    symbol: str


def parse_input(input_file: str) -> Dict[Tuple[int, int], Part]:
    """Parse input file and returns a dictionary (mapping of symbol coordinates -> Part)

    coordinates is "None" is there is no symbol linking the numbers

    Args:
        input_file (str): input file to parse

    Returns:
        Dict[Tuple[int, int], Part]: parsed mapping of symbols / part numbers
    """

    matrix = open(input_file, encoding="utf-8").read().splitlines()

    total_rows = len(matrix)
    total_columns = len(matrix[0])

    parts = {}

    for row in range(total_rows):
        parsed_number = ""
        symbol = ""
        symbol_coords = None
        for column in range(total_columns):
            value = matrix[row][column]
            if not value.isdigit():
                if parsed_number:
                    if symbol_coords in parts:
                        part = parts[symbol_coords]
                        part.numbers.append(int(parsed_number))
                    else:
                        parts[symbol_coords] = Part(
                            [int(parsed_number),],
                            symbol,
                        )
                parsed_number = ""
                symbol = ""
                symbol_coords = None
                continue

            parsed_number += value
            if not symbol:
                symbol, symbol_coords = _get_symbol(
                    matrix,
                    row,
                    column,
                    total_rows,
                    total_columns,
                )

        if parsed_number:
            if parsed_number:
                if symbol_coords in parts:
                    part = parts[symbol_coords]
                    part.numbers.append(int(parsed_number))
                else:
                    parts[symbol_coords] = Part(
                        [int(parsed_number),],
                        symbol,
                    )
    return parts


def _get_symbol(matrix: List[str], row: int, column: int, total_rows: int, total_columns: int):

    min_row = row - 1
    max_row = row + 2
    min_column = column - 1
    max_column = column + 2

    for current_row in range(min_row, max_row):
        if current_row < 0 or current_row + 1 >= total_rows:
            continue

        for current_column in range(min_column, max_column):
            if (
                current_row == row and current_column == column
                or current_column < 0
                or current_column + 1 > total_columns
            ):
                continue

            # NOTE: assumption is there is only one symbol?
            value = matrix[current_row][current_column]
            if not value.isdigit() and value != ".":
                return value, (current_row, current_column)

    return "", None
