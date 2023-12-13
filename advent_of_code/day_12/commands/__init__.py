"""day 12 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_12():
    """Day 12: Hot Springs"""


# add individual parts
day_12.add_command(part_01)
day_12.add_command(part_02)
