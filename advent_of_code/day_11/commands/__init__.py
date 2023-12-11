"""day 11 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_11():
    """Day 11: Cosmic Expansion"""

# add individual parts
day_11.add_command(part_01)
day_11.add_command(part_02)
