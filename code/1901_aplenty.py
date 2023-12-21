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


def apply_workflow(instructions: list[tuple[str, str]], part: dict[str, int]) -> str:
    for instruction in instructions:
        if instruction[0] is None:
            return instruction[1]
        else:
            letter = instruction[0][0]
            symbol = instruction[0][1]
            value = int(instruction[0][2:])
        if symbol == "<":
            if part[letter] < value:
                return instruction[1]
        elif symbol == ">":
            if part[letter] > value:
                return instruction[1]
        else:
            raise ValueError(f"Unknown symbol: {symbol}")


def main() -> None:
    instructions, parts = read_input()
    parsed_instructions = parse_instructions(instructions)
    parsed_parts = parse_parts(parts)
    next_wf = "in"
    total = 0
    for part in parsed_parts:
        while next_wf not in ["A", "R"]:
            next_wf = apply_workflow(parsed_instructions[next_wf], part)
        if next_wf == "A":
            total += sum(part.values())
        next_wf = "in"
    print(total)
    return None


if __name__ == "__main__":
    main()
