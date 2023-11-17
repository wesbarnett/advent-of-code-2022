from copy import deepcopy

from aoc import get_input  # , submit


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

    def __call__(self, wind, bot):
        new_loc = deepcopy(self.loc)

        if wind == ">":
            for r in new_loc:
                r[0] += 1
                # hit wall, reject movement
                if r[0] > 7:
                    new_loc = deepcopy(self.loc)
                    break

        elif wind == "<":
            for r in new_loc:
                r[0] -= 1
                # hit wall, reject movement
                if r[0] < 1:
                    new_loc = deepcopy(self.loc)
                    break

        self.loc = deepcopy(new_loc)

        self.new_loc = deepcopy(self.loc)
        for r in new_loc:
            r[1] -= 1
            # hit bottom (rock or floor), reject move
            if r[1] <= bot:
                return False

        self.loc = deepcopy(new_loc)
        return True


if __name__ == "__main__":
    year, day, level = 2022, 17, 1
    aoc_input = get_input(year, day)
    wind = aoc_input.rstrip("\n")
    wind = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

    rock = Rock(shape=0, x=0, y=0)

    for w in wind:
        if not rock(w, bot=0):
            break

    print(rock.loc)

    # submit(max_pressure, year, day, level)
