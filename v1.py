import json

f = open("periodic_table.json")
data = json.loads(f.read())
f.close()

# assumptions : numbers are single digits
def get_molar_mass(element, data):
    # base cases

    # (1) length is 1:
    if len(element) == 1:
        return data[element]
    # (2) length is 2
    # (2a) second char is lower
    # (2b) second char is number
    if len(element) == 2:
        if element[1].islower(): # He
            return data[element]
        elif element[1].isnumeric(): # H2
            return data[element[0]] * float(element[1])
        else: #HC
            return data[element[0]] + get_molar_mass(element[1:], data)

    # (3) length is 3
    # (3a) 2 char element with number
    # (3b) HHe
    # (3c) HeH
    # (3d) H2C
    # (3e) HC2
    if len(element) == 3:
        if element[2].isnumeric():
            if element[1].islower(): # e.g. He2
                return data[element[:2]] * float(element[2])
            elif element[1].isupper(): # e.g. HC2
                return data[element[0]] + get_molar_mass(element[1:], data)

        elif element[2].islower(): #HHe
            return data[element[0]] + get_molar_mass(element[1:], data)

        else: # last char is upper
            if element[1].isnumeric(): # H2C
                return data[element[0]] * float(element[1]) + get_molar_mass(element[2:], data)
            elif element[1].islower(): # HeH
                return data[element[:2]] + get_molar_mass(element[2:], data)
            else: #HCH
                return data[element[0]] + get_molar_mass(element[1:], data)

    # no more base cases
    # assumptions : longer than 3
    #               at least 2 elements (recurse in every case)
    # first char is always upper (assume valid input)

    # (1) all cases with lone upper at the front:
    # (1a) H2 - third char number (1b) H - third char not number
    if element[1].isupper(): # H... HHe... HH2...
        return data[element[0]] + get_molar_mass(element[1:], data)

    elif element[1].isnumeric(): # H2...
        return data[element[0]] * float(element[1]) + get_molar_mass(element[2:], data)

    elif element[1].islower(): # HeH... He2...
        if element[2].isnumeric():
            return data[element[0:2]] * float(element[2]) + get_molar_mass(element[3:], data)
        else:
            return data[element[0:2]] + get_molar_mass(element[2:], data)


print(get_molar_mass("H8C2Ca3", data))