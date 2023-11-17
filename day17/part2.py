from copy import deepcopy
from itertools import cycle

from aoc import get_input, submit


class Rock:
    def __init__(self, shape, x, y):
        """
        Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units
        above the highest rock in the room (or the floor, if there isn't one).
        """
        if shape == 0:
            """
            3456
            #### 4
            """
            self.loc = [
                [x + 3, y + 4],
                [x + 4, y + 4],
                [x + 5, y + 4],
                [x + 6, y + 4],
            ]
        elif shape == 1:
            """
            345
            .#. 6
            ### 5
            .#. 4
            """
            self.loc = [
                [x + 4, y + 6],
                [x + 3, y + 5],
                [x + 4, y + 5],
                [x + 5, y + 5],
                [x + 4, y + 4],
            ]
        elif shape == 2:
            """
            345
            ..# 6
            ..# 5
            ### 4
            """
            self.loc = [
                [x + 5, y + 6],
                [x + 5, y + 5],
                [x + 3, y + 4],
                [x + 4, y + 4],
                [x + 5, y + 4],
            ]
        elif shape == 3:
            """
            3
            # 7
            # 6
            # 5
            # 4
            """
            self.loc = [
                [x + 3, y + 7],
                [x + 3, y + 6],
                [x + 3, y + 5],
                [x + 3, y + 4],
            ]
        elif shape == 4:
            """
            34
            ## 5
            ## 4
            """
            self.loc = [
                [x + 3, y + 5],
                [x + 4, y + 5],
                [x + 3, y + 4],
                [x + 4, y + 4],
            ]
        else:
            raise ValueError("shape must be an integer 0 through 4")

    def __call__(self, wind, filled):
        new_loc = deepcopy(self.loc)

        if wind == ">":
            for r in new_loc:
                r[0] += 1
                # hit wall or rock, reject movement
                if r[0] > 7 or tuple(r) in filled:
                    new_loc = deepcopy(self.loc)
                    break

        elif wind == "<":
            for r in new_loc:
                r[0] -= 1
                # hit wall, reject movement
                if r[0] < 1 or tuple(r) in filled:
                    new_loc = deepcopy(self.loc)
                    break

        self.loc = deepcopy(new_loc)

        self.new_loc = deepcopy(self.loc)
        for r in new_loc:
            r[1] -= 1
            # hit bottom (rock or floor), reject move
            if tuple(r) in filled:
                return False

        self.loc = deepcopy(new_loc)
        return True


if __name__ == "__main__":
    year, day, level = 2022, 17, 2
    aoc_input = get_input(year, day)
    wind = list(aoc_input.rstrip("\n"))
    wind_index = cycle(range(len((wind))))
    max_iter = 1000000000000

    shapes = cycle(range(5))

    filled = set()
    col_heights = [0] * 7
    col_heights_shifted = [0] * 7
    states = {}

    for x in range(1, 8):
        filled.add((x, 0))

    max_y = 0
    max_y_all = []
    for n in range(max_iter):
        shape = next(shapes)
        rock = Rock(shape=shape, x=0, y=max_y)
        while True:
            wi = next(wind_index)
            if not rock(wind[wi], filled):
                # rock is at rest
                for r in rock.loc:
                    max_y = max(r[1], max_y)
                    filled.add(tuple(r))
                    col_heights[r[0] - 1] = max(r[1], col_heights[r[0] - 1])

                col_heights_min = min(col_heights)
                for i in range(len(col_heights)):
                    col_heights_shifted[i] = col_heights[i] - col_heights_min
                break

        max_y_all.append(max_y)

        # "state" of the tunnel is the shape of the rock, the location in the
        # wind stream, and the topology of the heighest points
        state = shape, wi, tuple(col_heights_shifted)

        # cycle detected
        if state in states:
            cycle_length = n - states[state]
            max_y_all.pop()
            max_y = max_y_all[-1]
            break

        states[state] = n

    max_y += (max_y_all[-1] - max_y_all[-cycle_length - 1]) * (
        (max_iter - n) // cycle_length
    )

    cycler = cycle(range(cycle_length, 0, -1))
    for _ in range((max_iter - n) % cycle_length):
        step_back = next(cycler)
        max_y += max_y_all[-step_back] - max_y_all[-step_back - 1]
    print(max_y)
    submit(max_y, year, day, level)
