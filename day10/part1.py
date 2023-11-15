from aoc import get_input, submit


class Program:
    def __init__(self):
        self.signal_strength = {}
        self.cycle = 0
        self.X = 1

    def __call__(self, instruction):
        if instruction == "noop":
            cycles = 1
        elif instruction.startswith("addx"):
            cycles = 2

        for _ in range(cycles):
            self.cycle += 1
            self.signal_strength[self.cycle] = self.cycle * self.X

        if instruction.startswith("addx"):
            self.X += int(instruction.split(" ")[1])


if __name__ == "__main__":
    year, day, level = 2022, 10, 1
    aoc_input = get_input(year, day)
    instructions = aoc_input.rstrip("\n").split("\n")

    program = Program()

    for inst in instructions:
        program(inst)

    ans = sum(program.signal_strength[x] for x in [20, 60, 100, 140, 180, 220])
    print(ans)

    submit(ans, year, day, level)
