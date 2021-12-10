# --------------------------"part1"----------------------------------------------------------------------#
# ------------------turning grid file into a list of 3-part tuples---------------------------------------#
# -first tuple is the grid ref, second is the row num, and third is a list of values on the row----------#
# --------------------second part of tuple is actually redundant, but helped with readability------------#

f = open("day4input.txt", "r")
l = f.read().splitlines()

grids = []
block_number = 0
row_number = 0

for index, item in enumerate(l):
    if item == "":
        row_number = 0
        block_number += 1
    else:
        grids.append((block_number, row_number, list(map(int, item.split()))))
        row_number += 1

# --------------------getting the list of bingo calls--------------------------------------------------#

f = open("day4input.txt", "r")
inp = f.read().split(",")
inp = [int(i) for i in inp]


# -----sumcolumns checks the sum of columns in a given grid to see if bingo has been achieved--------- #

def sumcolumns(gridnum=1, griddio=grids):
    column = []
    for i in range(5):
        if sum([tuple[2][i] for tuple in griddio if tuple[0] == gridnum]) == 0:
            return True  # return true if any of the columns in the grid sum to 0


# ----------amend_rows finds the called number in all grids, and changes the number found to 0--------#

def amend_rows(griddia=grids, inp=inp):
    for i in inp:
        for tuple in griddia:
            for index, number in enumerate(tuple[2]):
                if number == i:
                    tuple[2][index] = 0
                    if sum(tuple[2]) == 0 or sumcolumns(tuple[0], griddia):
                        return (i, sum([sum(xtuple[2]) for xtuple in griddia if xtuple[0] == tuple[0]]))  # return
                        # sum of the remaining grid


# ----------if the row sum or column sum is 0, the grid is the winner -------------------------------#

totals = (amend_rows(grids, inp))

print(totals[0] * totals[1])

# --------------------------"part2"----------------------------------------------------------------------#
# --amends part 1 solution, so that the result is only returned once 99 other successes have been found--#

s = len(set([tuple[0] for tuple in grids]))


def amend_rows_2(griddia=grids, inp=inp, winners=set()):
    for i in inp:
        for tuple in griddia:
            for index, number in enumerate(tuple[2]):
                if number == i and tuple[0] not in winners:
                    tuple[2][index] = 0
                    if sum(tuple[2]) == 0 or sumcolumns(tuple[0], griddia):
                        winners.add(tuple[0])
                        if len(winners) == s:
                            return (i, sum([sum(xtuple[2]) for xtuple in griddia if xtuple[0] == tuple[0]]))


totals = (amend_rows_2(grids, inp))

print(totals[0] * totals[1])
