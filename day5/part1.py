from collections import defaultdict

from aoc import get_input, submit


def move(stacks, src, dest):
    item = stacks[src].pop()
    stacks[dest].append(item)


if __name__ == "__main__":
    year, day, level = 2022, 5, 1
    aoc_input = get_input(year, day)

    lines = aoc_input.rstrip("\n").split("\n")

    break_loc = 0
    stacks_raw = []
    for i, line in enumerate(lines):
        if line == "":
            break_loc = i + 1
            break
        line = line.replace("    ", " ")
        line = line.replace("[", "")
        line = line.replace("]", "")
        stacks_raw.append(line)

    stacks = defaultdict(list)
    for i in range(len(stacks_raw) - 2, -1, -1):
        for j, x in enumerate(stacks_raw[i].split(" "), start=1):
            if x != "":
                stacks[j].append(x)

    for line in lines[break_loc:]:
        _, num, _, src, _, dest = line.split(" ")
        for _ in range(int(num)):
            move(stacks, int(src), int(dest))

    ans = "".join([v[-1] for v in stacks.values()])

    print(ans)
    submit(ans, year, day, level)
