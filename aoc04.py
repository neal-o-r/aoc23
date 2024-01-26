from utils import read_file
from typing import List
from dataclasses import dataclass
import re


@dataclass
class Card:
    card: int
    numbers: List[int]
    winners: List[int]


def parser(line: str) -> List[Card]:
    card, *rest = line.split(":")

    card_no = int(*re.findall("\d+", card))
    winners, nums = map(str.split, rest[0].split("|"))

    return Card(card_no, list(map(int, nums)), list(map(int, winners)))


def matches(card: Card) -> int:
    """
    how many matches are there?
    """
    return sum(1 for n in card.numbers if n in card.winners)


def score(n_matches: int) -> int:
    if n_matches == 0:
        return 0
    if n_matches == 1:
        return 1
    return 2 * score(n_matches - 1)


def count_cards(cards: List[Card]) -> List[int]:
    """
    we need to determine how many cards total we
    have at the end of a process where each winning
    cards wins us  1 more of the
    next "match" consecutive cards
    """
    # we start with one copy of each card
    n_cards = [1] * len(cards)
    for i, card in enumerate(cards):
        m = matches(card)
        for j in range(i + 1, i + m + 1):
            # for each card from i + 1 -> m we will
            # win an additional card for every card
            # we have in n_cards[i]
            n_cards[j] += n_cards[i]

    return n_cards


if __name__ == "__main__":

    cards = read_file("data/04.txt", parser=parser)

    scores = lambda cs: map(score, map(matches, cs))
    print(sum(scores(cards)))


    print(sum(count_cards(cards)))
