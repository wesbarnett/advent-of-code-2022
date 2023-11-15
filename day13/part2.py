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
    year, day, level = 2022, 13, 2
    aoc_input = get_input(year, day)
    items = [x for x in aoc_input.rstrip("\n").split("\n") if x != ""]
    items.append("[[2]]")
    items.append("[[6]]")

    # Bubble sort
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(items)):
            if compare(eval(items[i]), eval(items[i - 1])):
                items[i - 1], items[i] = items[i], items[i - 1]
                swapped = True

    decoder_key = []
    for i, item in enumerate(items, start=1):
        if item in ["[[2]]", "[[6]]"]:
            decoder_key.append(i)

    ans = decoder_key[0] * decoder_key[1]
    print(ans)
    submit(ans, year, day, level)
