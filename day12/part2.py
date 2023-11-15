from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2022, 12, 2
    aoc_input = get_input(year, day)

    grid = [list(x) for x in aoc_input.rstrip("\n").split("\n")]

    nrows, ncols = len(grid), len(grid[0])

    starts = []
    for j, row in enumerate(grid):
        for i, item in enumerate(row):
            if item in ["S", "a"]:
                starts.append((i, j))
            if item == "E":
                dest = (i, j)

    ans = []
    for start in starts:

        tent_dist = {}
        unvisited = set()

        for y, row in enumerate(grid):
            for x, item in enumerate(row):
                unvisited.add((x, y))
                tent_dist[(x, y)] = float("inf")

        i, j = start
        grid[j][i] = "a"
        tent_dist[(i, j)] = 0

        while dest in unvisited:
            for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                if (
                    x >= 0
                    and y >= 0
                    and x < ncols
                    and y < nrows
                    and (x, y) in unvisited
                ):
                    val = ord("z") if grid[y][x] == "E" else ord(grid[y][x])
                    if val - ord(grid[j][i]) <= 1:
                        tent_dist[(x, y)] = min(
                            tent_dist[(x, y)], tent_dist[(i, j)] + 1
                        )
                    else:
                        tent_dist[(x, y)] = min(
                            tent_dist[(x, y)], tent_dist[(i, j)] + float("inf")
                        )
            unvisited.remove((i, j))

            min_tent_dist = float("inf")
            for x, y in unvisited:
                if tent_dist[(x, y)] < min_tent_dist:
                    i, j = x, y
                    min_tent_dist = tent_dist[(x, y)]

            if min_tent_dist == float("inf"):
                break

        ans.append(tent_dist[dest])

    ans = min(ans)
    print(ans)
    submit(ans, year, day, level)
