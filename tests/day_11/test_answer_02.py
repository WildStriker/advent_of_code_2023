"""test_answer_02 module (day 11)"""
import os

from advent_of_code.day_11.puzzle.pairs import get_total_pair_distances
from advent_of_code.day_11.puzzle.parse import parse_input
from advent_of_code.day_11.puzzle.part_02 import answer_02


def test_case_1():
    """
    If each empty row or column was 10 times larger,
    the sum of the shortest paths between every pair of galaxies would be 1030
    """
    galaxy_mapping = parse_input(
        os.path.join(
            "test_inputs",
            "day_11.txt"
        ),
        10
    )
    assert get_total_pair_distances(galaxy_mapping) == 1030


def test_case_2():
    """
    If each empty row or column was 100 times larger,
    the sum of the shortest paths between every pair of galaxies would be 8410
    """
    galaxy_mapping = parse_input(
        os.path.join(
            "test_inputs",
            "day_11.txt"
        ),
        100
    )
    assert get_total_pair_distances(galaxy_mapping) == 8410


def test_case_3():
    """test with full expansion for part 2 (1000000)"""
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_11.txt"
        )
    ) == 82000210


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_02(
        os.path.join(
            "inputs",
            "day_11.txt"
        )
    ) == 593821230983
