file_input = open("day12input.txt", "r")
input_list = file_input.read().splitlines()


class Pathpoint:
    def __init__(self, name: str = (0, 0), next: set = set()):
        self.name = name
        self.big = self.name.isupper()
        self.next = next

input_list = (list(map(lambda dash: dash.split("-"), input_list)))
Pathpoints = []

for i in input_list:
    for j in i:
        if j in [p.name for p in Pathpoints]:
            for p in Pathpoints:
                if p.name == j:
                    if j == i[0]:
                        p.next.add(i[1])
                    else:
                        p.next.add(i[0])
        else:
            if j == i[0]:
                Pathpoints.append(Pathpoint(name=j, next={i[1]}))
            else:
                Pathpoints.append(Pathpoint(name=j, next={i[0]}))


def startend(pathpoint):
    if pathpoint.name == "start":
        return "A"
    elif pathpoint.name == "end":
        return "z"
    else:
        return pathpoint.name


def findnode(node):
    for i in Pathpoints:
        if i.name == node:
            main_deets = (i.name, i.next, i.big, [])
            for i in main_deets[1]:
                for p in Pathpoints:
                    if p.name == i:
                        main_deets[3].append(p)
            return main_deets


Pathpoints = sorted(Pathpoints, key=lambda x: startend(x))

wins = []
def next_options (wip=[]):
    poi = False
    g=[]
    for path in wip:
        if path == ['start','b','A']:
            poi = True
        else:
            poi = False
        if "fail" not in path:
            for i in range(len(findnode(path[-1])[3])):
                f = findnode(path[-1])[3][i]
                if f.name == "b" and poi:
                    print (path,"b up next")
                if "end" in path or "fail" in path:
                    pass
                elif f.name == "end":
                    q = path + [f.name]
                    g.append(q)
                elif f.name == "start":
                    pass
                elif f.big:
                    if path[-1] != f.name:
                        q = path + [f.name]
                        g.append(q)
                    else:
                        q = path + ["fail"]
                        g.append(q)
                elif f.name not in path:
                    q = path + [f.name]
                    g.append(q)
                elif (path.count(f.name) <= 1 and f.name != "start" and f.name !="end"):
                    unique = list(dict.fromkeys(path))
                    counts = [path.count(i) for i in unique if i != "start" and i != "end" and i!= f.name and i.islower()]
                    if len(counts)!=0:
                        if max(counts) >= 2:
                            q = path + ["fail"]
                            g.append(q)
                        else:
                            q = path + [f.name]
                            g.append(q)
                    else:
                        q = path + [f.name]
                        g.append(q)
                else:
                    q = path + ["fail"]
                    g.append(q)
    for i in g:
        if "end" in i:
            wins.append(i)
    return g

p = Pathpoints[0]
results = [[p.name]]

while not all("fail" in i or "end" in i for i in results):
    results = next_options(results)

for i in wins:
    print(str(i))
print(len(wins))

