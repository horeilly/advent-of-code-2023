def read_input() -> list[str]:
    with open("../data/17_clumsy_crucibles.txt", "r") as f:
        text = f.read().split("\n")
    text = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".split("\n")
    return text


def build_graph(text: list[str]) -> dict[tuple, list[dict[str, int]]]:
    graph = {}
    for i in range(len(text)):
        for j in range(len(text[i])):
            if (i, j) not in graph:
                graph[(i, j)] = []
            for d in [1, 2, 3]:
                if i - d >= 0:
                    try:
                        graph[(i, j)].append({
                            "node": (i - d, j),
                            "weight": sum([int(text[i - k][j]) for k in range(1, d + 1)])
                        })
                    except IndexError:
                        pass
                if j - d >= 0:
                    try:
                        graph[(i, j)].append({
                            "node": (i, j - d),
                            "weight": sum([int(text[i][j - k]) for k in range(1, d + 1)])
                        })
                    except IndexError:
                        pass
                if i + d < len(text):
                    try:
                        graph[(i, j)].append({
                            "node": (i + d, j),
                            "weight": sum([int(text[i + k][j]) for k in range(1, d + 1)])
                        })
                    except IndexError:
                        pass
                if j + d < len(text[i]):
                    try:
                        graph[(i, j)].append({
                            "node": (i, j + d),
                            "weight": sum([int(text[i][j + k]) for k in range(1, d + 1)])
                        })
                    except IndexError:
                        pass

    return graph


def dijkstra(graph: dict[tuple, list[dict[str, int]]], start: tuple) -> dict[tuple, int]:
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = [start]
    path = []
    while queue:
        current = queue.pop(0)
        for neighbour in graph[current]:
            distance = distances[current] + neighbour["weight"]
            if distance < distances[neighbour["node"]]:
                distances[neighbour["node"]] = distance
                queue.append(neighbour["node"])
    return distances


def main() -> None:
    text_input = read_input()
    graph = build_graph(text_input)
    distance = dijkstra(graph, (0, 0))
    # for node in graph:
    #     print(node, graph[node])
    print(distance)
    return None


if __name__ == "__main__":
    main()
