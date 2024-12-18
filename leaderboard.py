import os

import pandas as pd  # type: ignore[import-untyped]
import requests  # type: ignore[import-untyped]


def get_leaderboard() -> pd.DataFrame:
    session = requests.Session()
    resp = session.get(
        "https://adventofcode.com/2024/leaderboard/private/view/2794065.json",
        cookies={
            "session": "53616c7465645f5f3c672680ac8250fe181f7c00a4ff40d22105432f97baf9c1bb884a5d2a1f6133dd7c3179f4fe149c1c2409c52ef2f8e9ea5adc6c85cb6d5d"  # pylint: disable=line-too-long
        },
    )
    resp_json = resp.json()

    columns = ["name", "stars"] + [str(x) for x in range(1, 26)]
    table_dict: dict[str, list[str]] = {}
    for col in columns:
        table_dict[col] = []

    for _, user in resp_json["members"].items():
        table_dict["name"].append(user["name"])
        for day in range(1, 26):
            num_star = len(user["completion_day_level"].get(str(day), {}).keys())
            star_str = "*" * num_star + " " * (2 - num_star)
            table_dict[str(day)].append(star_str)
        table_dict["stars"].append(user["stars"])

    df = pd.DataFrame(table_dict)
    df = df.sort_values("stars", axis=0, ascending=False)
    df.index += 1

    return df


def write_table_to_md(df: pd.DataFrame) -> None:
    output = str(df)
    with open("README.md", "r", encoding="utf-8") as file_in:
        with open("tmp.md", "w", encoding="utf-8") as file_out:
            overwrite = False
            for line in file_in:
                if not overwrite:
                    file_out.write(line)
                    if "```leaderboard" in line:
                        overwrite = True
                else:
                    if line.strip() == "```":
                        overwrite = False
                        file_out.write(output + "\n")
                        file_out.write(line)

    os.unlink("README.md")
    os.rename("tmp.md", "README.md")


if __name__ == "__main__":
    leaderboard = get_leaderboard()
    write_table_to_md(leaderboard)
