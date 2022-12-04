import os
os.chdir(os.path.dirname(__file__))

sum = 0

with open("input.txt", "r") as input_file:
    for line in input_file:
        split_ranges = (line[:-1].split(','))
        first_range = split_ranges[0].split('-')
        second_range = split_ranges[1].split('-')
        if ((int(first_range[0]) <= int(second_range[0]) and int(first_range[1]) >= int(second_range[1])) or
            (int(first_range[0]) >= int(second_range[0]) and int(first_range[1]) <=int(second_range[1]))):
                sum += 1
            
print(sum)