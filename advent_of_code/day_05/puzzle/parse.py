"""parse module"""

from dataclasses import dataclass
from typing import List


@dataclass
class MappingRange:
    """Mapping Range info"""
    source: int
    destination: int
    length: int


@dataclass
class Mappings:
    """seed list and collection of mappings"""
    seeds: List[int]
    seed_to_soil: List[MappingRange]
    soil_to_fertilizer: List[MappingRange]
    fertilizer_to_water: List[MappingRange]
    water_to_light: List[MappingRange]
    light_to_temperature: List[MappingRange]
    temperature_to_huimidity: List[MappingRange]
    humidity_to_location: List[MappingRange]


def _map_range(file_input) -> List[MappingRange]:
    _ = next(file_input)

    mappings = []
    for line in file_input:
        if not line.strip():
            break
        destination, source, range_to_map = map(
            int,
            line.split()
        )

        mappings.append(MappingRange(source, destination, range_to_map))

    return mappings


def parse_input(input_file: str) -> Mappings:
    """parse input file and returns mapping instructions

    Args:
        input_file (str): input file to process

    Returns:
        Mappings: mapping file with starting seeds and mapping ranges
    """
    with open(input_file, encoding="utf-8") as file_input:
        seeds = map(int, next(file_input).split(":")[1].split())

        _ = next(file_input)

        seed_to_soil = _map_range(file_input)
        soil_to_fertilizer = _map_range(file_input)
        fertilizer_to_water = _map_range(file_input)
        water_to_light = _map_range(file_input)
        light_to_temperature = _map_range(file_input)
        temperature_to_huimidity = _map_range(file_input)
        humiidity_to_location = _map_range(file_input)

    return Mappings(
        seeds,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_huimidity,
        humiidity_to_location,
    )
