import argparse
import typing as t

import util

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
    print(f"Part 1 ({name}): ")

    # Part 2
    print(f"Part 2 ({name}): ")


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.input)
