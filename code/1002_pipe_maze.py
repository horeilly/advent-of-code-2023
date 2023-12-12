def read_input() -> list[str]:  # noqa
    with open("../data/10_pipe_maze.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def move_map() -> dict[str, list[str]]:
    return {
        "n": ["|", "7", "F"],
        "s": ["|", "J", "L"],
        "w": ["-", "F", "L"],
        "e": ["-", "J", "7"],
    }


def dir_change_map() -> dict[str, dict[str, str]]:
    return {
        "|": {
            "n": "n",
            "s": "s"
        },
        "-": {
            "e": "e",
            "w": "w"
        },
        "7": {
            "n": "w",
            "e": "s"
        },
        "J": {
            "s": "w",
            "e": "n"
        },
        "F": {
            "n": "e",
            "w": "s"
        },
        "L": {
            "s": "e",
            "w": "n"
        }
    }


def move(current_idx: tuple[int, int], direction: str) -> tuple[int, int]:
    row_idx, col_idx = current_idx
    if direction == "n":
        return row_idx - 1, col_idx
    elif direction == "s":
        return row_idx + 1, col_idx
    elif direction == "e":
        return row_idx, col_idx + 1
    elif direction == "w":
        return row_idx, col_idx - 1
    else:
        raise ValueError(f"Invalid direction: {direction}")


def get_starting_index(text: list[str]) -> tuple[int, int]:
    for row_index, row in enumerate(text):
        for column_index, char in enumerate(row):
            if char == "S":
                return row_index, column_index


def find_valid_next_moves_from_start(
        text: list[str], starting_index: tuple[int, int]) -> list[str]:
    valid_moves = []
    mmap = move_map()
    row_idx, col_idx = starting_index
    if text[row_idx][col_idx - 1] in mmap["w"] and col_idx - 1 >= 0:
        valid_moves.append("w")
    if text[row_idx][col_idx + 1] in mmap["e"] and col_idx + 1 < len(text[0]):
        valid_moves.append("e")
    if text[row_idx - 1][col_idx] in mmap["n"] and row_idx - 1 >= 0:
        valid_moves.append("n")
    if text[row_idx + 1][col_idx] in mmap["s"] and row_idx + 1 < len(text):
        valid_moves.append("s")
    return valid_moves


def determine_start_char(next_moves: list[str]) -> str:
    if set(next_moves) == {"n", "e"}:
        return "L"
    elif set(next_moves) == {"n", "w"}:
        return "J"
    elif set(next_moves) == {"s", "e"}:
        return "F"
    elif set(next_moves) == {"s", "w"}:
        return "7"
    else:
        raise ValueError(f"Invalid next moves: {next_moves}")


def build_loop(text: list[str], starting_index: tuple[int, int]) -> list[tuple[int, int]]:
    loop = []
    dmap = dir_change_map()
    row_idx, col_idx = starting_index
    current_dir = find_valid_next_moves_from_start(text, starting_index)[0]
    loop.append((row_idx, col_idx))
    finished = False
    while not finished:
        row_idx, col_idx = move((row_idx, col_idx), current_dir)
        current_char = text[row_idx][col_idx]
        if current_char == "S":
            finished = True
        elif current_char in dmap:
            current_dir = dmap[current_char][current_dir]
            loop.append((row_idx, col_idx))
        else:
            raise ValueError(f"Invalid character: {current_char}")
    return loop


def build_loop_text(text: list[str], starting_index: tuple[int, int]) -> list[str]:
    loop = build_loop(text, starting_index)
    start_moves = find_valid_next_moves_from_start(text, starting_index)
    loop_text = []
    for row_index, row in enumerate(text):
        loop_text_row = ""
        for col_index, char in enumerate(row):
            if char == "S":
                loop_text_row += determine_start_char(start_moves)
                continue
            if (row_index, col_index) in loop:
                loop_text_row += char
            else:
                loop_text_row += "."
        loop_text.append(loop_text_row)
    return loop_text


def get_candidates(text: list[str]) -> list[tuple[int, int]]:
    candidates = []
    for row_index, row in enumerate(text):
        for col_index, char in enumerate(row):
            if char == ".":
                candidates.append((row_index, col_index))
    return candidates


def check_if_within_loop(text: list[str], point: tuple[int, int]) -> bool:
    row_idx, col_idx = point
    row = text[row_idx]
    crosses = 0
    j = col_idx
    finished = False
    while not finished:
        if row[j] == "|":
            crosses += 1
        elif row[j] == "F":
            fully_crossed = False
            crosses += 1
            while not fully_crossed:
                j += 1
                if row[j] == "J":
                    fully_crossed = True
                elif row[j] == "7":
                    fully_crossed = True
                    crosses += 1
        elif row[j] == "L":
            fully_crossed = False
            crosses += 1
            while not fully_crossed:
                j += 1
                if row[j] == "J":
                    fully_crossed = True
                    crosses += 1
                elif row[j] == "7":
                    fully_crossed = True
        j += 1
        if j == len(row):
            finished = True
    return crosses % 2 == 1


def main() -> None:
    text = read_input()
    lt = build_loop_text(text, get_starting_index(text))
    candidates = get_candidates(lt)
    total = 0
    for candidate in candidates:
        if check_if_within_loop(lt, candidate):
            total += 1
    print(total)
    return None


if __name__ == "__main__":
    main()
