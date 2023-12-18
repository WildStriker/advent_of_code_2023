"""parse module"""
import enum
import re
from dataclasses import dataclass
from typing import List

PATTERN = re.compile("([A-Z]) ([0-9]+) \(#([0-9a-z]+)\)")


class Direction(enum.Enum):
    """direction to move"""
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


@dataclass
class Instruction:
    """digging instruction"""
    direction: Direction
    count: int


def parse_input(input_file: str, parse_hex: bool) -> List[Instruction]:
    """parse input file into usable instructions

    Args:
        input_file (str): input file to parse
        parse_hex (bool): parse hex string instead

    Returns:
        List[Instruction]: list of digging instructions
    """
    instructions = []
    with open(input_file, encoding="utf-8") as file_input:
        for line in file_input:
            direction, count, hex_value = PATTERN.search(line).groups()

            if parse_hex:
                direction = hex_value[-1]
                direction = Direction(int(direction))

                count = hex_value[:-1]
                count = int(count, 16)

            else:
                if direction == "R":
                    direction = Direction.RIGHT
                elif direction == "D":
                    direction = Direction.DOWN
                elif direction == "L":
                    direction = Direction.LEFT
                else:
                    direction = Direction.UP

                count = int(count)

            instructions.append(Instruction(direction, count))

    return instructions
