f = open("day10input.txt", "r")
rows = f.read().splitlines()

d = {"[": "]", "{": "}", "(": ")", "<": ">"}
db = {")": 3, "]": 57, "}": 1197, ">": 25137}
dc = {")": 1, "]": 2, "}": 3, ">": 4}


class Bracket:
    def __init__(self, open_bracket: str = None, close_bracket: str = None, Lev: int = 0):
        self.open_bracket = open_bracket
        self.level = Lev
        self.close_bracket = close_bracket


problems = []
scores = []

for line in rows:
    brackets = []
    level = 0
    score = 0
    for item in line:
        if item in d:
            brackets.append(Bracket(open_bracket=item, Lev=level))
            level += 1
        elif item in d.values():
            brackets[-1].close_bracket = item
            open = d[brackets[-1].open_bracket]
            close = brackets[-1].close_bracket
            if open != close:
                problems.append(db[item])
                brackets.append("kill")
                break
            else:
                brackets.pop()

    if "kill" in brackets:
        brackets = []
    brackets.sort(key=lambda b: b.level, reverse=True)
    for i in [dc[d[b.open_bracket]] for b in brackets if "kill" not in brackets]:
        score = (score * 5) + i
    if score > 0:
        scores.append(score)

scores.sort()
langth = len(scores)
result = scores[(langth // 2)]
print(result)
