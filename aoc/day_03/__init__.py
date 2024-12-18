__all__ = ["solve"]

import re
import typing as t
from pathlib import Path

from .. import util


def solve(input_type: t.Literal["sample", "input"] = "input") -> None:
    input_path = util.input_path(Path(__file__).parent.name, input_type)

    # Part 1
    file = util.read_input_raw(input_path)
    total = 0
    for a, b in re.findall("mul\\((\\d+),(\\d+)\\)", file):
        total += int(a) * int(b)
    print(f"Part 1 ({input_type}): {total}")

    # Part 2
    if input_type == "sample":
        file = util.read_input_raw(
            util.input_path(Path(__file__).parent.name, "sample2")
        )
    total = 0
    enabled = True
    for match in re.findall("mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\)", file):
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
        else:
            a, b = re.search("(\\d+),(\\d+)", match).groups()  # type: ignore[union-attr]
            if enabled:
                total += int(a) * int(b)
    print(f"Part 2 ({input_type}): {total}")
