import re

def main():
    total = 0
    with open("input.txt", "r") as input:
        for line in input:
            pattern = r"mul\(\d{1,3},\d{1,3}\)"
            matches = re.findall(pattern, line)
            trim_matches = [match[4:len(match) - 1] for match in matches]
            mult_ops = [match.split(',') for match in trim_matches]
            for num1, num2 in mult_ops:
                total += int(num1) * int(num2)
            
    print(f'Part 1 answer: {total}')

if __name__ == '__main__':
    main()