"""hash module"""


def get_hash_value(hash_input: str) -> int:
    """caculates hash "value" of given string

    Args:
        hash_input (bool): input string to calculate value for

    Returns:
        int: calculated value
    """
    hash_value = 0

    for character in hash_input:
        hash_value += ord(character)
        hash_value *= 17
        hash_value %= 256

    return hash_value
