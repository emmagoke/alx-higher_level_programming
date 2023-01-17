#!/usr/bin/python3
def roman_to_int(roman_string):
    # The dictionary of roman numerals
    rom = {'I': 1, 'V':5, 'X':10,'L':50, 
            'C':100,'D':500, 'M':1000}
    result = 0
    if type(roman_string) != str or roman_string is None:
        return result
    
    lens = len(roman_string)

    for num in range(lens):
        if num >= 1:
            if (rom[roman_string[num]] > rom[roman_string[num - 1]]):
                result -= rom[roman_string[num - 1]]
                result += rom[roman_string[num]] - rom[roman_string[num - 1]]
            else:
                result += rom[roman_string[num]]
        else:
            result += rom[roman_string[num]]

    return (result)
