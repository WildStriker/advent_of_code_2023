"""Part 1 Module"""
from .beam import Direction, trace_beam
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    grid = parse_input(file_input)

    beam_ends = [((0, 0), Direction.EAST)]

    totals = trace_beam(grid, beam_ends)

    return totals
