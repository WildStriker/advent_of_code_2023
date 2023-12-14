"""day 13 group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_13():
    """Day 13: Point of Incidence"""

day_13.add_command(part_01)
day_13.add_command(part_02)
