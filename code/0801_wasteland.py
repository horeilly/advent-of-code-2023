def read_input() -> list[str]:  # noqa
    with open("../data/08_wasteland.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def get_instructions(text: list[str]) -> list[str]:
    return list(text[0])


def build_map(text: list[str]) -> dict[str, dict]:
    values = text[2:]
    map_ = {}
    for v in values:
        source, dests = v.split(" = ")
        dests = dests[1:-1].split(", ")
        map_[source] = {"L": dests[0], "R": dests[1]}
    return map_


def main() -> None:
    text = read_input()
    instructions = get_instructions(text)
    map_ = build_map(text)
    current_loc = "AAA"
    steps = 0
    while current_loc != "ZZZ":
        current_loc = map_[current_loc][instructions.pop(0)]
        steps += 1
        if not instructions:
            instructions = get_instructions(text)
    print(steps)
    return None


if __name__ == "__main__":
    main()
