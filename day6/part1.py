from aoc import get_input, submit


def find_marker(buffer):
    for i in range(4, len(buffer)):
        seq = buffer[i - 4 : i]
        if len(seq) == len(set(seq)):
            return i


if __name__ == "__main__":
    year, day, level = 2022, 6, 1
    aoc_input = get_input(year, day).rstrip("\n")

    ans = find_marker(aoc_input)

    print(ans)
    submit(ans, year, day, level)
