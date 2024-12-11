def main():
    total = 0
    format = []
    with open("input.txt", "r") as input:
        for line in input:
            format = line.strip()

    expanded_format = []
    for i, num in enumerate(format):
        if i % 2 == 0:
            expanded_format += [[str(i // 2) for _ in range(int(num))]]
        else:
            expanded_format += ["." for _ in range(int(num))]

    for i in range(len(expanded_format) - 1, -1, -1):
        nums = expanded_format[i]
        if nums != ".":
            sliced = expanded_format[:i]
            span_index = does_have_span_length(sliced, len(nums))
            if span_index != -1:
                expanded_format = (
                    expanded_format[0:span_index]
                    + expanded_format[span_index + len(nums) :]
                )
                old_elem_index = expanded_format.index(nums)
                expanded_format = (
                    expanded_format[:old_elem_index]
                    + ["." for _ in range(len(nums))]
                    + expanded_format[old_elem_index + 1 :]
                )
                expanded_format.insert(span_index, nums)
    count = 0
    for i, nums in enumerate(expanded_format):
        if nums != ".":
            for num in nums:
                total += count * int(num)
                count += 1
        else:
            count += 1
    print(f"Part 2 answer: {total}")


def does_have_span_length(arr: list[str], length: int) -> int:
    current_tally = 0
    for i, num in enumerate(arr):
        if num == ".":
            current_tally += 1
            if current_tally == length:
                return i - current_tally + 1
        else:
            current_tally = 0
    return -1


if __name__ == "__main__":
    main()
