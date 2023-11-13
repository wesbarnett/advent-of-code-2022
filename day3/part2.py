import string

from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2022, 3, 2
    aoc_input = get_input(year, day)

    lines = aoc_input.rstrip("\n").split("\n")

    total_priority = 0

    priority = {
        **{x: i for i, x in enumerate(string.ascii_lowercase, start=1)},
        **{x: i for i, x in enumerate(string.ascii_uppercase, start=27)},
    }

    for i in range(0, len(lines), 3):
        inter = set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])
        total_priority += priority[str(*inter)]

    print(total_priority)

    submit(total_priority, year, day, level)
