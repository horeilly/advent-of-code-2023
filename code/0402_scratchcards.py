def read_input() -> list[str]:  # noqa
    with open("../data/04_scratchcards.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def parse_card(card: str) -> tuple:
    card = card.split(":")[1].strip()
    card = card.split("|")
    card = [i.strip().split() for i in card]
    card = [[int(j) for j in i] for i in card]
    return set(card[0]), set(card[1])


def compute_matches(winning_numbers: set, user_numbers: set) -> int:
    return len(winning_numbers.intersection(user_numbers))


def main() -> None:
    text = read_input()
    matches = []
    n_cards = [1] * len(text)
    for i, card in enumerate(text, 1):
        winning_numbers, user_numbers = parse_card(card)
        matches.append(compute_matches(winning_numbers, user_numbers))
    for i, n in enumerate(matches):
        for j in range(i + 1, n + i + 1):
            n_cards[j] += n_cards[i]
    print(sum(n_cards))
    return None


if __name__ == "__main__":
    main()
