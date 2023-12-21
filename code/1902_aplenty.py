def read_input() -> tuple[list[str], list[str]]:  # noqa
    with open("../data/19_aplenty.txt", "r") as f:
        text = f.read()[:-1].split("\n\n")
    instructions = text[0].split("\n")
    parts = text[1].split("\n")
    return instructions, parts


def parse_instructions(instructions: list[str]) -> dict[str, list[tuple[str, str]]]:
    parsed = {}
    for instruction in instructions:
        instruction = instruction.replace("{", " ").replace("}", "").split()
        parsed[instruction[0]] = []
        for rule in instruction[1].split(","):
            rule = rule.split(":")
            try:
                parsed[instruction[0]].append((rule[0], rule[1]))
            except IndexError:
                parsed[instruction[0]].append((None, rule[0]))
    return parsed


def parse_parts(parts: list[str]) -> list[dict[str, int]]:
    output = []
    for part in parts:
        pieces = part[1:-1].split(",")
        parsed = {}
        for piece in pieces:
            piece = piece.split("=")
            parsed[piece[0]] = int(piece[1])
        output.append(parsed)
    return output


def init_params() -> dict[str, int]:
    return {
        "x_min": 1,
        "x_max": 4000,
        "m_min": 1,
        "m_max": 4000,
        "a_min": 1,
        "a_max": 4000,
        "s_min": 1,
        "s_max": 4000
    }


def apply_workflow(instructions: list[tuple[str, str]], params: dict[str, int], result_store: dict[str, list]):
    output = []
    for instruction in instructions:
        if instruction[0] is None:
            if instruction[1] in result_store:
                result_store[instruction[1]].append(params.copy())
            else:
                output.append((instruction[1], params.copy()))
            return output, result_store
        else:
            letter = instruction[0][0]
            symbol = instruction[0][1]
            value = int(instruction[0][2:])
        if symbol == "<":
            split_params = [params.copy(), params.copy()]
            split_params[0].update({letter + "_max": value - 1})
            split_params[1].update({letter + "_min": value})
            if instruction[1] in result_store:  # noqa
                result_store[instruction[1]].append(split_params[0])
                params = split_params[1].copy()
            else:
                output.append((instruction[1], split_params[0]))
                params = split_params[1].copy()
        elif symbol == ">":
            split_params = [params.copy(), params.copy()]
            split_params[0].update({letter + "_min": value + 1})
            split_params[1].update({letter + "_max": value})
            if instruction[1] in result_store:  # noqa
                result_store[instruction[1]].append(split_params[0])
                params = split_params[1].copy()
            else:
                output.append((instruction[1], split_params[0]))
                params = split_params[1].copy()
        else:
            raise ValueError(f"Unknown symbol: {symbol}")
    return output, result_store


def main() -> None:
    instructions, parts = read_input()
    parsed_instructions = parse_instructions(instructions)
    print(parsed_instructions)
    params = init_params()
    queue = [("in", params)]
    result_store = {"A": [], "R": []}
    while queue:
        next_wf = queue.pop(0)
        output, result_store = apply_workflow(parsed_instructions[next_wf[0]], next_wf[1], result_store)
        for o in output:
            queue.append(o)
    print("A")
    total = 0
    for r in result_store["A"]:
        total += ((r["x_max"] - r["x_min"] + 1) * (r["m_max"] - r["m_min"] + 1) *
                  (r["a_max"] - r["a_min"] + 1) * (r["s_max"] - r["s_min"] + 1))
    print(total)
    return None


if __name__ == "__main__":
    main()
