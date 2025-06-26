import json

f = open("periodic_table.json")
data = json.loads(f.read())
f.close()

def get_num(str):
    i = 0
    num = ''
    while i < len(str) and str[i].isnumeric():
        num += str[i]
        i += 1
    return int(num)

# find "(" and ")"
# number after ")"
# inject number after each element
# remove parenthesis
# salvage code?
# N(CHO)3Ca2
def make_monstrosity(species):
    monstrosity = species

    monstrosity_index = 0
    for i in range(len(species) - 1):
        if (species[i+1].isupper()) and not (species[i].isnumeric()):
            monstrosity_index += 1
            monstrosity = monstrosity[:monstrosity_index] + "1" + monstrosity[monstrosity_index:]
        monstrosity_index += 1

    if not species[len(species) - 1].isnumeric():
        monstrosity = monstrosity + "1"
    return monstrosity