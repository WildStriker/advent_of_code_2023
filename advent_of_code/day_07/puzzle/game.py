"""game module"""
import collections
import enum
from functools import cmp_to_key
from typing import List, Tuple

from .parse import Hand

HIGHEST_CARD = "A"
WILD_CARD = "J"

WILD_VALUE = 1
NON_WILD_VALUE = 11

FACE_VALUE = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class HandType(enum.Enum):
    """Possible Hand Types"""
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


def _compare_cards(hand1: Tuple[Hand, HandType], hand2: Tuple[Hand, HandType]) -> int:
    """compares two cards together to determine rank (lowest to highest)

    Args:
        hand1 (Tuple[Hand, HandType]): hand1
        hand2 (Tuple[Hand, HandType]): hand2

    Returns:
        int: -1 if first card is lower, 1 is higher, 0 is the same
    """
    if hand1[1].value < hand2[1].value:
        return -1
    elif hand1[1].value > hand2[1].value:
        return 1
    else:
        for hand1_card, hand2_card in zip(hand1[0].cards, hand2[0].cards):
            hand1_card_value = FACE_VALUE[hand1_card]
            hand2_card_value = FACE_VALUE[hand2_card]
            if hand1_card_value < hand2_card_value:
                return -1
            elif hand1_card_value > hand2_card_value:
                return 1

    return 0


def _get_hand_type(hand: Hand, joker_is_wild: bool) -> HandType:
    """returns a hand type

    Args:
        hand (Hand): the hand to evaluate
        joker_is_wild (bool): true if jokers are wild

    Returns:
        HandType: returns the hand type
    """
    counts = collections.Counter(hand.cards)

    # udpate joker cards to be the card with the highest count
    if joker_is_wild and WILD_CARD in counts:
        jokers_count = counts.pop(WILD_CARD)
        most_common = counts.most_common(1)
        if not most_common:
            # we already know this is a five of a kind since no other card exists!
            return HandType.FIVE_OF_A_KIND

        counts[most_common[0][0]] += jokers_count

    has_three = False
    has_two = 0
    for count in counts.values():
        if count == 5:
            return HandType.FIVE_OF_A_KIND

        if count == 4:
            return HandType.FOUR_OF_A_KIND

        if count == 3:
            has_three = True
        elif count == 2:
            has_two += 1

    if has_three and has_two:
        return HandType.FULL_HOUSE
    elif has_three:
        return HandType.THREE_OF_A_KIND
    elif has_two > 1:
        return HandType.TWO_PAIR
    elif has_two == 1:
        return HandType.ONE_PAIR

    return HandType.HIGH_CARD


def calculate_winnings(hands: List[Hand], joker_is_wild: bool) -> int:
    """calculates winnings given all hands

    Args:
        hands (List[Hand]): hands to rank and score
        joker_is_wild (bool): if true, joker cards are consider "wild"
            and will take on the value of the next highest card count

    Returns:
        int: total calculated winnings
    """
    if joker_is_wild:
        FACE_VALUE[WILD_CARD] = WILD_VALUE
    else:
        FACE_VALUE[WILD_CARD] = NON_WILD_VALUE

    hands_and_type = []
    for hand in hands:
        hand_type = _get_hand_type(hand, joker_is_wild)
        hands_and_type.append((hand, hand_type))

    hands_and_type.sort(key=cmp_to_key(_compare_cards))

    total = 0
    for rank, hand_and_type in enumerate(hands_and_type, 1):
        total += hand_and_type[0].bid * rank

    return total
