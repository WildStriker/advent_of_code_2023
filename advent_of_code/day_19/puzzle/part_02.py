"""Part 2 Module"""
import copy
from typing import Dict, List, Tuple

from .parse import Comparator, Workflow, parse_input


def _get_possible(
    workflows: Dict[str, Workflow],
    part_ranges: List[Dict[str, Tuple[int, int]]],
    label,
) -> int:
    if label == "R":
        # none of these combinations matter since it is rejected!
        return 0
    elif label == "A":
        # calculate all total possibilities
        totals = 1
        for min_rating, max_rating in part_ranges.values():
            totals *= max_rating - min_rating + 1
        return totals

    totals = 0
    workflow = workflows[label]

    # process all rules
    # split parts into "accepted" range and continue processing the next flow
    # then continue processing the remaing range for the parts "left range"
    for rule in workflow.rules:
        min_rating, max_rating = part_ranges[rule.part]

        # accepted range to continue to the next workflow
        accepted_parts = copy.deepcopy(part_ranges)
        if rule.comparator == Comparator.GREATER_THAN:
            accepted_parts[rule.part] = (rule.value + 1, max_rating)
            # update part_ranges for this part to have remaining values
            part_ranges[rule.part] = (min_rating, rule.value)
        else:
            accepted_parts[rule.part] = (min_rating, rule.value - 1)
            # update part_ranges for this part to have remaining values
            part_ranges[rule.part] = (rule.value, max_rating)

        totals += _get_possible(
            workflows,
            accepted_parts,
            rule.then_next_workflow,
        )

    return totals + _get_possible(workflows, copy.deepcopy(part_ranges), workflow.catch_all)


def answer_02(file_input: str):
    """Part 2"""

    workflows, _listed_parts = parse_input(file_input)

    totals = _get_possible(
        workflows,
        {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)},
        "in",
    )

    return totals
