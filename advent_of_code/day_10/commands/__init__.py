"""day 10 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_10():
    """Day 10: Pipe Maze"""

# add individual parts
day_10.add_command(part_01)
day_10.add_command(part_02)
