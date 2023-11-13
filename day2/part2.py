from aoc import get_input, submit

if __name__ == "__main__":
    year, day = 2022, 2
    aoc_input = get_input(year, day)

    lines = aoc_input.rstrip("\n").split("\n")

    mapper = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }

    total_score = 0

    for line in lines:

        opp, me = line.split(" ")

        score = 0

        if me == "X":
            if mapper[opp] == "Rock":
                choice = "Scissors"
            elif mapper[opp] == "Paper":
                choice = "Rock"
            elif mapper[opp] == "Scissors":
                choice = "Paper"
        elif me == "Y":
            if mapper[opp] == "Rock":
                choice = "Rock"
            elif mapper[opp] == "Paper":
                choice = "Paper"
            elif mapper[opp] == "Scissors":
                choice = "Scissors"
            score += 3
        elif me == "Z":
            if mapper[opp] == "Rock":
                choice = "Paper"
            elif mapper[opp] == "Paper":
                choice = "Scissors"
            elif mapper[opp] == "Scissors":
                choice = "Rock"
            score += 6

        if choice == "Rock":
            score += 1
        elif choice == "Paper":
            score += 2
        elif choice == "Scissors":
            score += 3

        total_score += score

    print(total_score)
    submit(total_score, year, day, level=2)
