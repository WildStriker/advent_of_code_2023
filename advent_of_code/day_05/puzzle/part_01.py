"""Part 1 Module"""
import sys

from .find import find_value
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    results = parse_input(file_input)

    lowest = sys.maxsize
    for seed in results.seeds:
        soil, _ = find_value(seed, results.seed_to_soil)
        fertilizer, _ = find_value(soil, results.soil_to_fertilizer)
        water, _ = find_value(fertilizer, results.fertilizer_to_water)
        light, _ = find_value(water, results.water_to_light)
        temperature, _ = find_value(light, results.light_to_temperature)
        humidity, _ = find_value(temperature, results.temperature_to_huimidity)
        location, _ = find_value(humidity, results.humidity_to_location)

        lowest = min(lowest, location)

    return lowest
