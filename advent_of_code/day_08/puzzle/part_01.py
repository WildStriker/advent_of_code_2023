"""Part 1 Module"""
from .node import get_node_end
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    instructions = parse_input(file_input, "AAA")

    return get_node_end(instructions.start_nodes[0], instructions)
