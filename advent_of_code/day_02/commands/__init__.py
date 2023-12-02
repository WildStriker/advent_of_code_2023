"""day 2 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_02():
    """Day 2: Cube Conundrum"""


# add individual parts
day_02.add_command(part_01)
day_02.add_command(part_02)
