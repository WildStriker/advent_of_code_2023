"""day 14 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_14():
    """Day 14: Parabolic Reflector Dish"""

# add individual parts
day_14.add_command(part_01)
day_14.add_command(part_02)
