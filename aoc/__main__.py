import importlib
import re
import typer
from enum import Enum

app = typer.Typer()


class InputType(Enum):
    SAMPLE = "sample"
    INPUT = "input"


@app.command()
def solve(
    day: str = typer.Argument(help="The day to solve. e.g., 'day_01'"),
    input_type: InputType = typer.Option(
        "input",
        help=(
            "The input type to use, either 'sample' for the example provided in the problem "
            "or 'input' for the actual puzzle input."
        ),
    ),
):
    """Solve the day's puzzle."""
    if not re.match("day_\d\d", day):
        raise ValueError("`day` argument must be in format `day_\d\d`!")
    module = importlib.import_module(f".{day}", __package__)
    module.solve(input_type.value)


if __name__ == "__main__":
    app()
