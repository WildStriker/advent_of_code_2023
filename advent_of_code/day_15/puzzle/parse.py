"""parse module"""
from typing import List


def parse_input(input_file: str) -> List[str]:
    """parse input file into hash list

    Args:
        input_file (str): input file to parse

    Returns:
        List[str]: list of hashes
    """

    hashes = []
    with open(input_file, encoding="utf-8") as file_input:
        for line in file_input:
            line_hashes = line.strip().split(",")
            hashes.extend(line_hashes)

    return hashes
