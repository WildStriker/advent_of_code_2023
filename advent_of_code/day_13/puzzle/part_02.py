"""Part 1 Module"""
from .parse import parse_input
from .reflection import calculate_found_reflection, find_reflection


def answer_02(file_input: str):
    """Part 1"""

    reflections = parse_input(file_input)

    total = 0
    for reflection in reflections:
        original_found = find_reflection(reflection)

        total_columns = len(reflection.by_column)
        smudge_row = 0
        smudge_column = 0

        while True:
            original_value = reflection.by_row[smudge_row][smudge_column]
            cleaned = "." if original_value == "#" else "."
            reflection.by_row[smudge_row][smudge_column] = cleaned
            reflection.by_column[smudge_column][smudge_row] = cleaned

            found = find_reflection(reflection, original_found)
            reflection.by_row[smudge_row][smudge_column] = original_value
            reflection.by_column[smudge_column][smudge_row] = original_value

            if found:
                total += calculate_found_reflection(found)
                break

            smudge_column += 1
            if smudge_column >= total_columns:
                smudge_row += 1
                smudge_column = 0

    return total
