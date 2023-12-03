"""Part 01 Module"""
import os

import click

from ..puzzle.part_01 import answer_01


@click.command()
@click.option(
    '--input',
    "input_file",
    type=click.Path(exists=True),
    default=os.path.join("inputs", "day_03.txt"),
)
def part_01(input_file: str):
    """Part 1"""

    result = answer_01(input_file)

    print(result)
