from aoc import get_input, submit

if __name__ == "__main__":
    year, day = 2022, 2
    aoc_input = get_input(year, day)

    lines = aoc_input.rstrip("\n").split("\n")

    mapper = {
        "A": "Rock",
        "X": "Rock",
        "B": "Paper",
        "Y": "Paper",
        "C": "Scissors",
        "Z": "Scissors",
    }

    total_score = 0

    for line in lines:

        opp, me = line.split(" ")

        score = 0

        if mapper[me] == "Rock":
            score += 1
        elif mapper[me] == "Paper":
            score += 2
        elif mapper[me] == "Scissors":
            score += 3

        if mapper[opp] == mapper[me]:
            score += 3
        elif (
            (mapper[opp] == "Rock" and mapper[me] == "Paper")
            or (mapper[opp] == "Paper" and mapper[me] == "Scissors")
            or (mapper[opp] == "Scissors" and mapper[me] == "Rock")
        ):
            score += 6

        total_score += score

    print(total_score)
    submit(total_score, year, day, level=1)
