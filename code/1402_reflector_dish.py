def read_input() -> list[str]:  # noqa
    with open("../data/14_reflector_dish.txt", "r") as f:
        text = f.read()[:-1].split("\n")
    return text


def transpose(text: list[str]) -> list[str]:
    return ["".join(row) for row in zip(*text)]


def slide(row: str) -> str:
    parts = row.split("#")
    parts_out = []
    for part in parts:
        rocks = part.count("O")
        part = rocks * "O" + (len(part) - rocks) * "."
        parts_out.append(part)
    return "#".join(parts_out)


def tilt_north(text: list[str]) -> list[str]:
    text = transpose(text)
    text = [slide(row) for row in text]
    text = transpose(text)
    return text


def tilt_west(text: list[str]) -> list[str]:
    text = [slide(row) for row in text]
    return text


def tilt_south(text: list[str]) -> list[str]:
    text = transpose(text)
    text = [slide(row[::-1])[::-1] for row in text]
    text = transpose(text)
    return text


def tilt_east(text: list[str]) -> list[str]:
    text = [slide(row[::-1])[::-1] for row in text]
    return text


def cycle(text: list[str]) -> list[str]:
    text = tilt_north(text)
    text = tilt_west(text)
    text = tilt_south(text)
    text = tilt_east(text)
    return text


def compute_load(row: str) -> int:
    idx = len(row)  # noqa
    score = len(row)
    total = 0
    for c in row:
        if c == "#":
            idx -= 1
            score = idx
        elif c == ".":
            idx -= 1
        elif c == "O":
            total += score
            idx -= 1
            score -= 1
    return total


def guess_seq_len(seq):
    guess = 1
    max_len = len(seq) // 2
    for x in range(2, max_len):
        if seq[0:x] == seq[x:(2 * x)]:
            return x
    return guess


def main() -> None:
    RANDOM_START = 2000  # noqa
    SEQ_LEN = 3000  # noqa
    text = read_input()
    total = 0
    for i, row in enumerate(text):
        total += row.count("O") * (len(text) - i)
    outputs = []
    for _ in range(1, SEQ_LEN):
        text = cycle(text)
        total = 0
        for i, row in enumerate(text):
            total += row.count("O") * (len(text) - i)
        outputs.append(total)
    cycle_len = guess_seq_len(outputs[RANDOM_START:])
    outputs = outputs[RANDOM_START:][:cycle_len]
    n_cycles = (1000000000 - RANDOM_START) // cycle_len
    relevant_idx = 1000000000 - (RANDOM_START + cycle_len * n_cycles)
    print(outputs[relevant_idx - 1])
    return None


if __name__ == "__main__":
    main()
