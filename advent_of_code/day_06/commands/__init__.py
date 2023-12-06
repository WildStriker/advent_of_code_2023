"""day 6 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_06():
    """Day 6: Wait For It"""

# add individual parts
day_06.add_command(part_01)
day_06.add_command(part_02)
