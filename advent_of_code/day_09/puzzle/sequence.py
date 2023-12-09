"""sequence module"""
from typing import List


def get_next_diff_sequence(values: List[int], inverse: bool) -> List[int]:
    """gets the next sequence of diffs

    Args:
        values (List[int]): input values to start from
        inverse (bool): if inversed, return the first set of diffs instead of the last

    Returns:
        List[int]: list of all diffs in the sequence
    """
    diffs = []
    all_zero = True
    for previous_index, value in enumerate(values[1:]):
        diff = value - values[previous_index]
        diffs.append(diff)
        if diff != 0:
            all_zero = False

    if not all_zero:

        if inverse:
            diff = diffs[0]
        else:
            diff = diffs[-1]

        return [diff, *get_next_diff_sequence(diffs, inverse)]

    return [0,]
