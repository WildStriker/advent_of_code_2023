"""Part 2 Module"""
import re

from .hash import get_hash_value
from .parse import parse_input

PATTERN = re.compile("(.+)([-=])([0-9]*)")


def answer_02(file_input: str):
    """Part 2"""

    hashes = parse_input(file_input)

    boxes = {}
    for current_hash in hashes:
        matches = PATTERN.search(current_hash)
        label, mode, lens_number = matches.groups()
        box_number = get_hash_value(label)

        if box_number in boxes:
            box = boxes[box_number]
        else:
            box = {}
            boxes[box_number] = box

        if mode == "=":
            box[label] = int(lens_number)
        elif label in box:
            del box[label]

    totals = 0

    for box_number, box in boxes.items():
        for slot, (label, focus_length) in enumerate(box.items(), 1):
            totals += (1 + box_number) * slot * focus_length

    return totals
