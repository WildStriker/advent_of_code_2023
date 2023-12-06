"""Part 1 Module"""
from .acceleration import get_accelerations
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    races = parse_input(file_input, False)

    result = 1
    for race in races:
        longest_acceleration_time, shortest_acceleration_time = get_accelerations(
            race
        )

        result *= longest_acceleration_time - shortest_acceleration_time + 1

    return result
