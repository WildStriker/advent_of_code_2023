"""parse module"""
from typing import List

def parse_input(input_file: str) -> List[List[str]]:
    """parse input file into matrix of characters

    Args:
        input_file (str): inputfile

    Returns:
        List[List[str]]: platform / char matrix
    """
    platform = []
    with open(input_file, encoding="utf-8") as file_input:
        for line in file_input:
            platform.append([*line.strip(),])

    return platform
