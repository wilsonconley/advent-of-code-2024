__all__ = ["solve"]

import typing as t
from pathlib import Path

from .. import util


def solve(input_type: t.Literal["sample", "input"] = "input") -> None:
    input_path = util.input_path(Path(__file__).parent.name, input_type)

    # Part 1
    print(f"Part 1 ({input_type}): ")

    # Part 2
    print(f"Part 2 ({input_type}): ")
