"""area module"""
from typing import List

from .parse import Direction, Instruction


def get_area(instructions: List[Instruction]) -> int:
    """caculates the area of given dig instructions

    Args:
        instructions (List[Instruction]): instructions for dig area

    Returns:
        int: total area
    """
    current_coordinate = (0, 0)
    coordinates = []
    total = 0
    for instruction in instructions:

        if instruction.direction == Direction.UP:
            offset = (instruction.count * -1, 0)
        elif instruction.direction == Direction.DOWN:
            offset = (instruction.count * 1, 0)
        elif instruction.direction == Direction.LEFT:
            offset = (0, instruction.count * -1)
        else:
            offset = (0, instruction.count * 1)

        current_coordinate = (
            current_coordinate[0] + offset[0],
            current_coordinate[1] + offset[1]
        )
        coordinates.append(current_coordinate)
        # add outter area
        total += instruction.count

    # shoe lace formula to calculate inner area
    previous_coordinate = (0, 0)
    for coordinate in reversed(coordinates):
        calculate = previous_coordinate[0] * coordinate[1]
        calculate -= previous_coordinate[1] * coordinate[0]
        total += calculate
        previous_coordinate = coordinate

    return total // 2 + 1
