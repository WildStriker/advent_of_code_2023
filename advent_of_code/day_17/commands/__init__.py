"""day 17 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_17():
    """Day 17: Clumsy Crucible"""


# add individual parts
day_17.add_command(part_01)
day_17.add_command(part_02)
