def read_input() -> list[str]:  # noqa
    with open("../data/13_point_of_incidence.txt", "r") as f:
        text = f.read()[:-1].split("\n\n")
    return text


def parse_pattern(pattern: str) -> list[str]:
    return pattern.split("\n")


def transpose_pattern(pattern: list[str]) -> list[str]:
    return ["".join(row) for row in zip(*pattern)]


def find_reflection(pattern: list[str]) -> int:
    for i in range(len(pattern) - 1):
        n = i + 1
        p1 = pattern[:n]
        p2 = pattern[n:(2 * n)][::-1]
        p1 = p1[len(p1) - len(p2):]
        edit_distance = compute_edit_distance(p1, p2)
        if edit_distance == 1:
            return n
    return -1


def compute_edit_distance(part1: list[str], part2: list[str]) -> int:
    p1 = "".join(part1)
    p2 = "".join(part2)
    return sum([1 if p1[i] != p2[i] else 0 for i in range(len(p1))])


def main() -> None:  # noqa
    text = read_input()
    total = 0
    for pattern in text:
        pattern = parse_pattern(pattern)
        r = find_reflection(pattern)
        if r != -1:
            total += r * 100
        else:
            c = find_reflection(transpose_pattern(pattern))
            total += c
    print(total)
    return None


if __name__ == "__main__":
    main()
