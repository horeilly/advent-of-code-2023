# BS solution; manually changing ranges and iterating

def read_input() -> list[str]:
    with open("../data/05_seeds.txt", "r") as f:
        text = f.read()[:-1].split("\n\n")
    return text


def build_seed_map(text: list[str]) -> list[list[int]]:
    output = []
    config = [int(s) for s in text[0].split(": ")[1].split(" ")]
    for i in range(0, len(config), 2):
        output.append([config[i], config[i] + config[i + 1]])
    for row in output:
        print(row)
    return output


def check_valid_seed(config: list[list[int]], seed: int) -> bool:
    for row in config:
        if row[0] <= seed < row[1]:
            return True
    return False



def parse_map(text: str) -> list[list[int]]:
    values = [[int(v) for v in row.split()] for row in text.split("\n")[1:]]
    return values


def use_map(state: int, values: list[list[int]]):
    for row in values:
        if row[0] <= state < row[0] + row[2]:
            return state + (row[1] - row[0])
    return state


def main() -> None:
    text = read_input()
    seed_map = build_seed_map(text)
    s2s_map = parse_map(text[1])
    f2s_map = parse_map(text[2])
    w2f_map = parse_map(text[3])
    l2w_map = parse_map(text[4])
    t2l_map = parse_map(text[5])
    h2t_map = parse_map(text[6])
    l2h_map = parse_map(text[7])

    i = 1
    power = 8
    bounds = [0, 10]
    # for i in range(50855030, 50855040, 1):
    while True:
        for i in range(*bounds):
            # if i % 1000 == 0:
            #     print(i)
            #     break
            state = i * (10 ** power)
            for map_ in [l2h_map, h2t_map, t2l_map, l2w_map, w2f_map, f2s_map, s2s_map]:
                state = use_map(state, map_)
            if check_valid_seed(seed_map, state):
                print("DING DING DING")
                power -= 1
                bounds = i // (10 ** power), (i + 1) // (10 ** power)
                break

        print(i, state)
            # break
        # else:
        #     pass
            # i += 1
    return None


if __name__ == "__main__":
    main()
