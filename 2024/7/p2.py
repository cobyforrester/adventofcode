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
    print(f"Part 2 answer: {total}")


def can_be_valid(equation: list[tuple[int, list[int]]]) -> int:
    answer, nums = equation
    num_permutations = 3 ** (len(nums) - 1)
    count = 0
    while count != num_permutations:
        ops = int_to_base_3(count, len(nums) - 1)
        if perform_ops(nums, ops) == answer:
            return answer
        count += 1
    return 0


def int_to_base_3(num: int, length: int) -> str:
    result = ""
    for i in range(length - 1, -1, -1):
        # following an example helps a lot
        position_val = 3**i
        if position_val * 2 <= num:
            num = num - position_val * 2
            result += "2"
        elif position_val <= num:
            num = num - position_val
            result += "1"
        else:
            result += "0"
    return result


def perform_ops(nums: list[int], ops: str) -> int:
    total = nums[0]
    for i in range(len(ops)):
        op = ops[i]
        if op == "0":
            total = total + nums[i + 1]
        elif op == "1":
            total = total * nums[i + 1]
        else:
            # concat ||
            total = int(str(total) + str(nums[i + 1]))
    return total


if __name__ == "__main__":
    main()
