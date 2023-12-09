import re


def read_input() -> list[str]:
    with open("../data/03_gear_ratios.txt", "r") as f:
        text = f.read().split("\n")[:-1]
#     text = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """.split("\n")[:-1]
    return text


def extract_all_candidates(text: list[str]) -> list[list[dict]]:
    r = re.compile(r"[0-9]+")
    output = []
    for row in text:
        output.append([{"number": m.group(), "hbounds": list(m.span())}
                       for m in r.finditer(row)])
    return output


def get_indexes_to_check(
        hbounds: list[int], row: str, row_index: int,
        n_rows: int) -> list[tuple]:
    hbounds[0] -= 1
    vbounds = [row_index - 1, row_index + 1]
    top_indexes = [(vbounds[0], i) for i in range(hbounds[0], hbounds[1] + 1)]
    bottom_indexes = [(vbounds[1], i) for i in range(hbounds[0], hbounds[1] + 1)]
    middle_indexes = [(row_index, hbounds[0]), (row_index, hbounds[1])]
    all_indexes = top_indexes + bottom_indexes + middle_indexes
    filtered_indexes = []
    for index in all_indexes:
        if (0 <= index[0] < n_rows) and (0 <= index[1] < len(row)):
            filtered_indexes.append(index)
    return filtered_indexes


def main() -> None:
    total = 0
    text = read_input()
    candidates = extract_all_candidates(text)
    n_rows = len(candidates)
    for row_index, row in enumerate(candidates):
        for candidate in row:
            indexes_to_check = get_indexes_to_check(
                candidate["hbounds"], text[row_index], row_index, n_rows)
            for index in indexes_to_check:
                if text[index[0]][index[1]] != ".":
                    total += int(candidate["number"])
                    break
    print(total)
    return None


if __name__ == "__main__":
    main()
