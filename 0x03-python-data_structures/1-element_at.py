#!/usr/bin/python3
def element_at(my_list, idx):
    lens = len(my_list)
    if idx < 0:
        return None
    elif idx >= lens:
        return None
    else:
        for i in range(lens):
            if i == idx:
                return my_list[i]
