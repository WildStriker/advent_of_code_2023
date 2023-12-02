"""Part 1 Module"""
from .parse import Game, parse_input

available_cubes = {
    "red": 12,
    "green": 13,
    "blue":  14,
}


def is_possible(game: Game) -> bool:
    """checks to see if game is possible with cube counts available

    Args:
        game (Game): Game to validate

    Returns:
        bool: True if there is enough cubes to play this Game
    """
    for cubes in game.rounds:
        for cube in cubes:
            available_cube = available_cubes[cube.color]
            if cube.amount > available_cube:
                return False

    return True


def answer_01(file_input: str):
    """Part 1"""

    games = parse_input(file_input)

    total = 0
    for game in games:
        if is_possible(game):
            total += game.game_id

    return total
