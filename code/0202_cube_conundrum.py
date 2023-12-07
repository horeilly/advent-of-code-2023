def read_input() -> list[str]:
    with open("../data/02_cube_conundrum.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def get_game_boundary_values(game: str) -> list[int]:

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

    return [max_red, max_green, max_blue]


def boundary_power_sum(game_boundary_values: list[int]) -> int:

    total = 1

    for value in game_boundary_values:
        total *= value

    return total


def main() -> None:
    total = 0
    games = read_input()
    for game in games:
        game_boundary_values = get_game_boundary_values(game)
        total += boundary_power_sum(game_boundary_values)
    print(total)
    return None


if __name__ == "__main__":
    main()
