import os
import numpy as np

os.chdir(os.path.dirname(__file__))

def fillMap(map_list, input_list_of_lists, is_mirrored):
    treeline_index = 0
    for treeline in input_list_of_lists:
        if is_mirrored:
            tree_index= len(treeline)-1
        else:
            tree_index = 0
        maximum = treeline[0]
        map_list[treeline_index][tree_index]=1
        for tree in treeline:
            if int(tree) > int(maximum):
                maximum = tree
                map_list[treeline_index][tree_index] = 1
            if is_mirrored:
                tree_index-= 1
            else:
                tree_index+= 1
        treeline_index +=1
    return map_list

#################################
#####   Horizontal map    #######
#################################

puzzle_input = []
with open("input.txt", "r") as input_file:
    for line in input_file:
        puzzle_input.append(line.strip('\n'))

mirrored = [line[::-1] for line in puzzle_input]

treeline_map = []

tree_index = 0
for treeline in puzzle_input:
    treeline_map.append([1])
    maximum = treeline[0]
    for tree in treeline[1:]:
        if int(tree) > int(maximum):
            maximum = tree
            treeline_map[tree_index].append(1)
        else:
            treeline_map[tree_index].append(0)
    tree_index +=1


fillMap(treeline_map, mirrored, is_mirrored=True)
 
#################################
#####   Vertical map    #########
#################################

list_to_rotate =[list(element) for element in puzzle_input ]
transposed_puzzle_input = np.rot90(list_to_rotate,3).tolist()

vertical_input =[('').join(transposed_element) for transposed_element in transposed_puzzle_input]
transpose_treeline_map = np.rot90(treeline_map,3).tolist()
fillMap(transpose_treeline_map, vertical_input, is_mirrored=False)

transposed_mirrored = [line[::-1] for line in vertical_input]
fillMap(transpose_treeline_map, transposed_mirrored, is_mirrored=True)

total = 0
for number in transpose_treeline_map:
    total+=(sum(number))

print(total)

 

