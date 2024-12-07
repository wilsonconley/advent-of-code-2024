import typing as t
from pathlib import Path


def read_input_raw(name: t.Literal["sample", "input"] = "input") -> str:
    """Read the entire input file as a raw string."""
    with open(Path(__file__).parent / name, mode="rb") as file:
        return file.read().decode()


def read_input_lines(name: t.Literal["sample", "input"] = "input") -> list[str]:
    """Read the entire input file, separating each line into sequential elements in a list."""
    with open(Path(__file__).parent / name, mode="rb") as file:
        return [line.decode() for line in file.readlines()]


def yield_input_lines(name: t.Literal["sample", "input"] = "input") -> t.Iterable[str]:
    """Yield each line of the input file individually."""
    with open(Path(__file__).parent / name, mode="r", encoding="utf-8") as file:
        yield from file
