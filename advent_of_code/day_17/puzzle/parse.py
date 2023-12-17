"""parse module"""
from typing import Dict, Tuple


def parse_input(input_file: str) -> Tuple[Dict[Tuple[int, int], int], Tuple[int, int]]:
    """parse input file to mapping of all coordinates of potential heat loss

    Args:
        input_file (str): input file

    Returns:
        Tuple[Dict[Tuple[int, int], int], Tuple[int, int]]: heat loss coord mapping,
                                                            and ending coordinate
    """

    city_blocks = {}
    coords = (0, 0)
    with open(input_file, encoding="utf-8") as file_input:
        for row, line in enumerate(file_input):
            for column, character in enumerate(line.strip()):
                coords = (row, column)

                heat_loss = int(character)
                city_blocks[coords] = heat_loss

    return city_blocks, coords
