#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        lar = my_list[0]  # The largest element
        for i in range(1, len(my_list)):
            if my_list[i] > lar:
                lar = my_list[i]
        return lar
