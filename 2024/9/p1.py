def main():
    total = 0
    format = []
    with open("input.txt", "r") as input:
        for line in input:
            format = line.strip()

    expanded_format = []
    for i, num in enumerate(format):
        if i % 2 == 0:
            expanded_format += [str(i // 2) for _ in range(int(num))]
        else:
            expanded_format += ["." for _ in range(int(num))]

    for i in range(len(expanded_format) - 1, -1, -1):
        if expanded_format[i] != ".":
            period_index = expanded_format.index(".")
            if expanded_format.index(".") < i:
                expanded_format[period_index] = expanded_format[i]
                expanded_format[i] = "."
    for i, num in enumerate(expanded_format):
        if num != ".":
            total += i * int(num)
    print(f"Part 1 answer: {total}")


if __name__ == "__main__":
    main()
