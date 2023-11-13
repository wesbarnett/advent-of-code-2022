import os
from pathlib import Path
from urllib import parse, request


def get_input(year, day):
    basepath = Path(f"{os.environ['HOME']}/.cache/aoc")
    basepath.mkdir(parents=True, exist_ok=True)
    p = basepath / f"infile_{year}_{day}"
    try:
        aoc_input = p.read_text()
    except FileNotFoundError:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        headers = {"Cookie": f"session={os.environ['AOC_COOKIE']}"}
        req = request.Request(url, headers=headers)
        with request.urlopen(req) as response:
            aoc_input = response.read().decode("utf-8")
            p.write_text(aoc_input)
    return aoc_input


def submit(answer, year, day, level):
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    headers = {"Cookie": f"session={os.environ['AOC_COOKIE']}"}
    req = request.Request(url, headers=headers)
    data = parse.urlencode({"level": level, "answer": answer}).encode()
    req = request.Request(url, data=data, headers=headers)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
