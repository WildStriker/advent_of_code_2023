"""cli module, register all day modules here"""
import click

from .day_01.commands import day_01
from .day_02.commands import day_02


@click.group()
def cli():
    """Advent of Code 2023"""


# register commands in CLI
cli.add_command(day_01)
cli.add_command(day_02)
