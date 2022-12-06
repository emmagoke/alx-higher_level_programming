#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lens = len(my_list) - 1
    if (idx < 0) or (idx > lens):
        return my_list
    else:
        for i in range(lens + 1):
            if i == idx:
                my_list.remove(my_list[i])
                return my_list
