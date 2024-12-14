import typing as t
from pathlib import Path


def input_path(day: str, input_type: str) -> Path:
    """Construct the file path to the day's input."""
    return Path(__file__).parent / day / input_type


def read_input_raw(path: Path) -> str:
    """Read the entire input file as a raw string."""
    with open(path, mode="rb") as file:
        return file.read().decode()


def read_input_lines(path: Path) -> list[str]:
    """Read the entire input file, separating each line into sequential elements in a list."""
    with open(path, mode="rb") as file:
        return [line.decode() for line in file.readlines()]


def yield_input_lines(path: Path) -> t.Iterable[str]:
    """Yield each line of the input file individually."""
    with open(path, mode="r", encoding="utf-8") as file:
        yield from file
