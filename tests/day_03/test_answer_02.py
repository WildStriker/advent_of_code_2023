"""test_answer_02 module (day 3)"""
import os

from advent_of_code.day_03.puzzle.part_02 import answer_02


def test_case_1():
    """In this schematic, there are two gears.
    The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345.
    The second gear is in the lower right; its gear ratio is 451490.
    (The * adjacent to 617 is not a gear because it is only adjacent to one part number.)
    Adding up all of the gear ratios produces 467835.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_03.txt"
        )
    ) == 467835
