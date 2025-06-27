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
def inject_in_substring(substring, multiple = 1):
    new_string = substring
    index = 0

    for i in range(len(substring) - 1):
        if substring[i + 1].isupper():
            if not substring[i].isnumeric():
                index += 1
                new_string = new_string[:index] + str(multiple) + new_string[index:]
            else:
                num = int(multiple) * int(new_string[index])
                new_string = new_string[:index] + str(num) + new_string[index + 1:]
        index += 1

    if not substring[len(substring) - 1].isnumeric():
        new_string = new_string + str(multiple)
    else:
        num = int(multiple) * int(new_string[index])
        new_string = new_string[:index] + str(num)

    return new_string

# now we have a function to deal with a substring. we just need to:
# (1) call in strategic locations
# (2)
def parse_whole(species):
    new_species = species
    while "(" in species:
        i_start = species.index("(")
        i_end = species.index(")")
        substring = species[i_start + 1: i_end]
        multiple = species[i_end + 1]

        if (i_end + 2) > len(species):
            rest = ""
        else:
            rest = species[i_end + 2:]

        new_species = species[:i_start] + inject_in_substring(substring, multiple) + rest
        species = new_species

    new_species = inject_in_substring(species, 1)

    return new_species

print(parse_whole("H(CHO)2Ne"))

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

print("Enter species :D : ")
species = input()
print("Molar mass : " + str(get_molar_mass(make_dic(parse_whole(species)), data)))