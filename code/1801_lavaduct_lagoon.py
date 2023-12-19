def read_input() -> list[str]:
    with open("../data/18_lavaduct_lagoon.txt", "r") as f:
        text = f.read()[:-1].split("\n")
    return text


def parse_input(text: list[str]) -> list[dict[str, str]]:
    parsed = []
    for line in text:
        line = line.split()
        parsed.append({
            "direction": line[0],
            "distance": int(line[1]),
            "color": line[2][1:-1]
        })
    return parsed


def build_boundary(parsed_input: list[dict]) -> list[tuple]:
    start = (0, 0)
    boundary = [start]
    current = start
    for instruction in parsed_input:
        if instruction["direction"] == "R":
            for i in range(instruction["distance"]):
                point = (current[0], current[1] + 1)
                boundary.append(point)
                current = point
        elif instruction["direction"] == "L":
            for i in range(instruction["distance"]):
                point = (current[0], current[1] - 1)
                boundary.append(point)
                current = point
        elif instruction["direction"] == "U":
            for i in range(instruction["distance"]):
                point = (current[0] - 1, current[1])
                boundary.append(point)
                current = point
        elif instruction["direction"] == "D":
            for i in range(instruction["distance"]):
                point = (current[0] + 1, current[1])
                boundary.append(point)
                current = point
        else:
            raise ValueError(f"Unknown direction: {instruction['direction']}")
    return boundary


def get_bounds(boundary: list[tuple]) -> tuple[int, int, int, int]:
    min_x = min([point[0] for point in boundary])
    max_x = max([point[0] for point in boundary])
    min_y = min([point[1] for point in boundary])
    max_y = max([point[1] for point in boundary])
    return min_x, max_x, min_y, max_y


def display_boundary(boundary: list[tuple]) -> None:
    min_x = min([point[0] for point in boundary])  # noqa
    max_x = max([point[0] for point in boundary])
    min_y = min([point[1] for point in boundary])
    max_y = max([point[1] for point in boundary])
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if (i, j) in boundary:
                print("#", end="")
            else:
                print(".", end="")
        print()
    return None


def walk_boundary(boundary: list[tuple]) -> list[tuple]:
    visited = set(boundary)
    not_visited = {(1, 1)}
    while not_visited:
        current = not_visited.pop()
        visited.add(current)
        for neighbour in [(current[0] + 1, current[1]),
                          (current[0] - 1, current[1]),
                          (current[0], current[1] + 1),
                          (current[0], current[1] - 1)]:
            if neighbour not in visited:
                not_visited.add(neighbour)
    return list(visited)


def main() -> None:
    text_input = read_input()
    parsed_input = parse_input(text_input)
    boundary = build_boundary(parsed_input)
    boundary = walk_boundary(boundary)
    print(len(boundary))
    return None


if __name__ == "__main__":
    main()
