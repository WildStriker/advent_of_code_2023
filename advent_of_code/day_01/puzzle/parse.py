"""parse module"""
from typing import List

CONVERT_TO_NUMERIC = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse_input(input_file: str, numeric_only: bool) -> List[int]:
    """reads an input file and returns parsed data

    Args:
        input_file (str): input file to parse
        numeric_only (bool): if true, only pull digits

    Returns:
        List[int]: usable parsed list
    """
    targets = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if not numeric_only:
        targets.extend(CONVERT_TO_NUMERIC.keys())

    values = []
    with open(input_file, encoding="utf-8") as file_input:
        for value in file_input:
            found_numbers = []

            word = ""
            index = 0
            pointer = index
            possible_matches = targets
            found = None
            while index < len(value):
                word += value[pointer]

                possible_matches = _filter_possible_matches(word, possible_matches)
                if len(possible_matches) == 1 and possible_matches[0] == word:
                    if word in CONVERT_TO_NUMERIC:
                        found = CONVERT_TO_NUMERIC[word]
                    else:
                        found = int(word)
                    found_numbers.append(
                        found
                    )

                pointer += 1
                if not possible_matches or found or pointer >= len(value):
                    word = ""
                    index += 1
                    pointer = index
                    possible_matches = targets
                    found = None

            values.append(int(f"{found_numbers[0]}{found_numbers[-1]}"))

    return values


def _filter_possible_matches(word: str, possible_matches: List[str]) -> List[str]:
    """given word, filter list of possible values to extract

    Args:
        word (str): current "number" being parsed
        possible_matches (List[str]): current list of possible matches

    Returns:
        List[str]: filtered list
    """

    filtered = []
    for possible_match in possible_matches:
        if possible_match.startswith(word):
            filtered.append(possible_match)

    return filtered
