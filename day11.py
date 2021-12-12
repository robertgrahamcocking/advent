'''parts one and two combined- part one section mainly commented out'''

file_input = open("day11input.txt", "r")
input_list = file_input.read().splitlines()
print(input_list)
rows = len(input_list)
columns = len(input_list[0])

class Octopus:
    def __init__(self, location: tuple = (0,0) , energy_level: int = 0):
        self.location = location
        self.energy_level = int(energy_level)
        self.adjacent = [(location[0]+rowadjust,location[1]+coladjust) for rowadjust in range(-1,2) for coladjust in range(-1,2) if
                         location[0]+rowadjust>=0 and
                         location[1]+coladjust>=0 and
                         location[0]+rowadjust < rows and
                         location[1]+coladjust < columns and
                         (location[0]+rowadjust,location[1]+coladjust) != self.location]
        self.flashcount = set()
        self.flashed = False

Steps = [_ for _ in range(1,1001)]
Octopi = [Octopus((row,column),energy) for row, rowvalues in enumerate(input_list) for column, energy in enumerate(rowvalues)]
newflash = 0

for step in Steps:
    count = 0
    for o in Octopi:
        o.flashed = False
    print("step",step)
    for o in Octopi:
        o.energy_level += 1 #add one
        if o.energy_level > 9:
            o.flashcount.add(step)
            o.energy_level = 0
            newflash += 1

    while newflash > 0:
        for o1 in Octopi: #looking at each octopus
            if step in o1.flashcount and o1.flashed == False: #which has flashed but hasn't yet activated others
                o1.flashed = True  # this can no longer appear in the loop of to-flash octopuses
                newflash -= 1
#                print("octopus at", o1.location, "flashed. flash level down to", newflash)
                for adj in o1.adjacent: #if we now look at that octopus's neighbours...
                    for o2 in Octopi:
                        if o2.location == adj \
                                and o2.location != o1 \
                                and o2.energy_level != 0 and o2.flashed == False:
                            o2.energy_level += 1 #energy goes up
                            if o2.energy_level > 9: #and some neighbours might flash
                                o2.flashcount.add(step)
                                o2.energy_level = 0
                                newflash += 1
#                               print("octopus at",o2.location,"reached 10","flashlevel=",newflash)

    if all(step in o.flashcount for o in Octopi):
        print(step)

        count = 0
        for i in Octopi:
            count += (len(i.flashcount))
        print("flashes =",count)
        print("------------------------------")
        for i in range(rows):
            print([o.energy_level for o in Octopi if o.location[0] == i])
        print("------------------------------")

        break


#count = 0
#for i in Octopi:
#    count += (len(i.flashcount))
#print("flashes =", count)
#print(count)