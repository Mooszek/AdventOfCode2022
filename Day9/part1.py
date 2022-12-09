import os
import pprint as pp

os.chdir(os.path.dirname(__file__))

PLAYGROUND_SIZE=1000
STARTING_INDEX=500
PRINT_PLAYGROUND=False

puzzle_input = []

with open("input.txt", "r") as input_file:
    for line in input_file:
        puzzle_input.append(line.strip('\n'))

def move_right_head(horizontal_index):
    horizontal_index= horizontal_index + 1
    return horizontal_index

def move_left_head(horizontal_index):
    horizontal_index= horizontal_index - 1
    return horizontal_index

def move_up_head(vertical_index):
    vertical_index= vertical_index - 1
    return vertical_index

def move_down_head(vertical_index):
    vertical_index= vertical_index + 1
    return vertical_index

playground = []
 
for vertical_playground in range(PLAYGROUND_SIZE):
    playground.append([])
    for horizontal_playground in range(PLAYGROUND_SIZE):
        playground[vertical_playground].append(0)

vertical_index =STARTING_INDEX
horizontal_index=STARTING_INDEX
tail_vertical_index = vertical_index
tail_horizontal_index = horizontal_index

new_vertical_index = vertical_index
for line in puzzle_input:
    if line.split(' ')[0] =='R':
        for step in range(int(line.split(" ")[1])):
            new_horizontal_index = move_right_head(horizontal_index)
            if(abs(new_horizontal_index - tail_horizontal_index) >1 and tail_vertical_index == vertical_index):
                tail_horizontal_index = horizontal_index
                tail_vertical_index = vertical_index
            elif((abs(new_vertical_index - tail_vertical_index) >1 or (abs(new_horizontal_index - tail_horizontal_index) >1 ))):
                tail_horizontal_index = horizontal_index
                tail_vertical_index = vertical_index
            horizontal_index = new_horizontal_index
            playground[tail_vertical_index][tail_horizontal_index] = 1

    if line.split(' ')[0] =='L':
        for step in range(int(line.split(" ")[1])):
            new_horizontal_index = move_left_head(horizontal_index)
            if(abs(new_horizontal_index - tail_horizontal_index) >1 and tail_vertical_index == vertical_index):
                tail_horizontal_index = horizontal_index
                tail_vertical_index = vertical_index
            elif((abs(new_vertical_index - tail_vertical_index) >1 or (abs(new_horizontal_index - tail_horizontal_index) >1 ))):
                tail_horizontal_index = horizontal_index
                tail_vertical_index = vertical_index
            horizontal_index = new_horizontal_index
            playground[tail_vertical_index][tail_horizontal_index] = 1
    if line.split(' ')[0] =='U':
        for step in range(int(line.split(" ")[1])):
            new_vertical_index = move_up_head(vertical_index)
            if(abs(new_vertical_index - tail_vertical_index) >1 and tail_horizontal_index == horizontal_index):
                tail_vertical_index = vertical_index
                tail_horizontal_index = horizontal_index
            elif((abs(new_vertical_index - tail_vertical_index) >1 or (abs(new_horizontal_index - tail_horizontal_index) >1 ))):
                tail_vertical_index = vertical_index
                tail_horizontal_index = horizontal_index
            vertical_index = new_vertical_index
            playground[tail_vertical_index][tail_horizontal_index] = 1
    if line.split(' ')[0] =='D':
        for step in range(int(line.split(" ")[1])):
            new_vertical_index = move_down_head(vertical_index)
            if(abs(new_vertical_index - tail_vertical_index) >1 and tail_vertical_index == vertical_index):
                tail_vertical_index = vertical_index
                tail_horizontal_index = horizontal_index
            elif((abs(new_vertical_index - tail_vertical_index) >1 or (abs(new_horizontal_index - tail_horizontal_index) >1 ))):
                tail_vertical_index = vertical_index
                tail_horizontal_index = horizontal_index
            vertical_index = new_vertical_index
            playground[tail_vertical_index][tail_horizontal_index] = 1

if PRINT_PLAYGROUND:
    pp.pprint(playground)

total = 0
for number in playground:
    total += sum(number)

print(total)