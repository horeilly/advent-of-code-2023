def read_input() -> list[str]:  # noqa
    with open("../data/09_mirage.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def parse_input(text: list[str]) -> list[list[int]]:
    values = []
    for row in text:
        values.append([int(v) for v in row.split()])
    return values


def predict_row(values: list[int]) -> int:
    all_zero = False
    array = []
    prediction = values[-1]
    while not all_zero:
        for i in range(len(values) - 1):
            array.append(values[i + 1] - values[i])
        prediction += array[-1]
        if set(array) == {0}:
            all_zero = True
        else:
            values = array
            array = []
    return prediction


def main() -> None:  # noqa
    text = read_input()
    values = parse_input(text)
    total = 0
    for row in values:
        total += predict_row(row)
    print(total)
    return None


if __name__ == "__main__":
    main()
