"""day 20 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_20():
    """Day 20: Pulse Propagation"""


# add individual parts
day_20.add_command(part_01)
day_20.add_command(part_02)
