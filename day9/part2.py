from collections import defaultdict

from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2022, 9, 2
    aoc_input = get_input(year, day)
    lines = aoc_input.rstrip("\n").split("\n")

    rope = [[0, 0] for _ in range(10)]

    tail_pos = defaultdict(lambda: False)
    tail_pos[tuple(rope[-1])] = True

    for line in lines:
        d, m = line.split(" ")
        m = int(m)

        for _ in range(m):

            if d == "L":
                rope[0][0] -= 1
            elif d == "R":
                rope[0][0] += 1
            elif d == "U":
                rope[0][1] += 1
            elif d == "D":
                rope[0][1] -= 1

        for i in range(9):

            head = rope[i]
            tail = rope[i + 1]

            if abs(tail[0] - head[0]) in [0, 1] and abs(tail[1] - head[1]) in [0, 1]:
                continue
            elif tail[0] == head[0] and tail[1] == (head[1] + 2):
                tail[1] = head[1] + 1
            elif tail[0] == head[0] and tail[1] == (head[1] - 2):
                tail[1] = head[1] - 1
            elif tail[0] == (head[0] + 2) and tail[1] == head[1]:
                tail[0] = head[0] + 1
            elif tail[0] == (head[0] - 2) and tail[1] == head[1]:
                tail[0] = head[0] - 1
            elif head[0] > tail[0] and head[1] > tail[1]:
                tail[0] += 1
                tail[1] += 1
            elif head[0] < tail[0] and head[1] > tail[1]:
                tail[0] -= 1
                tail[1] += 1
            elif head[0] < tail[0] and head[1] < tail[1]:
                tail[0] -= 1
                tail[1] -= 1
            elif head[0] > tail[0] and head[1] < tail[1]:
                tail[0] += 1
                tail[1] -= 1

            if i == 8:
                tail_pos[tuple(tail)] = True

    ans = sum(tail_pos.values())
    print(ans)
    submit(ans, year, day, level)
