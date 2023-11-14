from aoc import get_input, submit


def find_marker(buffer, seq_len=14):
    for i in range(seq_len, len(buffer)):
        seq = buffer[i - seq_len : i]
        if len(seq) == len(set(seq)):
            return i


if __name__ == "__main__":
    year, day, level = 2022, 6, 2
    aoc_input = get_input(year, day).rstrip("\n")

    ans = find_marker(aoc_input)

    print(ans)
    submit(ans, year, day, level)
