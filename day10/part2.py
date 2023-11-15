from aoc import get_input


class Program:
    def __init__(self):
        self.cycle = 0
        self.X = 1
        self.screen = []

    def __call__(self, instruction):
        if instruction == "noop":
            cycles = 1
        elif instruction.startswith("addx"):
            cycles = 2

        for _ in range(cycles):
            if self.cycle % 40 in [self.X - 1, self.X, self.X + 1]:
                self.screen.append("#")
            else:
                self.screen.append(".")
            self.cycle += 1

        if instruction.startswith("addx"):
            self.X += int(instruction.split(" ")[1])


if __name__ == "__main__":
    year, day, level = 2022, 10, 1
    aoc_input = get_input(year, day)
    instructions = aoc_input.rstrip("\n").split("\n")

    program = Program()

    for inst in instructions:
        program(inst)

    for x in range(0, 240, 40):
        print("".join(program.screen[x : x + 40]))
