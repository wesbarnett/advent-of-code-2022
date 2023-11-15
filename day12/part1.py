from pathlib import Path

# from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2022, 12, 1
    # aoc_input = get_input(year, day)
    aoc_input = Path("test_input").read_text()

    grid = [list(x) for x in aoc_input.rstrip("\n").split("\n")]

    nrows = len(grid)
    ncols = len(grid[0])
    for j, row in enumerate(grid):
        for i, item in enumerate(row):
            if item == "S":
                start = (i, j)

    steps = {}
    visited = set()

    i, j = start

    def move(i, j):
        cur = grid[j][i]
        visited.add((i, j))
        print(i, j)
        print(cur)

        if (i, j) in steps:
            return steps[(i, j)]

        if cur == "E":
            steps[(i, j)] = 0
            return steps[(i, j)]

        if cur == "S":
            cur = "a"

        if j + 1 < nrows and (i, j + 1) not in visited:
            up = grid[j + 1][i]
            if ord(up) - ord(cur) <= 1:
                steps_up = move(i, j + 1)
            else:
                steps_up = float("inf")
        else:
            steps_up = float("inf")

        if j - 1 >= 0 and (i, j - 1) not in visited:
            down = grid[j - 1][i]
            if ord(down) - ord(cur) <= 1:
                steps_down = move(i, j - 1)
            else:
                steps_down = float("inf")
        else:
            steps_down = float("inf")

        if i + 1 < ncols and (i + 1, j) not in visited:
            right = grid[j][i + 1]
            if ord(right) - ord(cur) <= 1:
                steps_right = move(i + 1, j)
            else:
                steps_right = float("inf")
        else:
            steps_right = float("inf")

        if i - 1 >= 0 and (i - 1, j) not in visited:
            left = grid[j][i - 1]
            if ord(left) - ord(cur) <= 1:
                steps_left = move(i - 1, j)
            else:
                steps_left = float("inf")
        else:
            steps_left = float("inf")

        steps[(i, j)] = min(steps_up, steps_down, steps_right, steps_left) + 1
        print(steps[(i, j)])
        return steps[(i, j)]

    steps = move(i, j)
    print(steps)
    # submit(ans, year, day, level)
