#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_li = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_li.append(replace)
        else:
            new_li.append(my_list[i])
    return new_li
