from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2022, 4, 1
    aoc_input = get_input(year, day)

    lines = aoc_input.rstrip("\n").split("\n")
    total = 0
    for line in lines:
        assign1, assign2 = line.split(",")
        assign1_low, assign1_high = assign1.split("-")
        assign2_low, assign2_high = assign2.split("-")

        if (
            int(assign1_low) <= int(assign2_low)
            and int(assign1_high) >= int(assign2_high)
        ) or (
            int(assign2_low) <= int(assign1_low)
            and int(assign2_high) >= int(assign1_high)
        ):
            total += 1
    print(total)

    submit(total, year, day, level)
