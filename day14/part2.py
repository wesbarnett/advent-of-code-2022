from aoc import get_input, submit


def sim_sand(grid, min_y):

    nsand = 0
    while True:
        x, y = 500, 0
        while True:
            # try directly below
            if (x, y + 1) not in grid and y + 1 < min_y:
                y += 1
            # try to the left
            elif (x - 1, y + 1) not in grid and y + 1 < min_y:
                x -= 1
                y += 1
            # try to the right
            elif (x + 1, y + 1) not in grid and y + 1 < min_y:
                x += 1
                y += 1
            # no options, rest here
            else:
                grid.add((x, y))
                nsand += 1
                # block source
                if (x, y) == (500, 0):
                    return nsand
                break


if __name__ == "__main__":
    year, day, level = 2022, 14, 2
    aoc_input = get_input(year, day)

    paths = aoc_input.rstrip("\n").split("\n")
    grid = set()

    for path in paths:
        points = path.split(" -> ")
        for i in range(1, len(points)):
            p1 = tuple([int(x) for x in points[i - 1].split(",")])
            p2 = tuple([int(x) for x in points[i].split(",")])
            grid.add(p1)
            grid.add(p2)
            for j in range(p1[0], p2[0]):
                grid.add((j, p1[1]))
            for j in range(p1[1], p2[1]):
                grid.add((p1[0], j))
            for j in range(p1[0], p2[0], -1):
                grid.add((j, p1[1]))
            for j in range(p1[1], p2[1], -1):
                grid.add((p1[0], j))

    min_y = float("-inf")
    for x, y in grid:
        if y > min_y:
            min_y = y

    min_y += 2

    nsand = sim_sand(grid, min_y)
    print(nsand)
    submit(nsand, year, day, level)
