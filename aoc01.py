# https://adventofcode.com/2023/day/1

"""
Part 1:
Read the file, extract the 1st and last ints on each line
treat them as a two digit number and sum them all.

Part 2:
substitute ints for the spelled out names of the numbers,
then do the same things before
"""

import re
from utils import read_file, alphabet



def first_last_ints(line: str) -> int:
    # strip everything that's not a number, concatenate the first + last
    nums = list(filter(lambda x: x not in alphabet, line))

    fst, lst = nums[0], nums[-1]
    return int(f"{fst}{lst}")


def replace_digits(line: str) -> int:
    digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
              "six": 6, "seven": 7, "eight": 8, "nine": 9}

    regex = r"(?=(one|two|three|four|five|six|seven|eight|nine))"

    # get indices of first and last int, any relevant spelled-out
    # nums are before or after that
    int_id = [i for i, l in enumerate(line) if l.isdigit()]
    fst_i, lst_i = min(int_id), max(int_id)

    # use an overlapping regex to find all spelled out nums (digits)
    digits_before_int = re.findall(regex, line[:fst_i])
    digits_after_int = re.findall(regex, line[lst_i:])

    # fst is either the first digit before an int, or it the int
    # same (but opposite) for the lst
    fst = digits[digits_before_int[0]] if digits_before_int else int(line[fst_i])
    lst = digits[digits_after_int[-1]] if digits_after_int else int(line[lst_i])

    return int(f"{fst}{lst}")



if __name__ == "__main__":

    lines = read_file("data/01.txt")

    values = map(first_last_ints, lines)
    print(sum(values))

    values = map(replace_digits, lines)
    print(sum(values))
