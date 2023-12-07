def read_input() -> list[str]:
    with open("../data/02_cube_conundrum.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def extract_game_id(game: str) -> int:
    return int(game.split(":")[0].split(" ")[1])


def get_game_boundaries(game: str) -> dict[str, int]:

    draws = game.split(":")[1].strip().replace(",", ";").split("; ") # noqa

    max_red = 0
    max_green = 0
    max_blue = 0

    for draw in draws:
        parts = draw.split(" ")
        value, color = int(parts[0]), parts[1]
        if color == "red":
            max_red = max(max_red, value)
        elif color == "green":
            max_green = max(max_green, value)
        elif color == "blue":
            max_blue = max(max_blue, value)
        else:
            raise ValueError("Something went wrong...")

    return {"red": max_red, "green": max_green, "blue": max_blue}


def check_if_valid_game(game_boundaries: dict, game_constraints: dict) -> bool:

    for color in game_boundaries:
        if game_constraints[color] < game_boundaries[color]:
            return False

    return True


def main() -> None:
    loaded_config = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    total = 0
    games = read_input()
    for game in games:
        game_id = extract_game_id(game)
        game_boundaries = get_game_boundaries(game)
        if check_if_valid_game(game_boundaries, loaded_config):
            total += game_id
    print(total)
    return None


if __name__ == "__main__":
    main()
