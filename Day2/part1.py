import os
os.chdir(os.path.dirname(__file__))

#A - rock
#B - paper
#C - scissors
#Y - paper value 2
#X - rock value 1
#Z - scissors value 3

scores = {
    "A Y" : 8, #6 for win and 2 for paper
    "A X" : 4, # 3 for draw and 1 for rock
    "A Z" : 3,  # 0 for loss and 3 for scissors
    "B Y" : 5, # 3 for draw and 2 for paper
    "B X" : 1, # 0 for loss  and 1 for rock
    "B Z" : 9, #  6 for win and 3 for scissors
    "C Y" : 2, # 0 for loss and 2 for scissors
    "C X" : 7, # 6 for win and 1 for rock
    "C Z" : 6, # 3 for draw and 3 for scissors
}

with open("input.txt", "r") as input_file:
    total = 0
    for line in input_file:
        total += scores[line.replace('\n', '')]

print(total)

 