"""day 18 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_18():
    """Day 18: Lavaduct Lagoon"""

# add individual parts
day_18.add_command(part_01)
day_18.add_command(part_02)
