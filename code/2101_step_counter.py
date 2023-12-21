def read_input() -> list[str]:
    with open("../data/21_step_counter.txt", "r") as f:
        text = f.read().split("\n")
    return text


def get_starting_point(text: list[str]) -> tuple[int, int, int]:
    for i, row in enumerate(text):
        for j, c in enumerate(row):
            if c == "S":
                return i, j, 0


def get_eligible_neighbors(text: list[str], i: int, j: int, k: int) -> list[tuple[int, int, int]]:
    eligible = []
    if i - 1 >= 0:
        if text[i - 1][j] == ".":
            eligible.append((i - 1, j, k + 1))
    if i + 1 < len(text):
        if text[i + 1][j] == ".":
            eligible.append((i + 1, j, k + 1))
    if j - 1 >= 0:
        if text[i][j - 1] == ".":
            eligible.append((i, j - 1, k + 1))
    if j + 1 < len(text[i]):
        if text[i][j + 1] == ".":
            eligible.append((i, j + 1, k + 1))
    return eligible


def main() -> None:
    text = read_input()
    i, j, k = get_starting_point(text)
    STEPS = 64  # noqa
    nodes = []
    queue = [(i, j, k)]
    visited = set()
    while queue:
        i, j, k = queue.pop(0)
        if (i, j) not in visited and k <= STEPS:
            visited.add((i, j))
            nodes.append((i, j, k))
            neighbors = get_eligible_neighbors(text, i, j, k)
            for neighbor in neighbors:
                if (neighbor[0], neighbor[1]) not in visited:
                    queue.append(neighbor)
    print(len(set([(n[0], n[1]) for n in nodes if n[2] % 2 == 0])))

    return None


if __name__ == "__main__":
    main()
