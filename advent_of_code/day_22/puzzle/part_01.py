"""Part 1 Module"""
from .gravity import apply_gravity, get_removeable_cubes
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""
    # TODO

    cubes = parse_input(file_input)

    cube_supports, is_supported_by, _ = apply_gravity(cubes)

    can_be_remove = get_removeable_cubes(cubes, cube_supports, is_supported_by)

    return len(can_be_remove)
