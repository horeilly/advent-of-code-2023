import math


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


def get_sources(map_: dict[str, dict]) -> list[str]:
    return [k for k in map_ if k[-1] == "A"]


def get_dests(map_: dict[str, dict]) -> list[str]:
    return [k for k in map_ if k[-1] == "Z"]


def compute_loop_length(map_: dict[str, dict], source: str, instructions: list) -> int:
    instructions_store = instructions.copy()
    steps = 0
    while not source.endswith("Z"):
        instruction = instructions.pop(0)
        source = map_[source][instruction]
        if not instructions:
            instructions = instructions_store.copy()
        steps += 1
    return steps


def main() -> None:
    text = read_input()
    map_ = build_map(text)
    sources = get_sources(map_)
    loops = []
    for source in sources:
        instructions = get_instructions(text)
        loop_length = compute_loop_length(map_, source, instructions)
        loops.append(loop_length)
    print(math.lcm(*loops))
    return None


if __name__ == "__main__":
    main()
