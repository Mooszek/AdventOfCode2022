import os
os.chdir(os.path.dirname(__file__))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

priorities = {letter: (letters.index(letter) + 1) for letter in letters}

with open("input.txt", "r") as input_file:
    gifts = [set(line[:len(line)//2]).intersection(line[len(line)//2:]).pop() for line in input_file]

sum = 0

for gift in gifts:
    sum += priorities[gift]

print(sum)