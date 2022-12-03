import os
os.chdir(os.path.dirname(__file__))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

priorities = {letter: (letters.index(letter) + 1) for letter in letters}

intersections = []

with open("input.txt", "r") as input_file:
    for line in input_file:

        first_intersect= set(line).intersection(input_file.readline().replace('\n',''))
        final_intersect= set(first_intersect).intersection(input_file.readline().replace('\n',''))
        intersections.append(final_intersect.pop())

sum = 0

for letter in intersections:
    sum += priorities[letter]

print(sum)