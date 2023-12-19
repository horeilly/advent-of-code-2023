def read_input() -> list[str]:
    with open("../data/18_lavaduct_lagoon.txt", "r") as f:
        text = f.read()[:-1].split("\n")
    return text


def parse_input(text: list[str]) -> list[dict[str, str]]:
    parsed = []
    for line in text:
        data = line[-7:-1]
        direction = {"0": "R", "1": "D", "2": "L", "3": "U"}[data[-1]]
        distance = int("0x" + data[:-1], 16)
        parsed.append({
            "direction": direction,
            "distance": distance
        })
    return parsed


def build_boundary(parsed_input: list[dict]) -> list[tuple]:
    start = (0, 0)
    boundary = [start]
    current = start
    for instruction in parsed_input:
        if instruction["direction"] == "R":
            # for i in range(instruction["distance"]):
            point = (current[0], current[1] + instruction["distance"])
            boundary.append(point)
            current = point
        elif instruction["direction"] == "L":
            # for i in range(instruction["distance"]):
            point = (current[0], current[1] - instruction["distance"])
            boundary.append(point)
            current = point
        elif instruction["direction"] == "U":
            # for i in range(instruction["distance"]):
            point = (current[0] - instruction["distance"], current[1])
            boundary.append(point)
            current = point
        elif instruction["direction"] == "D":
            # for i in range(instruction["distance"]):
            point = (current[0] + instruction["distance"], current[1])
            boundary.append(point)
            current = point
        else:
            raise ValueError(f"Unknown direction: {instruction['direction']}")
    return boundary


def determine_direction(current: tuple, next_: tuple) -> str:
    if current[0] == next_[0]:
        if current[1] < next_[1]:
            return "R"
        else:
            return "L"
    else:
        if current[0] < next_[0]:
            return "D"
        else:
            return "U"


def determine_turn(current: tuple, next_: tuple, next_next: tuple) -> str:
    if current[0] == next_[0]:
        if current[1] < next_[1]:
            if next_next[0] < next_[0]:
                return "L"
            else:
                return "R"
        else:
            if next_next[0] < next_[0]:
                return "R"
            else:
                return "L"
    else:
        if current[0] < next_[0]:
            if next_next[1] < next_[1]:
                return "R"
            else:
                return "L"
        else:
            if next_next[1] < next_[1]:
                return "L"
            else:
                return "R"


def determine_edge_type(direction: str, turn: str) -> str:
    if direction == "R":
        if turn == "L":
            return "L"
        else:
            return "R"
    elif direction == "L":
        if turn == "L":
            return "R"
        else:
            return "L"
    elif direction == "U":
        if turn == "L":
            return "B"
        else:
            return "T"
    elif direction == "D":
        if turn == "L":
            return "T"
        else:
            return "B"
    else:
        raise ValueError(f"Unknown direction: {direction}")


def enrich_boundary(boundary: list[tuple]) -> list[tuple]:
    output = []
    n_vertices = len(boundary)
    y_adjustment = 0
    x_adjustment = 0
    for i in range(len(boundary) - 1):
        from_direction = determine_direction(
            boundary[i - 1 % n_vertices], boundary[i % n_vertices])
        turn = determine_turn(
            boundary[i - 1 % n_vertices], boundary[i % n_vertices], boundary[(i + 1) % n_vertices])
        edge_type = determine_edge_type(from_direction, turn)
        if boundary[i % n_vertices] == (0, 0):
            edge_type = None
        if edge_type == "R":
            x_adjustment = 1 if x_adjustment == 0 else x_adjustment
        elif edge_type == "L":
            x_adjustment = 0
        elif edge_type == "T":
            y_adjustment = 0
        elif edge_type == "B":
            y_adjustment = 1 if y_adjustment == 0 else y_adjustment
        vertex = (boundary[i % n_vertices][0] + y_adjustment,
                  boundary[i % n_vertices][1] + x_adjustment)

        output.append(vertex)
    return output


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


def compute_polygon_area(vertices: list[tuple[int, int]]) -> float:
    area = 0.0
    n = len(vertices)

    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]

    area = int(abs(area) // 2)
    return area


def main() -> None:
    text_input = read_input()
    parsed_input = parse_input(text_input)
    boundary = build_boundary(parsed_input)
    boundary = enrich_boundary(boundary)
    area = compute_polygon_area(boundary)
    print(area)
    return None


if __name__ == "__main__":
    main()
