"""Part 01 Module"""
import os

import click

from ..puzzle.part_01 import answer_01


@click.command()
@click.option(
    '--input',
    "input_file",
    type=click.Path(exists=True),
    default=os.path.join("inputs", "day_21.txt"),
)
@click.option(
    '--steps',
    "total_steps",
    type=int,
    default=64,
)
def part_01(input_file: str, total_steps: int):
    """Part 1"""

    result = answer_01(input_file, total_steps)

    print(result)
