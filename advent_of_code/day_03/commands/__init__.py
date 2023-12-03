"""day 3 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_03():
    """Day 3: Gear Ratios"""


# add individual parts
day_03.add_command(part_01)
day_03.add_command(part_02)
