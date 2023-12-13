def read_input() -> list[str]:  # noqa
    with open("../data/12_springs.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def parse_map(text: str) -> tuple:
    candidate, config = text.split()
    config = [int(c) for c in config.split(",")]
    return candidate, config


def is_full(text: str, config: list[int]) -> bool:
    if text.count("#") == sum(config):
        return True
    else:
        return False


def is_potential(text: str, config: list[int]) -> bool:
    deterministic_text = text.split("?")[0]
    candidate = " ".join(deterministic_text.split(".")).split()
    candidate_config = [c.count("#") for c in candidate]
    if len(candidate_config) > len(config):
        return False
    else:
        for i, (cand, conf) in enumerate(zip(candidate_config, config)):
            if i == len(candidate_config) - 1:
                if conf < cand:
                    return False
            else:
                if cand != conf:
                    return False
        return True


def is_valid(text: str, config: list[int]) -> bool:
    candidate = " ".join(text.split(".")).split()
    candidate_config = [c.count("#") for c in candidate]
    if candidate_config == config:
        return True
    else:
        return False


def fill_next(text: str, config: list[int], total: int) -> int:
    q_idxs = [i for i, c in enumerate(text) if c == "?"]
    # print(q_idxs)
    if len(q_idxs) == 0:
        if is_valid(text, config):
            print(text)
            return 1
    else:
        new_text1 = "".join([c if i != q_idxs[0] else "#" for i, c in enumerate(text)])
        print(new_text1, "p1", is_potential(new_text1, config))
        if is_potential(new_text1, config):
            # print(new_text1, "p1")
            total += fill_next(new_text1, config, 0)
        new_text2 = "".join([c if i != q_idxs[0] else "." for i, c in enumerate(text)])
        print(new_text2, "p2", is_potential(new_text2, config))
        if is_potential(new_text2, config):
            # print(new_text2, "p2")
            total += fill_next(new_text2, config, 0)
        return total


def main() -> None:
    text = read_input()
    text = "?".join(["#??????#??."] * 1)
    total = 0
    # for t in text:
    #     candidate, config = parse_map(t)
    #     print(candidate, config)
        # fill_next(candidate, config, 0)
    print(total)
    print(fill_next(text, [2, 7] * 1, 0))
    # print(is_potential(".#.#####?#?#?#?", [1, 3, 1, 6] * 1))
    return None


if __name__ == "__main__":
    main()
