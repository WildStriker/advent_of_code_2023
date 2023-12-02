"""parse module"""
from dataclasses import dataclass
from typing import List


@dataclass
class Cube:
    """Individual Rounds for a Game"""
    amount: int
    color: str


@dataclass
class Game:
    """A Single Game Instance"""
    game_id: int
    rounds: List[List[Cube]]


def parse_input(input_file: str) -> List[Game]:
    """Parse input into a usable format

    Args:
        input_file (str): input file

    Returns:
        List[Game]: List of parsed game info
    """

    games = []
    with open(input_file, encoding="utf-8") as file_input:
        for game_line in file_input:

            game_id, rounds_string = game_line.split(":")

            game_id = int(game_id.split(" ")[1])
            rounds_string = rounds_string.split(";")

            parsed_rounds = []
            games.append(Game(game_id, parsed_rounds))
            for cubes in rounds_string:
                cubes_string = cubes.split(",")

                parsed_cubes = []
                parsed_rounds.append(parsed_cubes)
                for cube_string in cubes_string:
                    amount, color = cube_string.strip().split(" ")
                    amount = int(amount)

                    parsed_cubes.append(Cube(amount, color))
    return games
