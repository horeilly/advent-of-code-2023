def read_input() -> list[str]:  # noqa
    with open("../data/16_the_floor_is_lava.txt") as f:
        text = f.read()[:-1].split("\n")
    return text


def direction_graph() -> dict:
    return {
        "n": {
            "/": "e",
            "-": ["w", "e"],
            "\\": "w",
            "|": "n",
            ".": "n"
        },
        "e": {
            "/": "n",
            "-": "e",
            "\\": "s",
            "|": ["n", "s"],
            ".": "e"
        },
        "s": {
            "/": "w",
            "-": ["w", "e"],
            "\\": "e",
            "|": "s",
            ".": "s"
        },
        "w": {
            "/": "s",
            "-": "w",
            "\\": "n",
            "|": ["n", "s"],
            ".": "w"
        }
    }


def move_idx(curr_idx: tuple[int, int], direction: str, text: list[str]) -> tuple[int, int]:
    if direction == "n":
        if curr_idx[0] == 0:
            raise ValueError("Cannot move north")
        return curr_idx[0] - 1, curr_idx[1]
    elif direction == "e":
        if curr_idx[1] == len(text[0]) - 1:
            raise ValueError("Cannot move east")
        return curr_idx[0], curr_idx[1] + 1
    elif direction == "s":
        if curr_idx[0] == len(text) - 1:
            raise ValueError("Cannot move south")
        return curr_idx[0] + 1, curr_idx[1]
    elif direction == "w":
        if curr_idx[1] == 0:
            raise ValueError("Cannot move west")
        return curr_idx[0], curr_idx[1] - 1
    else:
        raise ValueError(f"Invalid direction: {direction}")


def move_direction(symbol: str, direction_from: str, dgraph: dict) -> str:
    return dgraph[direction_from][symbol]


def build_graph(text: list[str], dgraph: dict) -> dict:
    output = {}
    for i in range(len(text)):
        for j in range(len(text[i])):
            for k in ["n", "e", "s", "w"]:
                try:
                    out_idx = move_idx((i, j), k, text)
                    out_dir = move_direction(text[out_idx[0]][out_idx[1]], k, dgraph)
                    if isinstance(out_dir, list):
                        output[(i, j, k)] = [(*out_idx, out_dir[0]), (*out_idx, out_dir[1])]
                    else:
                        output[(i, j, k)] = [(*out_idx, out_dir,)]
                except ValueError:
                    pass
    return output


def main() -> None:
    text = read_input()
    dgraph = direction_graph()
    graph = build_graph(text, dgraph)
    visited = set()
    to_visit = {(0, 0, "s")}
    while to_visit:
        curr_idx = to_visit.pop()
        if curr_idx in visited:
            continue
        visited.add(curr_idx)
        try:
            for idx in graph[curr_idx]:
                if idx not in visited:
                    to_visit.add(idx)
        except KeyError:
            pass
    print(len(sorted(list(set([(idx[0], idx[1]) for idx in visited])), key=lambda x: (x[1], x[0]))))
    return None


if __name__ == "__main__":
    main()
