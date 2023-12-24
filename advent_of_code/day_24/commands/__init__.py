"""day 24 group set up"""
import click

from .command_01 import part_01


@click.group()
def day_24():
    """Day 24: Never Tell Me The Odds"""

# add individual parts
day_24.add_command(part_01)
