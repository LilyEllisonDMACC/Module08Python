"""
Program: sort_and_search_array.py
Author: Lily Ellison
Last date modified: 03/02/2023

The purpose of this program is to sort and search an array using two functions.

"""

import array as arr


def sort_array(a_array):
    """
    Accepts an array and preforms the sort function on it.
    :param a_array: any array submitted
    :return: none, the function acts on the items in the array to sort it, no return is needed
    """
    a_array.sort()


def search_array(a_array, item):
    """
    Accepts an array and an item to locate in the array, returns the index of said item
    :param a_array: any array
    :param item: subject of the search, to be located in the array
    :return: the number of the item's index
    """
    index_num = a_array.index(item)
    return index_num


if __name__ == '__main__':
    #Create array:
    my_array = [15, 30, 5, 200, 25]
    #display original array:
    print("My array: " + str(my_array))
    #call search function to identify index of 5 and display results:
    print("Index of '5': " + str(search_array(my_array, 5)))
    #Sort array: (no return required as this function acts on the array)
    sort_array(my_array)
    #Display results of sorting:
    print("Sorted: " + str(my_array))
    #call search function to identify index of 5 and display results:
    print("New index of '5': " + str(search_array(my_array, 5)))


'''
Testing:
My array: [15, 30, 5, 200, 25]
Index of '5': 2
Sorted: [5, 15, 25, 30, 200]
New index of '5': 0

Process finished with exit code 0
'''