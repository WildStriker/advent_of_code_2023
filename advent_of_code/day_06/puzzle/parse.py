"""parse module"""
from dataclasses import dataclass
from typing import List


@dataclass
class Race:
    """Race info"""
    time: int
    distance: int


def parse_input(input_file: str, remove_whitespace: bool) -> List[Race]:
    """parse puzzle input and return a list of races

    Args:
        input_file (str): input file to parse
        remove_whitespace (bool): boolean flag to remove white space between input numbers

    Returns:
        List[Race]: list of races
    """
    races = []
    with open(input_file, encoding="utf-8") as file_input:
        times = next(file_input)
        distances = next(file_input)
        if remove_whitespace:
            times = times.replace(" ", "")
            distances = distances.replace(" ", "")

        times = map(int, times.split(":")[1].split())
        distances = map(int, distances.split(":")[1].split())

        for time, distance in zip(times, distances):
            races.append(Race(time, distance))

    return races
