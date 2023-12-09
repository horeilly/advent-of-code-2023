import re


def read_input() -> list[str]:
    with open("../data/03_gear_ratios.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def extract_all_gear_indexes(text: list[str]) -> list[list]:
    r = re.compile(r"\*{1}")
    output = []
    for row_index, row in enumerate(text):
        output.extend([[row_index, m.start()] for m in r.finditer(row)])
    return output


def get_side_ratio(index: list[int], text: list[str]) -> tuple:
    adjacent_number_count = 0
    ratio = 1
    l = re.search(r"[0-9]+\*$", text[index[0]][:(index[1] + 1)])
    if l is not None:
        adjacent_number_count += 1
        ratio *= int(l.group()[:-1])
    r = re.search(r"^\*[0-9]+", text[index[0]][index[1]:])
    if r is not None:
        adjacent_number_count += 1
        ratio *= int(r.group()[1:])
    return adjacent_number_count, ratio


def get_ul_ratio(index: list[int], text: list[str], adjustment: int) -> tuple:
    adjacent_number_count = 0
    ratio = 1
    ul = re.search(r"[0-9]+\.$", text[index[0] - adjustment][:(index[1] + 1)])
    if ul is not None:
        adjacent_number_count += 1
        ratio *= int(ul.group()[:-1])
    ur = re.search(r"^\.[0-9]+", text[index[0] - adjustment][index[1]:])
    if ur is not None:
        adjacent_number_count += 1
        ratio *= int(ur.group()[1:])
    if text[index[0] - adjustment][index[1]].isdigit():
        uml = re.search(r"[0-9]+$", text[index[0] - adjustment][:(index[1] + 1)])
        if uml is not None:
            uml = uml.group()
        umr = re.search(r"^[0-9]+", text[index[0] - adjustment][index[1]:])
        if umr is not None:
            umr = umr.group()
        um = uml[:-1] + umr
        adjacent_number_count += 1
        ratio *= int(um)
    return adjacent_number_count, ratio


def get_upper_ratio(index: list[int], text: list[str]) -> tuple:
    return get_ul_ratio(index, text, 1)


def get_lower_ratio(index: list[int], text: list[str]) -> tuple:
    return get_ul_ratio(index, text, -1)


def main() -> None:
    total = 0
    text = read_input()
    gear_indexes = extract_all_gear_indexes(text)
    for index in gear_indexes:
        if index[0] == 0:
            uanc, ur = 0, 1
            sanc, sr = get_side_ratio(index, text)
            lanc, lr = get_lower_ratio(index, text)
        elif index[0] == len(text) - 1:
            uanc, ur = get_upper_ratio(index, text)
            sanc, sr = get_side_ratio(index, text)
            lanc, lr = 0, 1
        else:
            uanc, ur = get_upper_ratio(index, text)
            sanc, sr = get_side_ratio(index, text)
            lanc, lr = get_lower_ratio(index, text)
        anc = uanc + sanc + lanc
        r = ur * sr * lr
        if anc == 2:
            total += r
    print(total)
    return None


if __name__ == "__main__":
    main()
