from aoc import get_input, submit


def dist(p1, p2):
    """Manhattan distance."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


if __name__ == "__main__":
    year, day, level = 2022, 15, 2
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

    maxc = 4000000
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
        print(s, d, len(list(perim)))
        if len(list(perim)) == 1:
            break
        for p in list(perim):
            if dist(s, p) <= d:
                perim.remove(p)

    b = list(perim)[0]
    print(b)
    ans = b[0] * 4000000 + b[1]
    print(ans)

    submit(ans, year, day, level)
