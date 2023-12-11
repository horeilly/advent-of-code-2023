def read_input() -> list[str]:
    with open("../data/05_seeds.txt", "r") as f:
        text = f.read()[:-1].split("\n\n")
    return text


def get_seeds(text: list[str]) -> list[int]:
    return [int(s) for s in text[0].split(": ")[1].split(" ")]


def parse_map(text: str) -> list[list[int]]:
    values = [[int(v) for v in row.split()] for row in text.split("\n")[1:]]
    return values


def use_map(state: int, values: list[list[int]]):
    for row in values:
        if row[1] <= state < row[1] + row[2]:
            return state + (row[0] - row[1])
    return state


def main() -> None:
    text = read_input()
    seeds = get_seeds(text)
    s2s_map = parse_map(text[1])
    s2f_map = parse_map(text[2])
    f2w_map = parse_map(text[3])
    w2l_map = parse_map(text[4])
    l2t_map = parse_map(text[5])
    t2h_map = parse_map(text[6])
    h2l_map = parse_map(text[7])
    locations = []

    for seed in seeds:
        state = seed
        for map_ in [s2s_map, s2f_map, f2w_map, w2l_map, l2t_map, t2h_map, h2l_map]:
            state = use_map(state, map_)
        locations.append(state)
    print(min(locations))
    return None


if __name__ == "__main__":
    main()
