#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        a = 0
        try:
            a = my_list_1[x] / my_list_2[x]
        except TypeError:
                print("wrong type")
        except ZeroDivisionError:
                print("division by 0")
        except IndexError:
                print("out of range")
        finally:
            new_list.append(a)
    return new_list
