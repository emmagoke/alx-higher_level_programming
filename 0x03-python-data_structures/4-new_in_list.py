#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lens = len(my_list)
    if (idx < 0) or (idx >= lens):
        return my_list
    else:
        new_list = my_list.copy()
        for i in range(lens):
            if i == idx:
                new_list[i] = element
                return new_list
