def read_input() -> list[str]:
    with open("../data/22_sand_slabs.txt", "r") as f:
        text = f.read()[:-1].split("\n")
#     text = """1,0,1~1,2,1
# 0,0,2~2,0,2
# 0,2,3~2,2,3
# 0,0,4~0,2,4
# 2,0,5~2,2,5
# 0,1,6~2,1,6
# 1,1,8~1,1,9
# """[:-1].split("\n")
    return text


def parse_text(text: list[str]) -> list[list[tuple]]:
    config = []
    for line in text:
        config.append([tuple([int(i.strip()) for i in coord.split(",")]) for coord in line.split("~")])
    return config


def get_initial_floor(config: list[list[tuple]]) -> list[list[int]]:
    x_max = max([coord[1][1] + 1 for coord in config])
    y_max = max([coord[1][0] + 1 for coord in config])
    floor = [[0 for _ in range(x_max)] for _ in range(y_max)]
    return floor


def drop_brick(initial_position: list[tuple], floor: list[list[int]]) -> (list[tuple], list[list[int]]):
    orientation = "x" if initial_position[0][0] == initial_position[1][0] else "y"
    height = initial_position[1][2] - initial_position[0][2] + 1
    if orientation == "x":
        z_int = max([floor[initial_position[0][0]][i]
                     for i in range(initial_position[0][1], initial_position[1][1] + 1)])
        for i in range(initial_position[0][1], initial_position[1][1] + 1):
            floor[initial_position[0][0]][i] = z_int + height
    else:
        z_int = max([floor[j][initial_position[0][1]]
                     for j in range(initial_position[0][0], initial_position[1][0] + 1)])
        for j in range(initial_position[0][0], initial_position[1][0] + 1):
            floor[j][initial_position[0][1]] = z_int + height
    final_position = [
        (initial_position[0][0], initial_position[0][1], z_int + 1),
        (initial_position[1][0], initial_position[1][1], z_int + height)
    ]
    return final_position, floor


def find_supports(brick: list[tuple], config: list[list[tuple]]):
    orientation = "x" if brick[0][0] == brick[1][0] else "y"
    supports = []
    if brick[0][2] == 1:
        return supports
    else:
        eligible = [b for b in config if b[1][2] == brick[0][2] - 1]
        if orientation == "x":
            brick_points = {(brick[0][0], i) for i in range(brick[0][1], brick[1][1] + 1)}
            for b in eligible:
                support_points = {(i, b[0][1]) for i in range(b[0][0], b[1][0] + 1)}
                if brick_points.intersection(support_points):
                    supports.append(b[0])
        else:
            brick_points = {(i, brick[0][1]) for i in range(brick[0][0], brick[1][0] + 1)}
            for b in eligible:
                support_points = {(b[0][0], i) for i in range(b[0][1], b[1][1] + 1)}
                if brick_points.intersection(support_points):
                    supports.append(b[0])
        return supports


def find_supporting(supports: dict[tuple, list[tuple]]) -> dict[tuple, list[tuple]]:
    supporting = {}
    for brick in supports:
        for support in supports[brick]:
            if support not in supporting:
                supporting[support] = [brick]
            else:
                supporting[support].append(brick)
    for brick in supports:
        if brick not in supporting:
            supporting[brick] = []
    return supporting


def check_stability(brick_start: tuple, support_map: dict[tuple, list[tuple]], supporting_map: dict[tuple, list[tuple]]) -> bool:
    supporting = supporting_map[brick_start]
    return all([len(support_map[s]) > 1 for s in supporting])


def main() -> None:
    text = read_input()
    config = parse_text(text)
    config = sorted(config, key=lambda x: x[0][2])
    # print(config)
    floor = get_initial_floor(config)
    new_config = []
    for brick in config:
        b, floor = drop_brick(brick, floor)
        new_config.append(b)
    support_map = {}
    for brick in new_config:
        support_map[brick[0]] = find_supports(brick, new_config)
    supporting_map = find_supporting(support_map)
    n_to_remove = 0
    for brick in supporting_map:
        can_remove = check_stability(brick, support_map, supporting_map)
        if can_remove:
            n_to_remove += 1
    print(n_to_remove)
    return None


if __name__ == "__main__":
    main()
