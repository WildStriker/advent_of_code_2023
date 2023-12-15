"""test_hash module (day 15)"""
from advent_of_code.day_15.puzzle.hash import get_hash_value


def test_case_1():
    """HASH should be 52"""
    assert get_hash_value(
        "HASH"
    ) == 52


def test_case_2():
    """test individual hash values"""
    assert get_hash_value("rn=1") == 30
    assert get_hash_value("cm-") == 253
    assert get_hash_value("qp=3") == 97
    assert get_hash_value("cm=2") == 47
    assert get_hash_value("qp-") == 14
    assert get_hash_value("pc=4") == 180
    assert get_hash_value("ot=9") == 9
    assert get_hash_value("ab=5") == 197
    assert get_hash_value("pc-") == 48
    assert get_hash_value("pc=6") == 214
    assert get_hash_value("ot=7") == 231
