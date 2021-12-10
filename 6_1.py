def reduce_numbers(l, m, days=0, limit=18):
    for index, item in enumerate(l):  # the passgage of a day:
        if item == 0 and m[index]:
            l[index] = 6
            l.append(8)
            m.append(False)
        elif item == 8 and not (m[index]):
            m[index] = True
        elif item == 7:
            l[index] -= 1
            m[index] = True
        else:
            l[index] -= 1

    days += 1

    if days != limit:
        reduce_numbers(l, m, days, limit)  # recursive call
    else:
        print(len(l))