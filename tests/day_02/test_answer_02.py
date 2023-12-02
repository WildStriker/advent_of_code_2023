"""test_answer_02 module (day 2)"""
import os

from advent_of_code.day_02.puzzle.part_02 import answer_02


def test_case_1():
    """
    In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes.
    If any color had even one fewer cube, the game would have been impossible.

    Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
    Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
    Game 4 required at least 14 red, 3 green, and 15 blue cubes.
    Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

    The power of a set of cubes is equal to the numbers of
    red, green, and blue cubes multiplied together.
    The power of the minimum set of cubes in game 1 is 48.
    In games 2-5 it was 12, 1560, 630, and 36, respectively.
    Adding up these five powers produces the sum 2286.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_02.txt"
        )
    ) == 2286
