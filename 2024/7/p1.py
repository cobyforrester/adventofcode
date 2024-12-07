def main():
    total = 0
    equations: list[tuple[int, list[int]]] = []
    with open("input.txt", "r") as input:
        for line in input:
            answer, nums = line.strip().split(":")
            answer = int(answer)
            nums = nums.strip().split(" ")
            nums = [int(num) for num in nums]
            equations.append((answer, nums))
    for eq in equations:
        total += can_be_valid(eq)
    print(f"Part 1 answer: {total}")


def can_be_valid(equation: list[tuple[int, list[int]]]) -> int:
    answer, nums = equation
    num_permutations = 2 ** (len(nums) - 1)
    count = 0b0
    while count != num_permutations:
        count_bin = bin(count).lstrip("0b")
        padding = "0" * (len(nums) - len(count_bin) - 1)
        ops = padding + count_bin
        if perform_ops(nums, ops) == answer:
            return answer
        count += 1
    return 0


def perform_ops(nums: list[int], ops: str) -> int:
    total = nums[0]
    for i in range(len(ops)):
        if ops[i] == "0":
            total = total + nums[i + 1]
        else:
            total = total * nums[i + 1]
    return total


if __name__ == "__main__":
    main()
