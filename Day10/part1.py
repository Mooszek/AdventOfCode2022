import os

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

cycle =1

interesting_signals = []

for signal in signals:
    if cycle in [20, 60, 100, 140, 180, 220]:
        interesting_signals.append(signal_value * cycle)
    signal_value += signal
    cycle+=1

print(sum(interesting_signals))