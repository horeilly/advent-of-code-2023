def read_input() -> list[str]:
    with open("../data/01_trebuchet.txt", "r") as f:
        text = f.read().split("\n")
    return text


def bag_of_words() -> dict[str, int]:
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "zero": 0, "one": 1, "two": 2, "three": 3,
            "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def compute_calibration_value(text: str) -> int:

    bow = bag_of_words()

    value = 0
    current_first, current_first_value = float("inf"), float("nan")
    current_last, current_last_value = float("inf"), float("nan")

    for substr in bow:
        starting_idx = text.find(substr)
        if starting_idx != -1:
            if starting_idx < current_first:
                current_first = starting_idx
                current_first_value = bow[substr]
    value += current_first_value * 10

    for substr in bow:
        starting_idx = text[::-1].find(substr[::-1])
        if starting_idx != -1:
            if starting_idx < current_last:
                current_last = starting_idx
                current_last_value = bow[substr]
    value += current_last_value

    return value


def main() -> None:
    total = 0
    text_input = read_input()[:-1]
    for row in text_input:
        row_value = compute_calibration_value(row)
        total += row_value
    print(total)
    return None


if __name__ == "__main__":
    main()
