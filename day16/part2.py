from itertools import product

from aoc import get_input, submit


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
    year, day, level = 2022, 16, 2
    aoc_input = get_input(year, day)
    lines = aoc_input.rstrip("\n").split("\n")

    valves = []
    valve_graph = {}
    valve_indices = {}
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
        if rates[valve_name] != 0:
            valves.append(valve_name)

    dist = floyd_warshall(valve_graph, valve_indices)

    dp, dt = {}, {}
    for valve in valves:
        time = 26
        time = time - dist[valve_indices["AA"]][valve_indices[valve]] - 1
        pressure = rates[valve] * time
        dp[(valve,)] = pressure
        dt[(valve,)] = time

    dp_all = dict(dp)
    for _ in range(len(valves) - 1):
        dp2, dt2 = {}, {}
        for k, valve in product(dp.keys(), valves):
            if valve not in k:
                time = dt[k]
                pressure = dp[k]
                time = time - dist[valve_indices[k[-1]]][valve_indices[valve]] - 1
                if time >= 0:
                    pressure += rates[valve] * time
                    dp2[*k, valve] = pressure
                    dt2[*k, valve] = time
        dp, dt = dp2, dt2
        dp_all.update(dict(dp))

    dp_all = dict(sorted(dp_all.items(), key=lambda item: item[1], reverse=True))
    max_pressure = float("-inf")
    for (k1, v1), (k2, v2) in product(dp_all.items(), dp_all.items()):
        if v1 * 2 < max_pressure:
            break
        if len(set(k1) & set(k2)) > 0:
            continue
        max_pressure = max(max_pressure, v1 + v2)
    print(max_pressure)
    submit(max_pressure, year, day, level)
