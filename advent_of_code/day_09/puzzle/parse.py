"""parse module"""
from typing import List


def parse_input(input_file: str) -> List[List[int]]:
    """parse input file into history of sequences

    Args:
        input_file (str): input file to parse

    Returns:
        List[List[int]]: history sequence data
    """

    history = []
    with open(input_file, encoding="utf-8") as file_input:
        for line in file_input:
            history.append(
                list(map(int, line.split()))
            )

    return history
