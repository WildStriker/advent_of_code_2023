"""Part 1 Module"""
from .heat_loss import get_lowest_heat_loss_path
from .parse import parse_input


def answer_01(file_input: str):
    """Part 1"""

    city_blocks, end = parse_input(file_input)

    minimal_heat_loss = get_lowest_heat_loss_path(
        (0, 0),
        end,
        city_blocks,
        0,
        3,
    )
    return minimal_heat_loss
