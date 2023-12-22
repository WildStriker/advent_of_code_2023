"""gravity module"""
from typing import List, Set, Tuple

from .parse import Cube

X_POSITION = 0
Y_POSITION = 1
Z_POSITION = 2


def apply_gravity(cubes: List[Cube]) -> Tuple[Set[int], Set[int], int]:
    """apply gravity to a given list of cubes

    Args:
        cubes (List[Cube]): cubes to apply gravity to

    Returns:
        Tuple[Set[int],Set[int], int]: returns a mapping of:
                            cubes that are supporting cubes
                            cubes thats are being supported by other cubes
                            total count of cube "falls"

    """

    fall_count = 0

    cube_supports = {}
    is_supported_by = {}

    cubes.sort(key=lambda cube: (cube.end[Z_POSITION]))

    for sorted_current_index, cube in enumerate(cubes):
        # cube is already at ground level
        if cube.start[Z_POSITION] == 1:
            continue

        cubes.sort(key=lambda cube: (cube.end[Z_POSITION]))

        sorted_support_cube_index = sorted_current_index
        is_currently_supported = False
        while True:
            sorted_support_cube_index -= 1

            # all support checks checked
            if sorted_support_cube_index < 0:
                # set the cube on the ground if nothing is supporting it
                if not is_currently_supported:
                    diff = cube.end[Z_POSITION] - cube.start[Z_POSITION]
                    cube.start[Z_POSITION] = 1
                    cube.end[Z_POSITION] = cube.start[Z_POSITION] + diff
                    fall_count += 1
                break

            possible_support = cubes[sorted_support_cube_index]

            # skip cubes on the same level, these shouldnt intersect?
            # or if start of this cube is alredy before the end of the next cube
            if cube.start[Z_POSITION] <= possible_support.end[Z_POSITION]:
                continue

            # this next cube is not on the same level as another cube currently supporting this
            elif (
                is_currently_supported
                and cube.start[Z_POSITION] != possible_support.end[Z_POSITION] + 1
            ):
                break

            # check if the cube could sit on the potential support cube
            if (
                (
                    possible_support.end[X_POSITION] >= cube.start[X_POSITION]
                    and possible_support.start[X_POSITION] <= cube.end[X_POSITION]
                )
                and
                (
                    possible_support.end[Y_POSITION] >= cube.start[Y_POSITION]
                    and possible_support.start[Y_POSITION] <= cube.end[Y_POSITION]
                )
            ):

                # drop the cube down to the next possible support cubee
                if cube.start[Z_POSITION] != possible_support.end[Z_POSITION] + 1:
                    diff = cube.end[Z_POSITION] - cube.start[Z_POSITION]
                    cube.start[Z_POSITION] = possible_support.end[Z_POSITION] + 1
                    cube.end[Z_POSITION] = cube.start[Z_POSITION] + diff
                    fall_count += 1

                # track cubes being supported and supporting other cubes
                if cube.index not in is_supported_by:
                    is_supported_by[cube.index] = set()
                is_supported_by[cube.index].add(possible_support.index)

                if possible_support.index not in cube_supports:
                    cube_supports[possible_support.index] = set()
                cube_supports[possible_support.index].add(cube.index)

                is_currently_supported = True

    return cube_supports, is_supported_by, fall_count


def get_removeable_cubes(
    cubes: List[Cube],
    cube_supports: Set[int],
    is_supported_by: Set[int],
) -> Set[int]:
    """finds cubes that are removeable from the stack without causing other cubes to "fall"

    Args:
        cubes (List[Cube]): list of cubes that has graity applied
        cube_supports (Set[int]): cubes that are supporting other cubes
        is_supported_by (Set[int]): cubes that are supported by other cubes

    Returns:
        Set[int]: set of removable cubes
    """
    can_be_remove = set()
    for cube in cubes:
        if not cube.index in cube_supports:
            can_be_remove.add(cube.index)
            continue

        supported_cubes = cube_supports[cube.index]

        can_remove = True
        for supported_cube in supported_cubes:
            supported_by = is_supported_by[supported_cube]
            if len(supported_by) == 1:
                can_remove = False
                break

        if can_remove:
            can_be_remove.add(cube.index)

    return can_be_remove
