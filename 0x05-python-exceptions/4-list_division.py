#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    if (list_length < len(my_list_1)) or (list_length < len(my_list_2)):
        print("out of range")
        return result
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
            result.append(ans)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
        finally:
            continue

    return result
