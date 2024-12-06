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
        corrected_update = _correct_update(update, rules)
        if corrected_update:
            total += corrected_update[len(corrected_update) // 2]
    print(f"Part 2 answer: {total}")


def _correct_update(update: list[int], rules: dict[str, list[str]]) -> list[int]:
    was_fixed = False
    is_fixed = False
    while not is_fixed:
        seen = []
        is_fixed = True
        for i in range(len(update)):
            num = update[i]
            if num in rules and set(seen).intersection(rules[num]):
                # i code for a living???
                is_fixed = False
                was_fixed = True
                bad_num = set(seen).intersection(rules[num]).pop()
                tmp = update[:i]
                tmp.reverse()
                new_num_index = len(tmp) - tmp.index(bad_num) - 1
                update = update[:i] + update[i + 1 :]
                update.insert(new_num_index, num)
                break
            seen.append(num)
    if was_fixed:
        return update
    return []


if __name__ == "__main__":
    main()
