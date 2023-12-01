"""day 01 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_01():
    """Day 1: Trebuchet?!"""


# add individual parts
day_01.add_command(part_01)
day_01.add_command(part_02)
