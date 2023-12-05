"""test_answer_01 module (day 5)"""
import os

from advent_of_code.day_05.puzzle.part_01 import answer_01


def test_case_1():
    """With this map, you can look up the soil number required for each initial seed number:

    Seed number 79 corresponds to soil number 81.
    Seed number 14 corresponds to soil number 14.
    Seed number 55 corresponds to soil number 57.
    Seed number 13 corresponds to soil number 13.

    The gardener and his team want to get started as soon as possible,
    so they'd like to know the closest location that needs a seed. Using these maps,
    find the lowest location number that corresponds to any of the initial seeds.
    To do this, you'll need to convert each seed number through other categories
    until you can find its corresponding location number.

    In this example, the corresponding types are:
    Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
    Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
    Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
    Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

    So, the lowest location number in this example is 35.
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_05.txt"
        )
    ) == 35


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_05.txt"
        )
    ) == 214922730
