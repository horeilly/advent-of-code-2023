def read_input() -> list[str]:
    with open("../data/01_trebuchet.txt", "r") as f:
        text = f.read().split("\n")
    return text


def compute_calibration_value(text: str) -> int:
    value = 0
    for char in text:
        if char.isdigit():
            value += int(char) * 10
            break
    for char in text[::-1]:
        if char.isdigit():
            value += int(char)
            break
    return value


def main() -> None:
    total = 0
    text_input = read_input()
    for row in text_input:
        row_value = compute_calibration_value(row)
        total += row_value
    print(total)
    return None


if __name__ == "__main__":
    main()
