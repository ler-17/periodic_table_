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

def make_dic(monstrosity):
    dic = {}
    guy = 0
    i = 0
    while i < len(monstrosity):
        if monstrosity[i].isnumeric():
            num = get_num(monstrosity[i:])
            dic[monstrosity[guy:i]] = dic.get(monstrosity[guy:i], 0) + num
            guy = i + len(str(num))
            i += len(str(num)) - 1
        i += 1

    return dic

def get_molar_mass(dic, data):
    molar_mass = 0
    for element in dic:
        molar_mass += data[element] * float(dic[element])
    return molar_mass


# print(make_monstrosity("H826C"))
# monstrosity = make_monstrosity("H826C")
# print(make_dic(monstrosity))
# dic = make_dic(monstrosity)
# print(get_molar_mass(dic, data))

print("Enter species :D (no parenthesis): ")
species = input()
print("Molar mass : " + str(get_molar_mass(make_dic(make_monstrosity(species)), data)))


