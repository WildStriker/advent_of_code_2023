"""parse module"""
from dataclasses import dataclass
import enum
import re
from typing import List, Tuple, Dict

WORKFLOW_PATTERN = re.compile(
    "([a-z]+){(([a-z]+[<>][0-9]+:[a-zA-Z]+,)+)([a-zA-Z]+)}"
)
RULE_PATTERN = re.compile("([a-z]+)([<>])([0-9]+):([a-zA-Z]+)")


class Comparator(enum.Enum):
    """Comparator operator to use"""
    LESS_THAN = 0
    GREATER_THAN = 1


@dataclass
class Rule:
    """Rule info"""
    part: str
    comparator: Comparator
    value: int
    then_next_workflow: str


@dataclass
class Workflow:
    """Workflow info"""
    name: str
    rules: List[Rule]
    catch_all: str


def parse_input(input_file: str) -> Tuple[Dict[str, Workflow], List[Dict[str, int]]]:
    """process into file into workflow and list of parts

    Args:
        input_file (str): input file to process

    Raises:
        NotImplementedError: raised when an unimplemented operator is given

    Returns:
        Tuple[Dict[str, Workflow], List[Dict[str, int]]]: mapping of workflows and list of parts
    """

    workflows = {}
    parts = []
    with open(input_file, encoding="utf-8") as file_input:
        # workflows
        for line in file_input:
            if not line.strip():
                break

            name, rules_section, _, catch_all = WORKFLOW_PATTERN.search(
                line
            ).groups()

            rules = []
            for rule_section in rules_section.removesuffix(",").split(","):
                part, comparator, value, then_next_workflow = RULE_PATTERN.search(
                    rule_section).groups()

                if comparator == ">":
                    comparator = Comparator.GREATER_THAN
                elif comparator == "<":
                    comparator = Comparator.LESS_THAN
                else:
                    raise NotImplementedError(
                        f"Unimplemented operator: {comparator}"
                    )

                rules.append(
                    Rule(part, comparator, int(value), then_next_workflow))

            workflows[name] = Workflow(name, rules, catch_all)

        # parts
        listed_parts = []
        for line in file_input:
            line = line.strip()[1:-1]

            parts = {}
            listed_parts.append(parts)
            for part in line.split(","):
                name, rating = part.split("=")
                rating = int(rating)

                parts[name] = rating

    return workflows, listed_parts
