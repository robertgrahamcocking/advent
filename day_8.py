f = open("day8input.txt", "r")
l = f. read(). splitlines()
result = 0

for line in l:
    j = str(line[:58]).split(" ")
    for p in j:
        if len(p)==2:
            one = set(i for i in p)
        elif len(p)==4:
            four = set(i for i in p)
        elif len(p)==3:
            seven = set(i for i in p)
        elif len(p)==7:
            eight = set(i for i in p)


    for p in j:
        if len(p)==6:
            if len(set(i for i in p) - four) == 2:
                nine = set(i for i in p)

    for p in j:
        if len(p)==6:
            if len(set(i for i in p) - one) == 5:
                six = set(i for i in p)

    for p in j:
        if len(p)==6:
            if set(i for i in p) != six and set(i for i in p) != nine:
                zero = set(i for i in p)

    for p in j:
        if len(p)==5:
            if len(set(i for i in p) - one) == 3:
                three = set(i for i in p)


    for p in j:
        if len(p)==5:

            if len( set(i for i in p) - nine ) == 1:
                two = set(i for i in p)

    for p in j:
        if len(p) == 5:
            if set(i for i in p) != three and set(i for i in p) != two:
                five = set(i for i in p)

    numbers = [zero,one,two,three,four,five,six,seven,eight,nine]
    print(numbers)
    print("---------------")
    print("---------------")
    print("***",seven-four,"***")
    print(four-one-two,"*",four-five)
    print("***", eight - zero, "***")
    print(two-three,"*",one-two)
    print("***", three - seven -four, "***")
    print("---------------")
    print("---------------")


    k = str(line[61:]).split(" ")
    templist = ""
    for q in k:
        for index,number in enumerate(numbers):
            if set (i for i in q) == number:
                templist = templist + str(index)
    print(templist)
    print(int(templist))
    result += int(templist)

print(result)

#part one
#for i in l:
#    i = str(i[61:]).split(" ")
#    for j in i:
#        print(len(j))
#        if len(j) in [2,3,4,7]:
#            total +=1

