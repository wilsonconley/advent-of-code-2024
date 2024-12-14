__all__ = ["solve"]

import typing as t
from pathlib import Path

from .. import util


def solve(input_type: t.Literal["sample", "input"] = "input") -> None:
    input_path = util.input_path(Path(__file__).parent.name, input_type)

    # Part 1
    group_one = []
    group_two = []
    for line in util.yield_input_lines(input_path):
        a, b = line.split()
        group_one.append(a)
        group_two.append(b)
    group_one = sorted(group_one)
    group_two = sorted(group_two)
    total = 0
    for a, b in zip(group_one, group_two):
        distance = abs(int(a) - int(b))
        total += distance
    print(f"Part 1 ({input_type}): ")
    print(total)

    # Part 2
    total = 0
    for value in group_one:
        count = group_two.count(value)
        score = int(value) * count
        total += score
    print(f"Part 2 ({input_type}): ")
    print(total)
