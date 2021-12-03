#---------------------------part1----------------------------------------------------------------------------------#

f = open("day3.txt", "r")
l = f. read(). splitlines()


def part_1(l, length=12, gamma = [],epsilon = [], new= []):
    for i in range(length):
        new.append([int(j[i]) for j in l])
    for k in new:
        if sum(k) > len(l)/2:
            gamma.append(1)
            epsilon.append(0)
        else:
            epsilon.append(1)
            gamma.append(0)

    gamstring = ''.join(str(e) for e in gamma)
    epstring =  ''.join(str(e) for e in epsilon)

    return(int(gamstring, 2) * int(epstring, 2))

print(part_1(l,12))

#---------------------------part2----------------------------------------------------------------------------------#

def gaschecker(l,length=12,oxygen=True):
    for bit in range(length):
        #sorting the list allows for repeated winnowing by slicing the front or back section off
        l = sorted(l, key=lambda x: int (x[bit]))
        #taking the sum determines whether there are more ones than zeroes in a given column
        bit_list = [int(i[bit]) for i in l]
        s = sum(bit_list)
        #if s is more than half the length, then 1 must be more popular
        if s >= len(bit_list) / 2:
            if oxygen:
                l = l[len(bit_list) - s:] # zeroes from the front or ones from the end, depending on the gas
            else:
                l = l[:len(bit_list) - s]
            if len(l) == 1:
                return l
        else:
            if oxygen:
                l = l[:len(bit_list) - s]
            else:
                l = l[len(bit_list) - s:]
            if len(l) == 1:
                return l


oxstring = ''.join(str(e) for e in gaschecker(l,12,True))
co2string = ''.join(str(e) for e in gaschecker(l,12,False))

print(int(oxstring,2) * int(co2string,2))
