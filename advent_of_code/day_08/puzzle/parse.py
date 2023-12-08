"""parse module"""

import re
from dataclasses import dataclass
from typing import Dict, List, Tuple

REGEX = re.compile(r"([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)")


@dataclass
class Instructions:
    """Directions and Node Mappings"""
    directions: List[int]
    start_nodes: List[str]
    nodes: Dict[str, Tuple[str, str]]


def parse_input(input_file: str, start_node_pattern: str) -> Instructions:
    """parse puzzle input into useable instructions

    Args:
        input_file (str): input file to parse
        start_node_pattern (str): pattern to starting node(s)

    Returns:
        Instructions: instructions from input file
    """
    regex_start_node = re.compile(start_node_pattern)

    with open(input_file, encoding="utf-8") as file_input:
        directions = list(
            map(
                lambda direction: 0 if direction == "L" else 1,
                next(file_input).strip()
            )
        )

        _ = next(file_input)
        instructions = Instructions(directions, [], {})
        for line in file_input:
            results = REGEX.match(line)
            node = results.group(1)
            left = results.group(2)
            right = results.group(3)

            instructions.nodes[node] = (left, right)

            if regex_start_node.match(node):
                instructions.start_nodes.append(node)

    return instructions
