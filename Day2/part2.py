import os
os.chdir(os.path.dirname(__file__))

#A - rock
#B - paper
#C - scissors
#Y - draw
#X - lose
#Z - win
scores = {
    "A Y" : 4, #3 for draw + 1 for rock
    "A X" : 3, #0 for loss + 3 for scissors
    "A Z" : 8, #6 for win  + 2 for paper
    "B Y" : 5, #3 for draw + 2 for paper
    "B X" : 1, #0 for loss + 1 for rock
    "B Z" : 9, #6 for win + 3 for scissors
    "C Y" : 6, #3 for draw + 3 for scissors
    "C X" : 2, #0 for loss + 2 for paper
    "C Z" : 7  #6 for win + +1 for rock
}

with open("input.txt", "r") as input_file:
    total = 0
    for line in input_file:
        total += scores[line.replace('\n', '')]

print(total)