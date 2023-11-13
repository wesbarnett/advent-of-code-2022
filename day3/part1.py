import string

from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2022, 3, 1
    aoc_input = get_input(year, day)

    lines = aoc_input.rstrip("\n").split("\n")

    total_priority = 0

    priority = {
        **{x: i for i, x in enumerate(string.ascii_lowercase, start=1)},
        **{x: i for i, x in enumerate(string.ascii_uppercase, start=27)},
    }

    for line in lines:
        mid = len(line) // 2
        first, sec = set(line[:mid]), set(line[mid:])
        dup = first & sec
        total_priority += priority[str(*dup)]

    print(total_priority)

    submit(total_priority, year, day, level)
