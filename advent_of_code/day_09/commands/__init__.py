"""day 9 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_09():
    """Day 9: Mirage Maintenance"""


# add individual parts
day_09.add_command(part_01)
day_09.add_command(part_02)
