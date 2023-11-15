from pathlib import Path

# from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2022, 12, 1
    # aoc_input = get_input(year, day)
    aoc_input = Path("test_input").read_text()

    grid = [list(x) for x in aoc_input.rstrip("\n").split("\n")]

    nrows = len(grid)
    ncols = len(grid[0])
    visited = set()
    step_mapper = {}

    for j, row in enumerate(grid):
        for i, item in enumerate(row):
            if item == "S":
                start = (i, j)
                break

    def move(i, j):
        visited.add((i, j))

        if grid[j][i] == "E":
            return 0

        if (i, j) in step_mapper:
            return step_mapper[(i, j)]

        steps = float("inf")

        for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
            if x >= 0 and y >= 0 and x < ncols and y < nrows and (x, y) not in visited:
                val = ord("z") if grid[y][x] == "E" else ord(grid[y][x])
                if val - ord(grid[j][i]) <= 1:
                    steps = min(move(x, y), steps)

        visited.remove((i, j))
        step_mapper[(i, j)] = steps + 1
        return step_mapper[(i, j)]

    i, j = start
    grid[j][i] = "a"
    print(move(i, j))
    # submit(ans, year, day, level)
