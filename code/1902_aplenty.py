def read_input() -> tuple[list[str], list[str]]:
    with open("../data/19_aplenty.txt", "r") as f:
        text = f.read()[:-1].split("\n\n")
    text = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""[:-1].split("\n\n")
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
                continue
            output.append((instruction[1], params.copy()))
            continue
        else:
            letter = instruction[0][0]
            symbol = instruction[0][1]
            value = int(instruction[0][2:])
        if symbol == "<":
            p = params.copy()
            p.update({letter + "_max": value - 1})
            if instruction[1] in result_store:
                result_store[instruction[1]].append(params.copy())
                continue
            output.append((instruction[1], p))
            params.update({letter + "_min": value})
        elif symbol == ">":
            p = params.copy()
            p.update({letter + "_min": value + 1})
            if instruction[1] in result_store:
                result_store[instruction[1]].append(params.copy())
                continue
            output.append((instruction[1], p))
            params.update({letter + "_max": value})
        else:
            raise ValueError(f"Unknown symbol: {symbol}")
    return output, result_store



# def apply_workflow(instructions: list[tuple[str, str]], part: dict[str, int]) -> str:
#     for instruction in instructions:
#         if instruction[0] is None:
#             return instruction[1]
#         else:
#             letter = instruction[0][0]
#             symbol = instruction[0][1]
#             value = int(instruction[0][2:])
#         if symbol == "<":
#             if part[letter] < value:
#                 return instruction[1]
#         elif symbol == ">":
#             if part[letter] > value:
#                 return instruction[1]
#         else:
#             raise ValueError(f"Unknown symbol: {symbol}")


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
    for r in result_store["A"]:
        print(r)
    print("R")
    for r in result_store["R"]:
        print(r)
    return None

# {xn: 1, xx: 4000, mn: 1, mx: 4000, an: 1, ax: 4000, sn: 1, sx: 1350}
# {xn: 1, xx: 4000, mn: 1, mx: 4000, an: 1, ax: 4000, sn: 2771, sx: 4000}
# {xn: 1, xx: 4000, mn: 1, mx: 1800, an: 1, ax: 4000, sn: 1351, sx: 2770}


if __name__ == "__main__":
    main()
