from aoc import get_input, submit


def compare(left, right):

    for l, r in zip(left, right):
        if isinstance(l, int) and isinstance(r, list):
            return compare([l], r)
        elif isinstance(l, list) and isinstance(r, int):
            return compare(l, [r])
        elif isinstance(l, list) and isinstance(r, list):
            val = compare(l, r)
            if val is not None:
                return val
        elif l < r:
            return True
        elif l == r:
            continue
        elif l > r:
            return False

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False
    else:
        return None


if __name__ == "__main__":
    year, day, level = 2022, 13, 1
    aoc_input = get_input(year, day)
    pairs = aoc_input.rstrip("\n").split("\n\n")

    ans = 0
    for i, x in enumerate(pairs, start=1):
        left, right = x.split("\n")
        if compare(eval(left), eval(right)):
            ans += i

    print(ans)
    submit(ans, year, day, level)
