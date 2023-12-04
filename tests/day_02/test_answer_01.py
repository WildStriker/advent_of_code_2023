"""test_answer_01 module (day 2)"""
import os

from advent_of_code.day_02.puzzle.part_01 import answer_01


def test_case_1():
    """
    In game 1, three sets of cubes are revealed from the bag (and then put back again).
    The first set is 3 blue cubes and 4 red cubes;
    the second set is 1 red cube, 2 green cubes, and 6 blue cubes;
    the third set is only 2 green cubes.

    The Elf would first like to know which games would have been possible if the bag 
    contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

    In the example above, games 1, 2, and 5 would have been possible if the bag had
    been loaded with that configuration. However, game 3 would have been impossible
    because at one point the Elf showed you 20 red cubes at once; similarly, game 4
    would also have been impossible because the Elf showed you 15 blue cubes at once.
    If you add up the IDs of the games that would have been possible, you get 8
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_02.txt"
        )
    ) == 8


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_02.txt"
        )
    ) == 2076
