f = open("day5input.txt", "r")
l = f. read(). splitlines()
l = (list(map(lambda coord: coord.split(","),[i.replace(" -> ",",") for i in l]))) #convert to list of four coordinates

m = []

'''---part 1'''

for i in l:
    if i[0] == i[2]:
        x = int(i[0])
        y1 = min( int(i[3]),int(i[1])  )
        y2 = max( int(i[3]),int(i[1])  )
        m.append([x,y1,y2,True])

    elif i[1] == i[3]:
        y = int(i[1])
        x1 = min(int(i[0]), int(i[2]))
        x2 = max(int(i[0]), int(i[2]))
        m.append([y,x1,x2,False])

def add_to_dict_and_count (l,coords):
    for i in l:
        for j in range(i[1],i[2]+1):
            if i[3]:
                coord = (i[0],j)
            else:
                coord = (j,i[0])
            if coord in coords:
                coords[coord] += 1
            else:
                coords[coord] = 1

    return coords

coords = {}
output = add_to_dict_and_count(m,coords)
overall = 0
for i in output.values():
    if i > 1:
        overall +=1
print(overall)

###----------part 2-----------###

def add_to_dict_and_count_2 (l,coords):

    for i in l:
        x1 = int(i[1])
        x2 = int(i[3])

        y1 = int(i[0])
        y2 = int(i[2])

        xlen = max(x1,x2)-min(x1,x2)
        ylen = max(y1,y2)-min(y1,y2)

        xs = [j for j in range(x1,x2+(-1 if x1 > x2 else 1),(-1 if x1 > x2 else 1))] if x1!= x2 else [x1 for _ in range(ylen+1)]
        ys = [k for k in range(y1,y2+(-1 if y1 > y2 else 1),(-1 if y1 > y2 else 1))] if y1!= y2 else [y1 for _ in range(xlen+1)]
        coordstep = list(zip(xs,ys))

        for i in coordstep:
            if i in coords:
                coords[i] += 1
            else:
                coords[i] = 1
    return coords

coords = {}
output = add_to_dict_and_count_2 (l,coords)
overall = 0
for i in output.values():
    if i > 1:
        overall +=1

print(overall)