polymer = "PFVKOBSHPSPOOOCOOHBP"

s = {}
for i in polymer:
    if i not in s:
        s[i] = 1
    else:
        s[i] += 1



file_input = open("day14input.txt", "r")
input_list = file_input.read().splitlines()
rule_bit = input_list[2:]
rules = {}
for i in rule_bit:
    inputs = i[:2]
    outputs = i[-1]
    rules[inputs] = outputs

for i in rules.values():
    if i not in s:
        s[i] = 0

pairs = {}
for i in rules.keys():
    pairs[i] = 0

for index in range(len(polymer) - 1):
    pair = polymer[index:index + 2]
    pairs[pair] += 1

print("pairs",pairs)
print("s",s)
print("rules",rules)

for i in range(40):
    pairs_to_add = []
    for pair in pairs:
        s[rules[pair]] += pairs[pair]       #update the totals, based on the number present
        if pairs[pair] > 0:
            pairs_to_add.append((pair,pairs[pair]))
        pairs[pair]=0
#    pairs[pair] = 0

    print("pairs_to_add",pairs_to_add)

    for pair in pairs_to_add:
        for rule in rules.keys():           #rules are the list of keys
            if rule == pair[0]:
                first_letter_in_rule = rule[0]
                second_letter_in_rule = rule[1]
                result = rules[pair[0]]

                pairs[first_letter_in_rule+result] += pair[1] # add the first new pair
                pairs[result+second_letter_in_rule] += pair[1] #add the second new pair



    print("=================================================")
    print("new pairs", pairs)
    print("new s", s)

max_key = max(s, key=lambda key: s[key])
min_key = min(s, key=lambda key: s[key])

print(s[max_key]-s[min_key])


'''steps = 40
# 4171629740081 is too high



for step in range(steps):
    count=0
    additions={}
    for i in rules:
        first_bit = i[0]
        second_bit = i[1]
        for index in range(len(polymer)-1):
            pair = polymer[index:index+2]
            if pair == first_bit:
                count+=1
                additions[index] = second_bit

    new_length = len(polymer) + count
    new_poly= ""
    for i in range(new_length):
        if i in additions:
            new_poly = new_poly + polymer[0]+ additions[i]
            polymer=polymer[1:]

        elif len(polymer) >0:
            new_poly = new_poly + polymer[0]
            polymer=polymer[1:]

    polymer = new_poly

    s = {}
    for i in polymer:
        if i not in s:
            s[i] = 1
        else:
            s[i] += 1

    max_key = max(s, key=lambda key: s[key])
    min_key = min(s, key=lambda key: s[key])

    print(polymer)
    print(s[max_key] - s[min_key], max_key, min_key)

s = {}
for i in polymer:
    if i not in s:
        s[i] = 1
    else:
        s[i] += 1

max_key = max(s, key=lambda key: s[key])
min_key = min(s, key=lambda key: s[key])

print(s[max_key]-s[min_key])

#Concept:
#identify the number of times a given pair is created
# each time, the overall number will double- except for the very first and very last character.'''

