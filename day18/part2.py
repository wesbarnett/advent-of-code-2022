from collections import deque

from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2022, 18, 2
    aoc_input = get_input(year, day)

    cubes = set(
        [
            tuple([int(y) for y in x.split(",")])
            for x in aoc_input.rstrip("\n").split("\n")
        ]
    )

    # create a bounding box to search
    max_x = max(c[0] for c in cubes) + 1
    max_y = max(c[1] for c in cubes) + 1
    max_z = max(c[2] for c in cubes) + 1
    min_x = min(c[0] for c in cubes) - 1
    min_y = min(c[1] for c in cubes) - 1
    min_z = min(c[2] for c in cubes) - 1

    visited = set()

    # start at the minimum
    start = min_x, min_y, min_z
    queue = deque([start])
    visited.add(start)

    surf_area = 0

    # bread-first search
    while queue:
        v = queue.popleft()

        # try moving to any area adjacent to current location (but not diagnolly)
        for x, y, z in [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (-1, 0, 0),
            (0, -1, 0),
            (0, 0, -1),
        ]:
            x_tmp, y_tmp, z_tmp = v[0] + x, v[1] + y, v[2] + z

            # proposed move is a cube, so we know that has an exposed surface to the water
            if (x_tmp, y_tmp, z_tmp) in cubes:
                surf_area += 1
                continue

            # already visited
            if (x_tmp, y_tmp, z_tmp) in visited:
                continue
            visited.add((x_tmp, y_tmp, z_tmp))

            # outside bounding box
            if (
                x_tmp > max_x
                or y_tmp > max_y
                or z_tmp > max_z
                or x_tmp < min_x
                or y_tmp < min_y
                or z_tmp < min_z
            ):
                continue

            queue.append((x_tmp, y_tmp, z_tmp))

    print(surf_area)
    submit(surf_area, year, day, level)
