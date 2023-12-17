"""Part 2 Module"""
from .heat_loss import get_lowest_heat_loss_path
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    city_blocks, end = parse_input(file_input)

    minimal_heat_loss = get_lowest_heat_loss_path(
        (0, 0),
        end,
        city_blocks,
        4,
        10,
    )
    return minimal_heat_loss
