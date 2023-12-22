"""day TODO group set up"""
import click

from .command_01 import part_01
from .command_02 import part_02


@click.group()
def day_22():
    """Day X: TODO"""
    # TODO info here^^^^

# add individual parts
#TODO
day_22.add_command(part_01)
day_22.add_command(part_02)
