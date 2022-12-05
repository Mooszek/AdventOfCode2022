import os
import numpy as np

os.chdir(os.path.dirname(__file__))

def crate_mover(warehouse, executions, source, destination):
    for _ in range(executions):
        box  = warehouse[source].pop()
        warehouse[destination].append(box)

with open("input.txt", "r") as input_file:
    
    original_stacks=[]
    temp_stacks = []
    shelves= {}

    for row in range(0,8):
        original_stacks.append(input_file.readline().replace('\n', ''))
        temp_stacks.append([])
        for _ in range(1, 36, 4):
            temp_stacks[row].append((original_stacks[row][_]))

    transposed_stacks = np.rot90(temp_stacks,3).tolist()

    for row in transposed_stacks:
        while ' ' in row:
            row.remove(' ')

    for row_of_boxes in range(0,9):
        key_index = str(row_of_boxes+1)
        shelves[key_index] = transposed_stacks[row_of_boxes]

    input_file.readline()
    input_file.readline()

    for instruction in input_file:
        executions ,source, destination = instruction.split(' ')[1], instruction.split(' ')[3], instruction.split(' ')[5].replace('\n', '')
        crate_mover(shelves, int(executions), source, destination)

    top_stacks = []
    for key, value in shelves.items():
        top_stacks.append(shelves[key].pop())

    solution = ''.join(top_stacks)

    print(solution)
    