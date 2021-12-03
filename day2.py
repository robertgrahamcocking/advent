import pandas as pd

l = pd.read_csv('day2.txt', sep="\n", header=None)[0].tolist()

def part_1(hor=0,dep=0):
    for i in l:
        if i.find(" ") == 2:
            dep -= int(i[3:])
        elif i.find(" ") == 4:
            dep += int(i[4:])
        else:
            hor += int(i[7:])

    return(hor * dep)

def part_2(hor=0,dep=0,aim=0):

    for i in l:
        if i.find(" ") == 4:
            aim += int(i[4:])
        elif i.find(" ") == 2:
            aim -= int(i[2:])
        else:
            hor += int(i[7:])
            dep += (aim* int(i[7:]))

    return(hor * dep)

print(part_1())
print(part_2())