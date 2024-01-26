from utils import read_file, neighbours
from typing import List, Dict, Tuple

"""
This puzzle involves looking at a grid, parsing
n-digit numbers on that grid, and finding symbols
that border those numbers -- the challenge is that by
"borders the numbers" we mean border any digit in the
number.
"""

Row = List[str]
Grid = List[Row]
Point = Tuple[int, int]


class Number:
    """
    This number class will act as a place to put
    digits, so that I can incrementally add digits to
    the right as I see them on the grid
    """
    def __init__(self):
        self.num = 0
        self.digits = ""

    def add(self, digit):
        self.digits += digit
        self.num = int(self.digits)
        return self

    def __repr__(self):
        return self.digits

    def __hash__(self):
        """
        the "hash" is just the memory address,
        a unique identifier allowing us to know
        when a number spanning indices is the same number
        (made from adjacent digits)
        """
        return id(self)


Schematic = Dict[Point, Number]


def create_schematic(grid: Grid) -> Schematic:
    """
    a schematic is a dict that maps locations on the grid (i, j)
    to Numbers, where a Number is a class that I can update incrementally
    as I scan across the grid and see new digits. This means that all
    adjacent cells which contain a digit will end up mapped to the same Number
    """
    schematic = {}
    n = Number()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell.isnumeric():
                schematic[(i, j)] = n.add(cell)
            else:
                n = Number()

    return schematic


def symbol_neighbours(grid: Grid, schematic: Schematic) -> List[int]:
    """
    Now we iterate over the grid, and each time we hit a symbol look up
    its neighbours in the schematic
    """
    nums = set()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if not cell.isnumeric() and cell != ".":
                nums.update(
                    [schematic[n] for n in neighbours((i, j)) if n in schematic]
                )

    return [n.num for n in nums]


def gear_neighbours(grid: Grid, schematic: Schematic) -> List[int]:
    ratios = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "*":
                nums = set(schematic[n] for n in neighbours((i, j)) if n in schematic)
                if len(nums) == 2:
                    a, b = nums
                    ratios.append(a.num * b.num)

    return ratios

if __name__ == "__main__":

    grid = read_file("data/03.txt", parser=list)
    schematic = create_schematic(grid)
    print(sum(symbol_neighbours(grid, schematic)))

    print(sum(gear_neighbours(grid, schematic)))
