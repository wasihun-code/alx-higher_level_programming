#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    list3 = my_list_1
    listlength = len(my_list_1)

    try:
        for i in range(0, listlength):
            try:
                list3[i] = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                list3[i] = 0
                print("division by 0")
                pass
            except TypeError:
                list3[i] = 0
                print("wrong type")
                pass
            except IndexError:
                print("out of range")
                pass
    except:
        pass

    return list3
