from utils import read_file
from dataclasses import dataclass
from typing import List, Tuple
from collections import defaultdict
import re

"""
Part 1:
parse the games and determine if the colours used in each play
(;-delimited set of colous + nums) sum to less than what is allowable

Part 2:
find the max number of each different colour that occurs in a play
compute the sum of the prod of these numbers
"""


Play = List[Tuple[int, str]]  # [(2, "green")]


@dataclass
class Game:
    game_n: int
    plays: List[Play]


def parser(line: str) -> Game:
    game, rest = line.split(":")
    game_n = int(*re.findall("\d+", game))

    plays = []
    for r in rest.split(";"):
        play = []
        for g in r.split(","):
            n, col = g.split()
            play.append((int(n), col))
        plays.append(play)

    return Game(game_n, plays)


def check_game(game: Game, allowable: dict) -> bool:
    # iterate over plays, and insert into a dict
    # then check that each val in the dict is < allowable
    for play in game.plays:
        totals = defaultdict(int)
        for n, col in play:
            totals[col] += n

        for col in totals:
            if totals[col] > allowable[col]:
                return False

    return True


def min_allowable(game: Game) -> dict:
    # iterate over all plays and insert into
    # a dict if the val is bigger than any seen before
    totals = defaultdict(int)
    for play in game.plays:
        for n, col in play:
            if n > totals[col]:
                totals[col] = n

    return totals


def power(game: Game) -> int:
    p = 1
    for _, v in min_allowable(game).items():
        p *= v

    return p


if __name__ == "__main__":

    games = read_file("data/02.txt", parser=parser)

    allowable = defaultdict(int)
    allowable.update({"red": 12, "green": 13, "blue": 14})

    print(sum(g.game_n for g in games if check_game(g, allowable)))
    print(sum(map(power, games)))
