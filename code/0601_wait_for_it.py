def read_input() -> list[str]:
    with open("../data/06_wait_for_it.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def get_values(text: list[str]) -> list[list[int]]:
    values = []
    value_str = [row.split(":")[1] for row in text]
    times, distances = [[int(v) for v in row.split()] for row in value_str]
    for time, distance in zip(times, distances):
        values.append([time, distance])
    return values


def get_race_outcomes(time: int) -> list[int]:
    outcomes = []
    for i in range(time + 1):
        distance = (time - i) * i
        outcomes.append(distance)
    return outcomes


def get_n_ways_of_winning(time: int, distance: int) -> int:
    outcomes = get_race_outcomes(time)
    return sum([1 for o in outcomes if o > distance])


def main() -> None:
    total = 1
    text = read_input()
    values = get_values(text)
    for time, distance in values:
        total *= get_n_ways_of_winning(time, distance)
    print(total)
    return None


if __name__ == "__main__":
    main()
