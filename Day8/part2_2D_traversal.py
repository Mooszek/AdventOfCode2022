import os

os.chdir(os.path.dirname(__file__))

puzzle_input = []
with open("input.txt", "r") as input_file:
    for line in input_file:
        puzzle_input.append(list(line.strip('\n')))

min_index = 0
width =len(puzzle_input)
height = len(puzzle_input[0])

vertical_index =0
horizontal_index=0

take_number =  puzzle_input[vertical_index][horizontal_index]

max_score = 0
results = []
while horizontal_index < width:
    vertical_index = 0
    while vertical_index < height:
        to_the_right = horizontal_index + 1
        to_the_left = horizontal_index - 1
        above = vertical_index -1
        down = vertical_index + 1
        to_the_right_score = 0 
        to_the_left_score = 0 
        above_score = 0 
        down_score = 0 

        while to_the_right < width and puzzle_input[vertical_index][to_the_right] < puzzle_input[vertical_index][horizontal_index]:
            to_the_right_score +=1
            to_the_right +=1

        if to_the_right < width:
            to_the_right_score +=1

        while to_the_left >= 0 and puzzle_input[vertical_index][to_the_left] < puzzle_input[vertical_index][horizontal_index]:
            to_the_left_score +=1
            to_the_left -=1

        if to_the_left >= 0:
            to_the_left_score +=1

        while down < height and puzzle_input[down][horizontal_index] < puzzle_input[vertical_index][horizontal_index]:
            down_score +=1
            down +=1

        if down < height:
            down_score +=1

        while above >= 0 and puzzle_input[above][horizontal_index] < puzzle_input[vertical_index][horizontal_index]:
            above_score +=1
            above -=1

        if above >= 0:
            above_score +=1

        results.append(to_the_right_score *  to_the_left_score *  above_score * down_score)
        vertical_index +=1
    horizontal_index+=1

print(max(results))