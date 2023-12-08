"""node module"""
from .parse import Instructions


def get_node_end(node: str, instructions: Instructions) -> int:
    """gets the total amount of steps to reach the end of the node directions

    Args:
        node (str): starting node
        instructions (Instructions): instructions, contains nodes and directions

    Returns:
        int: total steps taken
    """
    steps_count = 0
    while True:
        for direction in instructions.directions:
            node = instructions.nodes[node][direction]
            steps_count += 1
            if node.endswith("Z"):
                return steps_count
