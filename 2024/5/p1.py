def main():
    total = 0
    rules: dict[int, set[int]] = {}
    updates = []
    with open("input.txt", "r") as input:
        section = 1
        for l in input:
            line = l.strip()
            if line == "":
                section = 2
            elif section == 1:
                num1, num2 = line.split("|")
                num1, num2 = int(num1), int(num2)
                if num1 in rules:
                    # references and jazz
                    rules[num1].add(num2)
                else:
                    rules[num1] = set([num2])
            else:
                nums = [int(num) for num in line.split(",")]
                updates.append(nums)
    for update in updates:
        if not len(update):
            total += update[0]
        elif _is_update_valid(update, rules):
            total += update[len(update) // 2]
    print(f"Part 1 answer: {total}")


def _is_update_valid(update: list[int], rules: dict[str, list[str]]) -> bool:
    seen = set()
    for num in update:
        if num in rules and seen.intersection(rules[num]):
            return False
        seen.add(num)
    return True


if __name__ == "__main__":
    main()
