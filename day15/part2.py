from aoc import get_input, submit


def dist(p1, p2):
    """Manhattan distance."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


if __name__ == "__main__":
    year, day, level = 2022, 15, 2
    aoc_input = get_input(year, day)
    aoc_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

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

    maxc = 20
    dists = []
    perim = set()
    # Find perimiters just outisde the range of each sensor
    for s, b in zip(sensors, beacons):
        print(s)
        d = dist(s, b)
        dists.append(d)

        # top right, incl y mid
        for i in range(d + 1, 0, -1):
            x = s[0] + d - i + 1
            y = s[1] + i
            if x < 0 or x > maxc or y < 0 or y > maxc:
                break
            perim.add((x, y))

        # bot right, incl x and y mid
        for i in range(d + 2):
            x = s[0] + d - i + 1
            y = s[1] - i
            if x < 0 or x > maxc or y < 0 or y > maxc:
                break
            perim.add((x, y))

        # bot left, incl x mid
        for i in range(d, -1, -1):
            x = s[0] - d + i - 1
            y = s[1] - i
            if x < 0 or x > maxc or y < 0 or y > maxc:
                break
            perim.add((x, y))

        # top left
        for i in range(1, d + 1):
            x = s[0] - d + i - 1
            y = s[1] + i
            if x < 0 or x > maxc or y < 0 or y > maxc:
                break
            perim.add((x, y))

    # Find perimiters that are within a sensor's range. If within range
    # then that is not a possible location
    for s, d in zip(sensors, dists):
        for p in list(perim):
            if dist(s, p) <= d:
                perim.remove(p)

    b = list(perim)[0]
    ans = b[0] * 4000000 + b[1]
    print(ans)

    submit(ans, year, day, level)
