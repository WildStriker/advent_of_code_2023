"""Part 01 Module"""
import os

import click

from ..puzzle.part_01 import answer_01


@click.command()
@click.option(
    '--input',
    "input_file",
    type=click.Path(exists=True),
    default=os.path.join("inputs", "day_24.txt"),
)
@click.option(
    '--min',
    "min_range",
    type=int,
    default=200000000000000,
)
@click.option(
    '--max',
    "max_range",
    type=int,
    default=400000000000000,
)
def part_01(input_file: str, min_range:int, max_range:int):
    """Part 1"""

    result = answer_01(input_file, min_range, max_range)

    print(result)
