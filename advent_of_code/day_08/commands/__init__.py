"""day 8 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_08():
    """Day 8: Haunted Wasteland"""


# add individual parts
day_08.add_command(part_01)
day_08.add_command(part_02)
