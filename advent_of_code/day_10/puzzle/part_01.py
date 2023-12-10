"""Part 1 Module"""
import math

from .parse import parse_input
from .trace import get_pipe_loop


def answer_01(file_input: str):
    """Part 1"""

    mapping = parse_input(file_input)

    count = len(get_pipe_loop(mapping))

    return math.ceil(count / 2)
