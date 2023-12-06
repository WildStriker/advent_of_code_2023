"""acceleration module"""
import math
from typing import Tuple

from .parse import Race


def get_accelerations(race: Race) -> Tuple[int, int]:
    """get the min and max acceleration times requires to achieve distance to complete the race

    Args:
        race (Race): The Race to calculate times for

    Returns:
        Tuple[int, int]: the long, and shorted acceleration time required
    """
    fastest_speed = race.time - 1
    min_time = math.ceil(race.distance // fastest_speed) - 1

    traveled_distance = 0

    while traveled_distance <= race.distance:
        min_time += 1
        useable_acceleration_time = race.time - min_time
        traveled_distance = useable_acceleration_time * min_time

    shortest_acceleration_time = min_time

    traveled_distance = 0
    max_time = useable_acceleration_time + 1
    while traveled_distance <= race.distance:
        max_time -= 1
        useable_acceleration_time = race.time - max_time
        traveled_distance = useable_acceleration_time * max_time

    longest_acceleration_time = max_time

    return longest_acceleration_time, shortest_acceleration_time
