"""Part 2 Module"""
import math

from .node import get_node_end
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    instructions = parse_input(file_input, "[0-9A-Z]+A")

    all_steps = []
    for node in instructions.start_nodes:
        all_steps.append(get_node_end(node, instructions))

    return math.lcm(*all_steps)
