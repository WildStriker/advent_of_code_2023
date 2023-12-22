"""Part 02 Module"""
import os

import click

from ..puzzle.part_02 import answer_02


@click.command()
@click.option(
    '--input',
    "input_file",
    type=click.Path(exists=True),
    # TODO
    default=os.path.join("inputs", "day_22.txt"),
)
def part_02(input_file: str):
    """Part 2"""

    # TODO
    result = answer_02(input_file)

    print(result)
