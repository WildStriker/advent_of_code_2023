"""test_answer_02 module (day 21)"""
import os

from advent_of_code.day_21.puzzle.part_02 import answer_02


def test_case_1():
    """
    In exactly 6 steps, he can still reach 16 garden plots.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_21.txt"
        ),
        6
    ) == 16


def test_case_2():
    """
    In exactly 10 steps, he can reach any of 50 garden plots.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_21.txt"
        ),
        10
    ) == 50


def test_case_3():
    """
    In exactly 50 steps, he can reach 1594 garden plots.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_21.txt"
        ),
        50
    ) == 1594


def test_case_4():
    """
    In exactly 100 steps, he can reach 6536 garden plots.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_21.txt"
        ),
        100
    ) == 6536


def test_case_5():
    """
    In exactly 500 steps, he can reach 167004 garden plots.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_21.txt"
        ),
        500
    ) == 167004


def test_case_6():
    """
    In exactly 1000 steps, he can reach 668697 garden plots.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_21.txt"
        ),
        1000
    ) == 668697


def test_case_7():
    """
    In exactly 5000 steps, he can reach 16733044 garden plots.
    """
    assert answer_02(
        os.path.join(
            "test_inputs",
            "day_21.txt"
        ),
        5000
    ) == 16733044
