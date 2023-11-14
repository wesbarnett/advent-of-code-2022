from collections import defaultdict

from aoc import get_input  # , submit

if __name__ == "__main__":
    year, day, level = 2022, 8, 1
    aoc_input = get_input(year, day)
    lines = aoc_input.rstrip("\n").split("\n")

    forest = []
    for line in lines:
        forest.append([int(x) for x in line])

    visible_map = defaultdict(lambda: False)

    for j in range(len(forest)):
        row = forest[j]
        # Scan row left to right
        max_height = 0
        for i, tree in enumerate(row):
            if tree > max_height:
                max_height = tree
                visible_map[(i, j)] = True

        # Scan row right to left
        max_height = 0
        for i, tree in reversed(list(enumerate(row))):
            if tree > max_height:
                max_height = tree
                visible_map[(i, j)] = True

    for i in range(len(forest[0])):

        column = [x[i] for x in forest]
        # Scan col top to bottom
        max_height = 0
        for j, tree in enumerate(column):
            if tree > max_height:
                max_height = tree
                visible_map[(i, j)] = True

        # Scan col bottom to top
        max_height = 0
        for j, tree in reversed(list(enumerate(column))):
            if tree > max_height:
                max_height = tree
                visible_map[(i, j)] = True

    visible_trees = sum(k for k in visible_map.values())
    print(visible_trees)

    # submit(visible_trees, year, day, level)
