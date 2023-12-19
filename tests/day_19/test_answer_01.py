"""test_answer_01 module (day 19)"""
import os

from advent_of_code.day_19.puzzle.part_01 import answer_01


def test_case_1():
    """
    {x=787,m=2655,a=1222,s=2876}: in -> qqz -> qs -> lnx -> A
    {x=1679,m=44,a=2067,s=496}: in -> px -> rfg -> gd -> R
    {x=2036,m=264,a=79,s=2244}: in -> qqz -> hdj -> pv -> A
    {x=2461,m=1339,a=466,s=291}: in -> px -> qkq -> crn -> R
    {x=2127,m=1623,a=2188,s=1013}: in -> px -> rfg -> A

    Three parts are accepted.
    Adding up the x, m, a, and s rating for each of the accepted parts gives
    7540 for the part with x=787,
    4623 for the part with x=2036,
    6951 for the part with x=2127.

    Adding all of the ratings for all of the accepted parts gives the sum total of 19114.
    """
    assert answer_01(
        os.path.join(
            "test_inputs",
            "day_19.txt"
        )
    ) == 19114


def test_puzzle_input():
    """test results from real puzzle input"""
    assert answer_01(
        os.path.join(
            "inputs",
            "day_19.txt"
        )
    ) == 377025
