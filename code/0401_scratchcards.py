def read_input() -> list[str]:
    with open("../data/04_scratchcards.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def parse_card(card: str) -> tuple:
    card = card.split(":")[1].strip()
    card = card.split("|")
    card = [i.strip().split() for i in card]
    card = [[int(j) for j in i] for i in card]
    return set(card[0]), set(card[1])


def compute_score(winning_numbers: set, user_numbers: set) -> int:
    matches = len(winning_numbers.intersection(user_numbers))
    if matches == 0:
        return 0
    elif matches == 1:
        return 1
    else:
        return 2 ** (matches - 1)


def main() -> None:
    text = read_input()
    total_score = 0
    for card in text:
        winning_numbers, user_numbers = parse_card(card)
        total_score += compute_score(winning_numbers, user_numbers)
    print(total_score)
    return None


if __name__ == "__main__":
    main()
