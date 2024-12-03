def main():
    safe = 0
    reports = []
    with open("input.txt", "r") as input:
        for line in input:
            reports.append([int(level) for level in line.split()])

    for report in reports:
        if _validate_report(report):
            safe += 1
    print(f'Part 1 answer: {safe}')

def _validate_report(report: list[int]) -> bool:
    # early exit if the report length is short
    if len(report) < 2:
        return True

    # note: if they are equal the loop will catch it
    is_increasing = report[0] < report[1]
    for i in range(len(report) - 1):
        current_level = report[i]
        next_level = report[i + 1]
        diff = abs(current_level - next_level)
        if diff == 0 or diff > 3:
            return False
        if is_increasing and current_level > next_level:
            return False
        if not is_increasing and current_level < next_level:
            return False
    return True
if __name__ == '__main__':
    main()