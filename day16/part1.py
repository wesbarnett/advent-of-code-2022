from enum import Enum, auto

from aoc import get_input  # , submit


class ValveState(Enum):
    OPEN = auto()
    CLOSED = auto()


class Valve:
    def __init__(self, name, rate, neighbs=None):
        self.name = name
        self.rate = rate
        if neighbs is None:
            self.neighbs = []
        else:
            self.neighbs = neighbs
        self.state = ValveState.CLOSED

    def __repr__(self):
        return f"Valve(name={self.name}, rate={self.rate}, neighbs={self.neighbs}, state={self.state})"


if __name__ == "__main__":
    year, day, level = 2022, 16, 1
    aoc_input = get_input(year, day)
    aoc_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""
    lines = aoc_input.rstrip("\n").split("\n")
    valves = {}
    for line in lines:
        first, sec = line.split("; ")
        valve_name = first.split(" ")[1]
        rate = int(first.split(" ")[-1].removeprefix("rate="))
        valves[valve_name] = Valve(valve_name, rate)

    for line in lines:
        first, sec = line.split("; ")
        valve_name = first.split(" ")[1]
        neighbs = sec.removeprefix("tunnels lead to valves ").split(", ")
        if len(neighbs) == 1:
            neighbs = [sec.removeprefix("tunnel leads to valve ")]
        print([valves[n] for n in neighbs])
        valves[valve_name].neighbs = [valves[n] for n in neighbs]

    time = 30

    def traverse(valve):
        global time
        print(valve.name)
        print(time)
        time -= 1
        if time <= 0:
            return 0

        if valve.rate > 0 and valve.state == ValveState.CLOSED:
            valve.state = ValveState.OPEN
            time -= 1
            if time <= 0:
                return 0

        if valve.state == ValveState.OPEN:
            pressure = time * valve.rate
        else:
            pressure = 0

        for n in valve.neighbs:
            pressure += traverse(n)

        return pressure

    print(traverse(valves["AA"]))

    # submit(count, year, day, level)
