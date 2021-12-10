f = open("day7input.txt", "r")
l = f.read().split(",")
crabs = list(map(int, l))

print(crabs)

### part 1 ###
checklist = {}
for i in range(min(crabs), max(crabs) + 1):
    total = 0
    for j in crabs:
        total += (i - j if i - j > 0 else j - i)
    checklist[i] = total
print(min(checklist.values()))

position = 16
moveto = 5


def fuelcheck(position, moveto):
    fuel = 0
    lo = min(position, moveto)
    hi = max(position, moveto) - lo + 1
    for i in range(hi):
        fuel += i
    return fuel


checklist = {}
for i in range(min(crabs), max(crabs) + 1):
    total = 0
    for j in crabs:
        total += fuelcheck(i, j)
    checklist[i] = total

print(min(checklist.values()))
