def read_input() -> list[str]:
    with open("../data/06_wait_for_it.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def get_values(text: list[str]) -> list[int]:
    value_str = [row.split(":")[1] for row in text]
    values = [int(row.replace(" ", "")) for row in value_str]
    return values


def get_lower_bound(time: int, max_distance: int) -> int:
    for i in range(time + 1):
        distance = (time - i) * i
        if distance > max_distance:
            return i
    return -1


def get_upper_bound(time: int, max_distance: int) -> int:
    for i in range(time + 1, 0, -1):
        distance = (time - i) * i
        if distance > max_distance:
            return i
    return -1


def main() -> None:
    text = read_input()
    time, distance = get_values(text)
    lb = get_lower_bound(time, distance)
    ub = get_upper_bound(time, distance)
    print(ub - lb + 1)
    return None


if __name__ == "__main__":
    main()
