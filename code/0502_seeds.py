import cProfile

def read_input() -> list[str]:
    with open("../data/05_seeds.txt", "r") as f:
        text = f.read()[:-1].split("\n\n")
#     text = """seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4
# """[:-1].split("\n\n")
    return text


def build_seed_map(text: list[str]) -> list[list[int]]:
    output = []
    config = [int(s) for s in text[0].split(": ")[1].split(" ")]
    for i in range(0, len(config), 2):
        output.append([config[i], config[i] + config[i + 1]])
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
    while True:
        if i % 100000 == 0:
            print(i)
            break
        state = i
        for map_ in [l2h_map, h2t_map, t2l_map, l2w_map, w2f_map, f2s_map, s2s_map]:
            state = use_map(state, map_)
        if check_valid_seed(seed_map, state):
            print(i, state)
            break
        else:
            i += 1
    return None


if __name__ == "__main__":
    cProfile.run("main()")

# 39  0 15
#  0 15 35
# 37 50  2
# 54 52 46
# 35 98  2
