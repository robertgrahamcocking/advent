file_input = open("day13input.txt", "r")
input_list = file_input.read().splitlines()
for index, item in enumerate(input_list):
    if item == "":
        inlist = input_list[:index]
        folds = input_list[index+1:]

inlist = [i.split(",") for i in inlist]
inlist = [tuple(map(int, i)) for i in inlist]
inlist.sort(key= lambda x: x[1])

def visualise(paper):
    columns = max([_[0] for _ in paper])
    rows = max([_[1] for _ in paper])
    for row in range(rows+1):
        tempstring = ""
        for column in range(columns+1):
            if (column,row) in inlist:
                tempstring += "X"
            else:
                tempstring += " "
        print(tempstring)

folds = (list(
    map(lambda x: x.split("="), [i.replace("fold along ", "") for i in folds])))

for fold in folds:

        columns = int(max([_[0] for _ in inlist]))
        rows = int(max([_[1] for _ in inlist]))
        split = int(fold[1])
        x_or_y = fold[0]

        if x_or_y == "y":
            halfway = rows // 2
            if split >= halfway:
                inlist = [(i[0],split*2 -i[1]) if i[1] > split else i for i in inlist]
            else:
                inlist = [(i[0],split*2 -i[1]) if i[1] > split else (halfway-split+i[0], split * 2 - i[1]) for i in inlist]
                list(dict.fromkeys(inlist))


        if x_or_y == "x":
            halfway = columns // 2
            if split >= halfway:
                inlist = [(split*2-i[0],i[1]) if i[0] > split else i for i in inlist]
            else:
                inlist = [(split*2-i[0],i[1]) if i[0] > split else (split*2-i[0] , halfway-split+i[1] ) for i in inlist]
                list(dict.fromkeys(inlist))

visualise(inlist)


'''for fold in folds:
        if fold[0] == "x":
            inlist = [ ( int(fold[1]) - (item[0] - int(fold[1]) ),   item[1]  )  for item in inlist ]
            m = min([i[0] for i in inlist])
            if m <0:
                inlist = [ (item[0] - m if item[0] < int(fold[1]) else item[0], item[1]  )  for item in inlist ]
            list(dict.fromkeys(inlist))
            visualise(inlist)
            print(fold, inlist)

        elif fold[0] == "y":
            inlist = [ ( item[0] ,  int(fold[1]) - (item[1] - int(fold[1]) )  )  for item in inlist  ]
            m = min([i[1] for i in inlist])
            if m <0:
                inlist = [ (item[0], item[0] - m if item[1] < int(fold[1]) else item[1]  )  for item in inlist ]
            list(dict.fromkeys(inlist))
            print(fold, inlist)

visualise(inlist)

#            [(fold[1] - (i[0] - fold[1]) if i[0] > fold[1] else i[0]),i[1]] for i in inlist]
#    elif fold[0] == "y":
#        inlist = [inlist[i][0], (fold[1] - (inlist[i][0] - fold[1]))]

#        inlist = [[i[0],(fold[1] - (i[0] - fold[1]) if i[0] > fold[1] else i[0])] for i in inlist]'''




