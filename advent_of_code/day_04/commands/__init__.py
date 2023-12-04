"""day 4 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_04():
    """Day 4: Scratchcards"""


# add individual parts
day_04.add_command(part_01)
day_04.add_command(part_02)
