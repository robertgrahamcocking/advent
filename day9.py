f = open("day9input.txt", "r")
l = f.read().splitlines()


def find_troughs(l):  ##part one - the coords.add part gives the solution to part one. Also used in part 2.
    mins = []
    coords = set()
    for row_num, row in enumerate(l):
        for column_num, item in enumerate(row):
            if row_num == 0 and column_num == 0:
                if l[1][0] > item and l[0][1] > item:
                    mins.append(int(item) + 1)
                    coords.add(row_num)

            elif column_num == len(row) - 1 and row_num == len(l) - 1:
                if l[row_num - 1][column_num] > item and l[row_num][column_num - 1] > item:
                    mins.append(int(item) + 1)
                    coords.add(row_num)

            elif row_num == 0 and column_num == len(row) - 1:
                if l[0][column_num - 1] > item and l[row_num + 1][column_num] > item:
                    mins.append(int(item) + 1)
                    coords.add((row_num, column_num))

            elif row_num == 0:
                if l[0][column_num - 1] > item and l[0][column_num + 1] > item and l[row_num + 1][column_num] > item:
                    mins.append(int(item) + 1)
                    coords.add((row_num, column_num))

            elif row_num == len(l) - 1:
                if l[row_num][column_num - 1] > item and l[row_num][column_num + 1] > item and l[row_num - 1][
                    column_num] > item:
                    mins.append(int(item) + 1)
                    coords.add((row_num, column_num))

            elif column_num == 0:
                if l[row_num - 1][0] > item and l[row_num + 1][0] > item and l[row_num][column_num + 1] > item:
                    mins.append(int(item) + 1)
                    coords.add((row_num, column_num))

            elif column_num == len(row) - 1:
                if l[row_num - 1][column_num] > item and l[row_num + 1][column_num] > item and l[row_num][
                    column_num - 1] > item:
                    mins.append(int(item) + 1)
                    coords.add((row_num, column_num))

            else:
                if l[row_num - 1][column_num] > item and l[row_num + 1][column_num] > item and l[row_num][
                    column_num - 1] > item and l[row_num][column_num + 1] > item:
                    mins.append(int(item) + 1)
                    coords.add((row_num, column_num))

    return coords


def surrounded(row, column, grid, relset):
    output = [(), (), (), ()]

    upcheck = False
    if row == 0:
        upcheck = True
    elif (grid[row - 1][column] == "9" or grid[row - 1][column] in relset):
        upcheck = True
    if upcheck == False:
        output[0] = (row - 1, column)
    else:
        output[0] = ()

    downcheck = False
    if row == len(grid) - 1:
        downcheck = True
    elif grid[row + 1][column] == "9" or grid[row + 1][column] in relset:
        downcheck = True

    if downcheck == False:
        output[1] = (row + 1, column)
    else:
        output[1] = ()

    leftcheck = False
    if column == 0:
        leftcheck = True

    elif grid[row][column - 1] == "9" or grid[row][column - 1] in relset:
        leftcheck = True

    if leftcheck == False:
        output[2] = (row, column - 1)
    else:
        output[2] = ()

    rightcheck = False
    if column == len(grid[0]) - 1:
        rightcheck = True
    elif grid[row][column + 1] == "9" or grid[row][column + 1] in relset:
        rightcheck = True

    if rightcheck == False:
        output[3] = (row, column + 1)
    else:
        output[3] = ()

    return output


class cavespot:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.linkvals = surrounded(dataval[0], dataval[1], l, set())


troughlens = []

for i in find_troughs(l):
    trough = []
    start = cavespot(i)
    cont = True

    trough.append(start.dataval)
    [trough.append(j) for j in ([i for i in start.linkvals if i != () and i not in trough])]

    while cont:
        startlength = len(trough)  # start length = startlength)
        for i in trough[1:]:
            start = cavespot(i)  # new trough is
            [trough.append(j) for j in ([i for i in start.linkvals if i != () and i not in trough])]
        endlength = len(trough)
        if startlength == endlength:  # if the trough has stopped growing
            cont = False

    troughlens.append(len(trough))

troughlens.sort(reverse=True)
print(troughlens)
print(troughlens[0] * troughlens[1] * troughlens[2])
