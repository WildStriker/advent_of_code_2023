"""Part 2 Module"""
import copy

from .gravity import apply_gravity, get_removeable_cubes
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    cubes = parse_input(file_input)

    cube_supports, is_supported_by, _ = apply_gravity(cubes)

    can_be_remove = get_removeable_cubes(cubes, cube_supports, is_supported_by)

    total_falls = 0
    for index, cube in enumerate(cubes):
        if cube.index in can_be_remove:
            continue
        removed_cube_stack = copy.deepcopy(cubes[:index] + cubes[index+1:])

        _, _, fall_count = apply_gravity(removed_cube_stack)
        total_falls += fall_count

    return total_falls
