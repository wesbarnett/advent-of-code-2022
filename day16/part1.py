from itertools import permutations, product

from aoc import get_input  # , submit


def floyd_warshall(graph, indices):
    n = len(indices)
    dist = [[float("inf") for _ in range(n)] for _ in range(n)]

    for k in graph.keys():
        dist[indices[k]][indices[k]] = 0

    for k, vals in graph.items():
        for v in vals:
            dist[indices[k]][indices[v]] = 1

    for k, i, j in product(range(n), range(n), range(n)):
        if dist[i][j] > dist[i][k] + dist[k][j]:
            dist[i][j] = dist[i][k] + dist[k][j]
    return dist


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
    valve_graph = {}
    valve_list = []
    valve_indices = {}
    unvisited = set()
    rates = {}

    for i, line in enumerate(lines):
        first, sec = line.split("; ")
        valve_name = first.split(" ")[1]
        neighbs = sec.removeprefix("tunnels lead to valves ").split(", ")
        rates[valve_name] = int(first.split(" ")[-1].removeprefix("rate="))
        if len(neighbs) == 1:
            neighbs = [sec.removeprefix("tunnel leads to valve ")]
        valve_graph[valve_name] = neighbs
        valve_indices[valve_name] = i
        valves[i] = valve_name
        if rates[valve_name] != 0:
            valve_list.append(valve_name)

    dist = floyd_warshall(valve_graph, valve_indices)

    max_pressure = float("-inf")
    for perm in permutations(valve_list):
        time = 30
        valve = "AA"
        pressure = 0
        for new_valve in perm:
            time = time - dist[valve_indices[valve]][valve_indices[new_valve]] - 1
            if time <= 0:
                break
            pressure += rates[new_valve] * time
            valve = new_valve
        if pressure > max_pressure:
            max_pressure = pressure

    print(max_pressure)
    # submit(count, year, day, level)
