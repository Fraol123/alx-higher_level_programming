#!/usr/bin/python3
"""my_list is the first list and my_list_2 the second list

   innorder to divide each element we ned new_list and
   append the results to it"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):

        try:
            div = my_list_1[i] / my_list_2[i]

        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
