l=[3,4,3,1,2]

def reduce_numbers_2(l,days=0,limit=18):
    appendcount = 0
    for index, item in enumerate(l):  # the passage of a day:
        if item == 0:
            appendcount += 1
            l[index] = 6
        else:
            l[index] -= 1
    for i in range(0, appendcount):
        l.append(8)
    days += 1
    if days < limit:
        reduce_numbers_2(l,days, limit)  # recursive call
    else:
        print("answer is",len(l))

'''will take an extremely long time to run with a longer input'''

reduce_numbers_2(l[0:1],0,2)
reduce_numbers_2(l[0:1],0,4)
reduce_numbers_2(l[0:1],0,80)


