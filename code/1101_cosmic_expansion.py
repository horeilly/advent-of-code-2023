def read_input() -> list[str]:  # noqa
    with open("../data/11_cosmic_expansion.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def find_empty_rows(universe: list[str]) -> list[int]:
    empty_rows = []
    for i, row in enumerate(universe):
        if row == "." * len(row):
            empty_rows.append(i)
    return empty_rows


def find_empty_columns(universe: list[str]) -> list[int]:
    empty_columns = []
    for i in range(len(universe[0])):
        column = "".join([row[i] for row in universe])
        if column == "." * len(column):
            empty_columns.append(i)
    return empty_columns


def expand_universe(universe: list[str]) -> list[str]:
    empty_rows = find_empty_rows(universe)
    empty_columns = find_empty_columns(universe)
    new_universe = []
    for i, row in enumerate(universe):
        new_universe.append(row)
        if i in empty_rows:
            new_universe.append(row)
    for i, row in enumerate(new_universe):
        new_row = []
        for j, char in enumerate(row):
            new_row.append(char)
            if j in empty_columns:
                new_row.append(char)
        new_universe[i] = "".join(new_row)
    return new_universe


def find_galaxies(universe: list[str]) -> dict[int, tuple[int, int]]:
    galaxies = {}  # noqa
    n = 1
    for i, row in enumerate(universe):
        for j, char in enumerate(row):
            if char == "#":
                galaxies[n] = (i, j)
                n += 1
    return galaxies


def compute_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main() -> None:
    total = 0
    text = read_input()
    universe = text
    universe = expand_universe(universe)
    galaxies = find_galaxies(universe)
    for i in range(1, len(galaxies) + 1):
        for j in range(i + 1, len(galaxies) + 1):
            total += compute_distance(galaxies[i], galaxies[j])
    print(total)
    return None


if __name__ == "__main__":
    main()
