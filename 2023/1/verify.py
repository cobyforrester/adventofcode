numbers=[ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

inputs = []
with open('input.txt') as reader:
    # Further file processing goes here
    inputs = reader.read().split('\n')[:-1]

new_inputs = []
for input in inputs:
    new_input = None
    first_index = (None, None)    
    last_index = (None, None)    

    for number in numbers:
        last = input.rindex(number)
        first = input.index(number)
        if first_index[0] is None or first_index[0] > first:
            first = (first, number)
        if last_index[0] is None or last_index[0] < last:
            last = (last, number)
    
    if first_index[0] is not None:
        new_input = 
    