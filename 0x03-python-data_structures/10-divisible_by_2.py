#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:  # empty list
        return False
    else:
        out = []   # output list
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                out.append(True)
            else:
                out.append(False)
        return out
