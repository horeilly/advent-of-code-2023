def read_input() -> list[str]:
    with open("../data/07_camel_cards.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def card_values() -> dict[str, int]:
    return {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8,
            "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}


def hand_values() -> dict[str, int]:
    return {"Five of a kind": 7, "Four of a kind": 6, "Full house": 5,
            "Three of a kind": 4, "Two pair": 3, "One pair": 2, "High card": 1}


def determine_hand(card_str: str) -> str:
    values = card_values()  # noqa
    cards = [values[c] for c in card_str]
    cards.sort()
    if cards[0] == cards[4]:
        hand = "Five of a kind"
    elif cards[0] == cards[3] or cards[1] == cards[4]:
        hand = "Four of a kind"
    elif ((cards[0] == cards[1] and cards[2] == cards[4]) or
          (cards[0] == cards[2] and cards[3] == cards[4])):
        hand = "Full house"
    elif cards[0] == cards[2] or cards[1] == cards[3] or cards[2] == cards[4]:
        hand = "Three of a kind"
    elif ((cards[0] == cards[1] and cards[2] == cards[3]) or
          (cards[0] == cards[1] and cards[3] == cards[4]) or
          (cards[1] == cards[2] and cards[3] == cards[4])):
        hand = "Two pair"
    elif cards[0] == cards[1] or cards[1] == cards[2] or cards[2] == cards[3] or cards[3] == cards[4]:
        hand = "One pair"
    else:
        hand = "High card"
    return hand


def create_config(text: list[str]) -> list[dict]:  # noqa
    config = []
    card_vals = card_values()
    hand_vals = hand_values()
    for row in text:
        cards, value = row.split()
        hand = determine_hand(cards)
        hand_val = hand_vals[hand]
        row = {
            "raw_hand": cards,
            "bid": int(value),
            "hand_value": hand_val,
            "tiebreaker": [card_vals[c] for c in cards]
        }
        config.append(row)
    return config


def main() -> None:
    text = read_input()
    config = create_config(text)
    config = sorted(config, key=lambda x: (
        x["hand_value"], x["tiebreaker"][0], x["tiebreaker"][1],
        x["tiebreaker"][2], x["tiebreaker"][3], x["tiebreaker"][4]))
    # print(config)
    total = 0
    for i, row in enumerate(config, 1):
        total += row["bid"] * i
    print(total)
    return None


if __name__ == "__main__":
    main()
