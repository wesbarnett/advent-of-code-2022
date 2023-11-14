from collections import defaultdict

from aoc import get_input  # , submit

if __name__ == "__main__":
    year, day, level = 2022, 8, 2
    aoc_input = get_input(year, day)
    lines = aoc_input.rstrip("\n").split("\n")

    forest = []
    for line in lines:
        forest.append([int(x) for x in line])

    score_map = defaultdict(lambda: 0)

    nrows, ncols = len(forest), len(forest[0])

    for j in range(nrows):
        row = forest[j]
        for i, tree in enumerate(row):

            score = 0
            for k in range(i - 1, -1, -1):
                score += 1
                if row[k] >= tree:
                    break
            score_map[(i, j)] = score

            score = 0
            for k in range(i + 1, ncols, 1):
                score += 1
                if row[k] >= tree:
                    break
            score_map[(i, j)] *= score

    for i in range(ncols):
        column = [x[i] for x in forest]
        for j, tree in enumerate(column):

            score = 0
            for k in range(i - 1, -1, -1):
                score += 1
                if column[k] >= tree:
                    break
            score_map[(i, j)] *= score

            score = 0
            for k in range(i + 1, nrows, 1):
                score += 1
                if row[k] >= tree:
                    break
            score_map[(i, j)] *= score

    ans = max(score_map.values())
    print(ans)
    # submit(ans, year, day, level)
