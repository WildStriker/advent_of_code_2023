"""Part 2 Module"""
from .parse import parse_input
from .sequence import get_next_diff_sequence


def _create_previous_sequence(diffs):
    new_diff = 0
    for diff in diffs[-2::-1]:
        new_diff = diff - new_diff

    return new_diff


def answer_02(file_input: str):
    """Part 2"""

    history = parse_input(file_input)

    total = 0
    for current_history in history:
        first_diffs = get_next_diff_sequence(current_history, True)
        new_diff = _create_previous_sequence(first_diffs)

        total += current_history[0] - new_diff

    return total
