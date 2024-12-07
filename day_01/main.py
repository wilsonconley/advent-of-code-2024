import argparse
import typing as t

from .. import util

parser = argparse.ArgumentParser()
parser.add_argument(
    "input",
    type=str,
    nargs="?",
    default="input",
    help="Puzzle input to use.",
)

# ============
# Main
# ============


def main(name: t.Literal["sample", "input"] = "input") -> None:
    # Part 1
    group_one = []
    group_two = []
    for line in util.yield_input_lines(name):
        a, b = line.split()
        group_one.append(a)
        group_two.append(b)
    group_one = sorted(group_one)
    group_two = sorted(group_two)
    total = 0
    for a, b in zip(group_one, group_two):
        distance = abs(int(a) - int(b))
        total += distance
    print(f"Part 1 ({name}): ")
    print(total)

    # Part 2
    total = 0
    for value in group_one:
        count = group_two.count(value)
        score = int(value) * count
        total += score
    print(f"Part 2 ({name}): ")
    print(total)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.input)
