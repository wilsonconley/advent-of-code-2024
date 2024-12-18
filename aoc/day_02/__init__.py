__all__ = ["solve"]

import typing as t
from pathlib import Path

from .. import util


def is_safe(levels: list[int]) -> bool:
    diff = [abs(levels[i] - levels[i - 1]) for i in range(1, len(levels))]
    return (sorted(levels) == levels or sorted(levels, reverse=True) == levels) and (
        min(diff) >= 1 and max(diff) <= 3
    )


def solve(input_type: t.Literal["sample", "input"] = "input") -> None:
    input_path = util.input_path(Path(__file__).parent.name, input_type)

    # Part 1
    safe = 0
    for line in util.yield_input_lines(input_path):
        levels = [int(x) for x in line.strip().split()]
        diff = [abs(levels[i] - levels[i - 1]) for i in range(1, len(levels))]
        if (sorted(levels) == levels or sorted(levels, reverse=True) == levels) and (
            min(diff) >= 1 and max(diff) <= 3
        ):
            safe += 1

    print(f"Part 1 ({input_type}): {safe}")

    # Part 2
    safe = 0
    for line in util.yield_input_lines(input_path):
        levels = [int(x) for x in line.strip().split()]
        combos = [levels]
        for i in range(0, len(levels)):
            combos.append(levels[:i] + levels[i + 1 :])
        for combo in combos:
            if is_safe(combo):
                safe += 1
                break
    print(f"Part 2 ({input_type}): {safe}")
