from aoc import get_input  # , submit

if __name__ == "__main__":
    year, day, level = 2022, 9, 1
    aoc_input = get_input(year, day)
    lines = aoc_input.rstrip("\n").split("\n")

    head = [0, 0]
    tail = [0, 0]

    nlocs = 0
    for line in lines:
        d, m = line.split(" ")
        m = int(m)

        if d == "L":
            head[0] -= m
        elif d == "R":
            head[0] += m
        elif d == "U":
            head[1] += m
        elif d == "D":
            head[1] -= m

        # same location or adjacent
        if (
            (tail == head)
            or (tail[0] == head[0] - 1 and tail[1] == head[1])
            or (tail[0] == head[0] + 1 and tail[1] == head[1])
            or (tail[0] == head[0] and tail[1] == head[1] - 1)
            or (tail[0] == head[0] and tail[1] == head[1] + 1)
            or (tail[0] == head[0] + 1 and tail[1] == head[1] + 1)
            or (tail[0] == head[0] - 1 and tail[1] == head[1] - 1)
            or (tail[0] == head[0] + 1 and tail[1] == head[1] - 1)
            or (tail[0] == head[0] - 1 and tail[1] == head[1] + 1)
        ):
            continue
        elif tail[0] == head[0] and tail[1] == head[1] + 2:
            tail[1] -= 1
        elif tail[0] == head[0] and tail[1] == head[1] - 2:
            tail[1] += 1
        elif tail[0] == head[0] + 2 and tail[1] == head[1]:
            tail[0] -= 1
        elif tail[0] == head[0] - 2 and tail[1] == head[1]:
            tail[0] += 1
        elif head[0] > tail[0] and head[1] > tail[1]:
            tail[0] += 1
            tail[1] += 1
        elif head[0] < tail[0] and head[1] > tail[1]:
            tail[0] -= 1
            tail[1] += 1
        elif head[0] < tail[0] and head[1] < tail[1]:
            tail[0] -= 1
            tail[1] -= 1
        elif head[0] > tail[0] and head[1] < tail[1]:
            tail[0] += 1
            tail[1] -= 1

        nlocs += 1

    print(nlocs)
    # submit(nlocs, year, day, level)
