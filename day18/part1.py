from operator import itemgetter

from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2022, 18, 1
    aoc_input = get_input(year, day)

    cubes = [
        tuple([int(y) for y in x.split(",")])
        for x in aoc_input.rstrip("\n").split("\n")
    ]
    sides = {c: 6 for c in cubes}

    xy = itemgetter(0, 1)
    yz = itemgetter(1, 2)
    xz = itemgetter(0, 2)
    x = itemgetter(0)
    y = itemgetter(1)
    z = itemgetter(2)

    for i in range(len(cubes) - 1):
        for j in range(i + 1, len(cubes)):
            if (
                (xy(cubes[i]) == xy(cubes[j]) and abs(z(cubes[i]) - z(cubes[j])) == 1)
                or (
                    yz(cubes[i]) == yz(cubes[j]) and abs(x(cubes[i]) - x(cubes[j])) == 1
                )
                or (
                    xz(cubes[i]) == xz(cubes[j]) and abs(y(cubes[i]) - y(cubes[j])) == 1
                )
            ):
                sides[cubes[i]] -= 1
                sides[cubes[j]] -= 1

    surf_area = sum(v for v in sides.values())

    submit(surf_area, year, day, level)
