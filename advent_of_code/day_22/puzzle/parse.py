"""parse module"""
from dataclasses import dataclass
from typing import List
@dataclass
class Cube:
    index: int
    start: List[int]
    end: List[int]

def parse_input(input_file: str):
    """TODO"""

    cubes = []
    with open(input_file, encoding="utf-8") as file_input:
        for index, line in enumerate(file_input):
            start, end = line.strip().split("~")

            start = list(map(int, start.split(",")))
            end = list(map(int, end.split(",")))

            cubes.append(
                Cube(
                    index,
                    start,
                    end,
                )
            )


    return cubes