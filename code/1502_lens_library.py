def read_input() -> list[str]:
    with open("../data/15_lens_library.txt", "r") as f:
        text = f.read()[:-1].split(",")
    return text


def compute_hash(row: str) -> int:
    row = row.replace("-", " ").replace("=", " ").split()[0]
    current_value = 0
    for c in row:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def parse_row(row: str) -> tuple:
    if "-" in row:
        label = row.split("-")[0]
        op = "-"
        value = -1
    elif "=" in row:
        label = row.split("=")[0]
        op = "="
        value = int(row.split("=")[1])
    else:
        raise ValueError("Invalid row")
    return label, op, value


def do_operation(label: str, op: str, value: int, boxes: list[list]) -> None:
    lens = {"label": label, "focal_length": value}
    box_idx = compute_hash(label)
    if op == "-":
        boxes[box_idx] = [l for l in boxes[box_idx] if l["label"] != label]  # noqa
        return None
    elif op == "=":
        box = boxes[box_idx]
        label_exists = False
        for l in box:  # noqa
            if l["label"] == label:
                l["focal_length"] = value
                label_exists = True
                break
        if not label_exists:
            box.append(lens)
        return None
    else:
        raise ValueError("Invalid operation")


def compute_focusing_power(boxes: list[list]) -> int:
    total = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            total += (i + 1) * (j + 1) * boxes[i][j]["focal_length"]
    return total


def main() -> None:
    text = read_input()
    output = [[] for _ in range(256)]
    for row in text:
        label, op, value = parse_row(row)
        do_operation(label, op, value, output)
    total = compute_focusing_power(output)
    print(total)
    return None


if __name__ == "__main__":
    main()
