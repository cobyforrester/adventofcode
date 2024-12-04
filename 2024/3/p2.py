import re

def main():
    total = 0
    program = ''
    with open("input.txt", "r") as input:
        for line in input:
            program += line.strip()
    
    # I suck at regex
    pattern = r"don't\(\)(.*?)(do\(\)|\Z)"

    trimmed_program = re.sub(pattern, '', program)

    print(trimmed_program)

    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, trimmed_program)
    trim_matches = [match[4:len(match) - 1] for match in matches]
    mult_ops = [match.split(',') for match in trim_matches]
    for num1, num2 in mult_ops:
        total += int(num1) * int(num2)
            
    print(f'Part 2 answer: {total}')

if __name__ == '__main__':
    main()