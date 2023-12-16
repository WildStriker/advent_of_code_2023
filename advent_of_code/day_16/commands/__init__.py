"""day 16 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_16():
    """Day 16: The Floor Will Be Lava"""

# add individual parts
day_16.add_command(part_01)
day_16.add_command(part_02)
