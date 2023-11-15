from collections import deque

from aoc import get_input, submit


class Monkey:
    def __init__(self, num, items, op, divisor, true_monkey, false_monkey):
        self.items = deque(items)
        self.num = num
        self.op_exp = op
        self.divisor = divisor
        self.count = 0
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def op(self, old):
        return eval(self.op_exp)

    def test(self, worry):
        if worry % self.divisor == 0:
            return self.true_monkey
        else:
            return self.false_monkey

    def __call__(self, monkeys):
        while self.items:
            item = self.items.popleft()
            worry = self.op(item)
            worry = worry // 3
            target_monkey = self.test(worry)
            monkeys[target_monkey].items.append(worry)
            self.count += 1


if __name__ == "__main__":
    year, day, level = 2022, 11, 1
    aoc_input = get_input(year, day)

    monkeys = []
    for x in aoc_input.rstrip("\n").split("\n\n"):

        lines = x.split("\n")
        num = lines[0].split(" ")[1].rstrip(":")
        items = [int(x.lstrip(" ")) for x in lines[1].split(":")[1].split(",")]
        op = lines[2].split(":")[1].lstrip(" ").split("=")[1]
        divisor = int(lines[3].split(" ")[-1])
        true_monkey = int(lines[4].split(" ")[-1])
        false_monkey = int(lines[5].split(" ")[-1])

        monkeys.append(Monkey(num, items, op, divisor, true_monkey, false_monkey))

    for _ in range(20):
        for monkey in monkeys:
            monkey(monkeys)

    ans = 1
    for x in sorted([m.count for m in monkeys])[-2:]:
        ans *= x

    print(ans)
    submit(ans, year, day, level)
