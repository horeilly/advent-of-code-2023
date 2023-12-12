from itertools import combinations

def read_input() -> list[str]:  # noqa
    with open("../data/12_springs.txt", "r") as f:
        text = f.read().split("\n")[:-1]
    return text


def parse_map(text: str) -> tuple:
    candidate, config = text.split()
    config = [int(c) for c in config.split(",")]
    return candidate, config


def check_valid_solution(solution: str, config: list[int]) -> bool:
    solution = solution.replace(".", " ")
    solution_config = [s.count("#") for s in solution.split()]
    return solution_config == config


def get_all_q_indexes(candidate: str) -> list[int]:
    return [i for i, c in enumerate(candidate) if c == "?"]


def get_all_insertion_indexes(q_indexes: list[int]) -> list[list[int]]:
    all_combos = []
    for i in range(len(q_indexes) + 1):
        for c in combinations(q_indexes, i):
            all_combos.append(list(c))
    return all_combos


def build_solution(candidate: str, insertion_indexes: list[int]) -> str:
    solution = ""
    for i in range(len(candidate)):
        if i in insertion_indexes:
            solution += "#"
        elif candidate[i] == "?":
            solution += "."
        else:
            solution += candidate[i]
    return solution


def find_solutions(candidate: str, config: list[int]) -> list[str]:
    solns = []
    q_idxs = get_all_q_indexes(candidate)
    i_idxs = get_all_insertion_indexes(q_idxs)
    for i in i_idxs:
        soln = build_solution(candidate, i)
        if check_valid_solution(soln, config):
            solns.append(soln)
    return solns


def main() -> None:
    text = read_input()
    total = 0
    for i, row in enumerate(text, 1):
        candidate, config = parse_map(row)
        solutions = find_solutions(candidate, config)
        total += len(solutions)
    print(total)
    return None


if __name__ == "__main__":
    main()
