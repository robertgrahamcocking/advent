f = open("day6input.txt", "r")
l = f.read().split(",")
l = list(map(int, l))

input_list = l
limit = 256

zeroes = input_list.count(0)
ones = input_list.count(1)
twos = input_list.count(2)
threes = input_list.count(3)
fours = input_list.count(4)
fives = input_list.count(5)
sixes = input_list.count(6)
sevens = input_list.count(7)
eights = input_list.count(8)

summary = ("x", [zeroes, ones, twos, threes, fours, fives, sixes, sevens, eights])
print(summary)

for i in range(limit):
    neweights = summary[1][0]

    summary[1][0] = summary[1][1]
    summary[1][1] = summary[1][2]
    summary[1][2] = summary[1][3]
    summary[1][3] = summary[1][4]
    summary[1][4] = summary[1][5]
    summary[1][5] = summary[1][6]
    summary[1][6] = summary[1][7]
    summary[1][7] = summary[1][8]
    summary[1][8] = neweights
    summary[1][6] = summary[1][6] + neweights

print(sum(summary[1]))
