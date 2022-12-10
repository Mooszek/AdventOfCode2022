import os
import pprint as pp

os.chdir(os.path.dirname(__file__))

signals = []

with open("input.txt", "r") as input_file:
    for line in input_file:
        if line.strip('\n').split(' ')[0]=='addx':
            signals.append(0)
            signals.append(int(line.strip('\n').split(' ')[1]))
        else:
            signals.append(0)


signal_value = 1
cycle =0
picture = []

position_to_write = cycle
for signal in signals:
    cycle+=1
    if signal_value in [position_to_write-1, position_to_write, position_to_write + 1]:
        picture.append('#')
    else:
        picture.append('.')
    position_to_write+=1
    signal_value += signal
    if cycle in [40,80,120,160,200,240]:
        position_to_write =0

picture.reverse()
    
finalstring = ''

for row in range(6):
    for sign in range(40):
        try:
            finalstring +=picture.pop()
        except:
            pass
    finalstring+= '\n'

pp.pprint(finalstring)

