"""day 23 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_23():
    """Day 23: A Long Walk"""


# add individual parts
day_23.add_command(part_01)
day_23.add_command(part_02)
