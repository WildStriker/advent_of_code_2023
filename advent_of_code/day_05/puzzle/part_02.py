"""Part 2 Module"""
import sys
from typing import Tuple

from .find import find_value
from .parse import Mappings, parse_input


def get_location_value(seed: int, range_of_seed: int, mappings: Mappings) -> Tuple[int, int]:
    """gets the location and smallest / shared range for the given seed

    Args:
        seed (int): seed to map
        range_of_seed (int): range of the seed we want to map
        mappings (Mappings): mappings to use

    Returns:
        Tuple[int, int]: the location we are mapping,
        the shared range that can still map
        seed + range to location + range without mapping changing in between
    """
    soil, range_of_soil = find_value(
        seed,
        mappings.seed_to_soil,
    )
    fertilizer, range_of_fertilizer = find_value(
        soil,
        mappings.soil_to_fertilizer,
    )
    water, range_of_water = find_value(
        fertilizer,
        mappings.fertilizer_to_water,
    )
    light, range_of_light = find_value(
        water,
        mappings.water_to_light,
    )
    temperature, range_of_temperature = find_value(
        light,
        mappings.light_to_temperature,
    )
    humidity, range_of_humidity = find_value(
        temperature,
        mappings.temperature_to_huimidity
    )
    location, range_of_location = find_value(
        humidity,
        mappings.humidity_to_location,
    )

    smallest_range = min(
        range_of_seed,
        range_of_soil,
        range_of_fertilizer,
        range_of_water,
        range_of_light,
        range_of_temperature,
        range_of_humidity,
        range_of_location,
    )

    return location, smallest_range


def answer_02(file_input: str):
    """Part 2"""

    results = parse_input(file_input)

    lowest = sys.maxsize
    seeds_and_range = iter(results.seeds)
    for seed in seeds_and_range:
        range_of_seed = next(seeds_and_range)

        offset = 0
        while offset < range_of_seed:
            location, smallest_range = get_location_value(
                seed + offset,
                range_of_seed - offset,
                results,
            )
            lowest = min(lowest, location)

            if smallest_range:
                offset += smallest_range
            else:
                offset += 1

    return lowest
