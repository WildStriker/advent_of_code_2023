"""Part 2 Module"""
from .acceleration import get_accelerations
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    race = parse_input(file_input, True)[0]

    longest_acceleration_time, shortest_acceleration_time = get_accelerations(
        race
    )

    return longest_acceleration_time - shortest_acceleration_time + 1
