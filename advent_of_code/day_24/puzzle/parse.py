"""parse module"""
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Hailstone:
    """Hailstone data"""
    start_position: Tuple[int, int, int]
    velocity: Tuple[int, int, int]
    end_position: Tuple[int, int, int]

    def slope_2d(self) -> float:
        """calculates slope for line intersect

        Returns:
            float: calculated slope value
        """
        return (
            (self.end_position[1] - self.start_position[1])
            /
            (self.end_position[0] - self.start_position[0])
        )

    def y_intercept_2d(self, slope: float) -> float:
        """calculates Y Intercept, used in line interesect calculations

        Args:
            slope (float): previously calculated slope

        Returns:
            float: caculated intercept value
        """
        return self.start_position[1] - slope * self.start_position[0]

    def line_intersect_2d(self, other_hailstone: 'Hailstone') -> Tuple[int, int] | None:
        """check if two lines intersect on X and Y axis, Z axis is not considered

        Args:
            other_hailstone (Hailstone): other hailstone to compare insections

        Returns:
            Tuple[int, int] | None: returns the found coordinates, None if it does not
        """
        self_slope = self.slope_2d()
        other_slope = other_hailstone.slope_2d()
        if self_slope == other_slope:
            return None

        self_y_intercept = self.y_intercept_2d(self_slope)
        x = (other_hailstone.y_intercept_2d(other_slope) -
             self_y_intercept) / (self_slope - other_slope)

        y = self_slope * x + self_y_intercept
        return x, y

    def is_past(self, coords: Tuple[int, ...]) -> bool:
        """check if given coords exists in the past

        Args:
            coords (Tuple[int, ...]): coordinates (could be 2d / 3d)

        Returns:
            bool: True if found in the past
        """

        for index, coord in enumerate(coords):
            diff = self.start_position[index] - coord

            if diff < 0 and self.velocity[index] < 0:
                return True

            if diff > 0 and self.velocity[index] > 0:
                return True

        return False


def parse_input(input_file: str) -> List[Hailstone]:
    """parse into file into a list of Hailstone

    Args:
        input_file (str): input file to parse

    Returns:
        List[Hailstone]: list of Hailstone
    """
    hailstones = []
    with open(input_file, encoding="utf-8") as file_input:
        for line in file_input:
            position, velocity = line.strip().split(" @ ")
            position = tuple(map(int, position.split(", ")))
            velocity = tuple(map(int, velocity.split(", ")))

            end_position = (
                position[0] + velocity[0],
                position[1] + velocity[1],
                position[2] + velocity[2],
            )

            hailstones.append(Hailstone(position, velocity, end_position))

    return hailstones
