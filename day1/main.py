from argparse import ArgumentParser
from pathlib import Path

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-i", "--infile", required=False, type=Path, default=Path("input")
    )
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n\n")
    print(max([sum(int(z) for z in y) for y in [x.split("\n") for x in lines]]))

    print(
        sum(
            sorted(
                [sum(int(z) for z in y) for y in [x.split("\n") for x in lines]],
                reverse=True,
            )[:3]
        )
    )
