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


def main() -> None:
    text = read_input()
    dmap = dir_change_map()
    current_symbol = ""
    current_idx = get_starting_index(text)
    next_moves = find_valid_next_moves_from_start(text, current_idx)
    direction = next_moves[0]
    steps = 0
    while current_symbol != "S":
        current_idx = move(current_idx, direction)
        current_symbol = text[current_idx[0]][current_idx[1]]
        try:
            direction = dmap[current_symbol][direction]
        except KeyError:
            pass
        steps += 1
    print(steps // 2)
    return None


if __name__ == "__main__":
    main()
