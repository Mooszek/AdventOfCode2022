import os

os.chdir(os.path.dirname(__file__))

with open("input.txt", "r") as input_file:
    puzzle_input = input_file.read()

message = [' ', ' ', ' ', ' ']

result = 0

for signal in puzzle_input:
    result += 1
    message.pop(0)
    message.append(signal)
    if len(set(message)) == 4 and ' ' not in set(message):
        break

print(result)