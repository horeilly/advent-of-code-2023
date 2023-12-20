def read_input() -> list[str]:
    with open("../data/20_pulse_propagation.txt", "r") as f:
        text = f.read()[:-1].split("\n")
    return text


class Switch:

    def __init__(self, dests: list[str]):
        self.dests = dests
        self.on = False

    def handle_pulse(self, pulse_in: str, _: str) -> str:
        if pulse_in == "low":
            if not self.on:
                pulse_out = "high"
            else:
                pulse_out = "low"
            self.on = not self.on
            return pulse_out
        else:
            return ""


class Conjunction:
    def __init__(self, inputs: list[str], dests: list[str]):
        self.dests = dests
        self.inputs = {i: "low" for i in inputs}

    def handle_pulse(self, pulse_in: str, in_node: str) -> str:
        self.inputs[in_node] = pulse_in
        if all([i == "high" for i in self.inputs.values()]):
            return "low"
        else:
            return "high"


class Broadcaster:
    def __init__(self, dests: list[str]):
        self.dests = dests

    @staticmethod
    def handle_pulse(pulse_in: str) -> str:
        return pulse_in


def build_config(text: list[str]) -> dict:
    config = {}
    for line in text:
        line = line.split("->")
        # print(line)
        key = line[0].strip()[1:] if line[0].strip()[0] in ["%", "&"] else line[0].strip()
        config[key] = {
            "dests": [i.strip() for i in line[1].split(",")],
            "type": line[0].strip()[0] if line[0].strip()[0] in ["%", "&"] else ""
        }
    for k1 in config:
        config[k1]["inputs"] = [k2 for k2 in config if k1 in config[k2]["dests"]]
    class_config = dict()
    for k in config:
        if config[k]["type"] == "%":
            class_config[k] = Switch(config[k]["dests"])
        elif config[k]["type"] == "&":
            class_config[k] = Conjunction(config[k]["inputs"], config[k]["dests"])
        else:
            class_config[k] = Broadcaster(config[k]["dests"])
    return class_config


def push(config) -> tuple[int, int]:
    queue = [{"from": "broadcaster", "to": dest, "pulse": "low"} for dest in config["broadcaster"].dests]
    n_low = 1
    n_high = 0
    while queue:
        current = queue.pop(0)
        if current["pulse"] == "low":
            n_low += 1
        else:
            n_high += 1
        # print(current["from"] + " -" + current["pulse"] + "-> " + current["to"])
        try:
            pulse = config[current["to"]].handle_pulse(current["pulse"], current["from"])
        except KeyError:
            continue
        for dest in config[current["to"]].dests:
            if pulse != "":
                queue.append({"from": current["to"], "to": dest, "pulse": pulse})

    return n_low, n_high


def main() -> None:
    text = read_input()
    config = build_config(text)
    n_low = 0
    n_high = 0
    for _ in range(1000):
        n_low_, n_high_ = push(config)
        n_low += n_low_
        n_high += n_high_
    print(n_low * n_high)
    return None


if __name__ == "__main__":
    main()
