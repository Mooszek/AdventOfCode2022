import os
os.chdir(os.path.dirname(__file__))

with open("input.txt", "r") as input_file:

    max = 0
    elf_carrying = 0
    for line in input_file:
        cur_calor = line.replace('\n', '')
        if cur_calor != "":
            elf_carrying += int(cur_calor)
        else:
            if max < elf_carrying:
                max = elf_carrying
            elf_carrying = 0

   
print(max)

