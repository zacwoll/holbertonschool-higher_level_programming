#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            a = my_list_1[x] / my_list_2[x]
        except TypeError:
                print("wrong type")
                a = 0
        except ZeroDivisionError:
                print("division by 0")
                a = 0
        except IndexError:
                print("out of range")
                a = 0
        new_list.append(a)
    return new_list

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
