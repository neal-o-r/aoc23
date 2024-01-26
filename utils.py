from typing import List, Callable, Tuple, Any, Dict
from collections import defaultdict


Point = Tuple[int, int]


alphabet = "abcdefghijklmnopqrstuvwxyz"
inf = float("inf")


lines = str.splitlines  # By default, split input text into lines


def read_file(fname: str, parser: Callable = str, splitter: Callable = lines) -> List:
    """
    read a file into a list of strs, split on delim
    """
    contents = open(fname).read()
    return list(map(parser, splitter(contents)))


def grid_dict(grid: List[List], default_type: Callable = lambda: None) -> Dict[Point, Any]:
    """
    It's sometimes handy to store a 2d grid as a dictionary
    of indices: values, rather than as a list of lists
    """
    d = defaultdict(default_type)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            d[(i, j)] = cell

    return d


def neighbours(pt: Point, nsew: bool = True, bounds: tuple = ((-inf, inf), (-inf, inf))) -> List[Point]:
    """
    given a 2d point, return all 8 neighbours,
    or 4 if nsew is True
    """
    x, y = pt
    bx, by = bounds

    pts = []
    if nsew:
        pts += [(x, y + 1),
                (x, y - 1),
                (x + 1, y),
                (x - 1, y)]

    pts += [(x - 1, y - 1), (x + 1, y + 1 ), (x - 1, y + 1), (x + 1, y - 1)]

    return [(x, y) for x, y in pts if (bx[0] < x < bx[1]) and (by[0] < y < by[1])]
