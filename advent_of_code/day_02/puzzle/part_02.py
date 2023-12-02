"""Part 2 Module"""
from .parse import parse_input


def answer_02(file_input: str):
    """Part 2"""

    games = parse_input(file_input)

    total = 0
    for game in games:

        fewest = {
            "red": 0,
            "green": 0,
            "blue":  0,
        }

        for cubes in game.rounds:
            for cube in cubes:
                fewest[cube.color] = max(fewest[cube.color], cube.amount)

        power = 1
        for amount in fewest.values():
            power *= amount
        total += power

    return total
