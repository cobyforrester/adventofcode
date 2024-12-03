"""
    Right answer but I think O(n*m^m) where n is number of reports and m is report length.
    There is surely a more time efficient solution.
"""

def main():
    safe = 0
    reports = []
    with open("input.txt", "r") as input:
        for line in input:
            reports.append([int(level) for level in line.split()])

    for report in reports:
        for i in range(len(report)):
            report_slice = report[0:i] + report[i+1:len(report)]
            if _validate_report(report_slice):
                safe += 1
                break
    print(f'Part 2 answer: {safe}')

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