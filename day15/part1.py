from aoc import get_input, submit


def dist(p1, p2):
    """Manhattan distance."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


if __name__ == "__main__":
    year, day, level = 2022, 15, 1
    aoc_input = get_input(year, day)

    lines = aoc_input.rstrip("\n").split("\n")

    sensors = []
    beacons = []
    nobeacons = set()
    for line in lines:
        s, b = line.split(":")
        s = s.removeprefix("Sensor at ")
        s = [int(x[2:]) for x in s.split(", ")]
        b = b.removeprefix(" closest beacon is at ")
        b = [int(x[2:]) for x in b.split(", ")]
        sensors.append(tuple(s))
        beacons.append(tuple(b))

    row = 2000000
    for s, b in zip(sensors, beacons):
        d = dist(s, b)

        for i in range(d + 1):

            xstart = s[0] - d + i
            xend = s[0] + d - i + 1

            y = s[1] - i
            if y == row:
                for x in range(xstart, xend):
                    if b != (x, y):
                        nobeacons.add((x, y))

            y = s[1] + i
            if y == row:
                for x in range(xstart, xend):
                    if b != (x, y):
                        nobeacons.add((x, y))

    count = sum(1 for _, y in nobeacons if y == row)
    print(count)
    submit(count, year, day, level)
