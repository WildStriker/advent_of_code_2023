"""Part 1 Module"""
from typing import Dict, List

from .parse import Comparator, Workflow, parse_input


def _get_results(workflows: Dict[str, Workflow], parts: List[Dict[str, int]], label: str):
    if label in {"A", "R"}:
        return label

    workflow = workflows[label]

    for rule in workflow.rules:
        rating = parts[rule.part]

        if rule.comparator == Comparator.GREATER_THAN:
            result = rating > rule.value
        else:
            result = rating < rule.value

        if result:
            return _get_results(workflows, parts, rule.then_next_workflow)

    return _get_results(workflows, parts, workflow.catch_all)


def answer_01(file_input: str):
    """Part 1"""

    workflows, listed_parts = parse_input(file_input)

    totals = 0
    for parts in listed_parts:
        result = _get_results(workflows, parts, "in")
        if result == "A":
            totals += sum(parts.values())

    return totals
