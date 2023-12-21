"""Part 02 Module"""
import os

import click

from ..puzzle.part_02 import answer_02


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
    default=26501365,
)
def part_02(input_file: str, total_steps: int):
    """Part 2"""

    result = answer_02(input_file, total_steps)


    print(result)
