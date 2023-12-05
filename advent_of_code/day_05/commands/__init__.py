"""day 5 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_05():
    """Day 5: If You Give A Seed A Fertilizer"""


# add individual parts
day_05.add_command(part_01)
day_05.add_command(part_02)
