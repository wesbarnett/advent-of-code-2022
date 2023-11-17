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
    year, day, level = 2022, 17, 1
    aoc_input = get_input(year, day)
    wind = cycle(list(aoc_input.rstrip("\n")))
    shapes = cycle(range(5))

    filled = set()
    for x in range(1, 8):
        filled.add((x, 0))

    max_y = 0
    for _ in range(2022):
        rock = Rock(shape=next(shapes), x=0, y=max_y)
        while True:
            w = next(wind)
            if not rock(w, filled):
                # rock is at rest
                for r in rock.loc:
                    max_y = max(r[1], max_y)
                    filled.add(tuple(r))
                break

    print(max_y)
    submit(max_y, year, day, level)
