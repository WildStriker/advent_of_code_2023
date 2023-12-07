"""day 7 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_07():
    """Day 7: Camel Cards"""

# add individual parts
day_07.add_command(part_01)
day_07.add_command(part_02)
