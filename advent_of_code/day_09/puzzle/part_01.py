"""Part 1 Module"""
from .parse import parse_input
from .sequence import get_next_diff_sequence


def answer_01(file_input: str):
    """Part 1"""

    history = parse_input(file_input)

    total = 0
    for current_history in history:
        last_diffs = get_next_diff_sequence(current_history, False)
        total += sum(last_diffs) + current_history[-1]

    return total
