def read_input() -> list[str]:  # noqa
    with open("../data/14_reflector_dish.txt", "r") as f:
        text = f.read()[:-1].split("\n")
    return text


def transpose(text: list[str]) -> list[str]:
    return ["".join(row) for row in zip(*text)]


def slide(row: str) -> int:
    idx = len(row)  # noqa
    score = len(row)
    total = 0
    for c in row:
        # print(c, idx, score, total)
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


def main() -> None:
    text = read_input()
    text = transpose(text)
    total = 0
    for row in text:
        total += slide(row)
    print(total)
    return None


if __name__ == "__main__":
    main()
