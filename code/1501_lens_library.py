def read_input() -> list[str]:
    with open("../data/15_lens_library.txt", "r") as f:
        text = f.read()[:-1].split(",")
    return text


def compute_row(row: str) -> int:
    current_value = 0
    for c in row:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def main() -> None:
    text = read_input()
    total = 0
    for row in text:
        inc = compute_row(row)
        print(inc)
        total += inc
    print(total)
    return None


if __name__ == "__main__":
    main()
