"""Part 1 Module"""
import queue

from .parse import parse_input


def answer_01(file_input: str, total_steps: int):
    """Part 1"""

    map_plots = parse_input(file_input)

    traveled = {map_plots.start_location}
    total_plots = 0
    frontier = queue.PriorityQueue()
    frontier.put((0, map_plots.start_location))

    remainder = total_steps % 2

    while not frontier.empty():

        steps, current_position = frontier.get()
        if steps % 2 == remainder:
            total_plots += 1

        if steps >= total_steps:
            continue

        neighbors = map_plots.get_neighbors(current_position, False, traveled)
        if not neighbors:
            continue

        for neighbor in neighbors:
            traveled.add(neighbor)
            frontier.put((steps + 1, neighbor))

    return total_plots
