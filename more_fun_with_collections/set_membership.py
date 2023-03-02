"""
Program: set_membership.py
Author: Lily Ellison
Last date modified: 03/02/2023

The purpose of this program is to determine if a given value is within a give set of elements.

"""


def in_set(search_set, search_value) :
    """
    Accepts a set and a value and checks if the value is held in the set
    :param search_set: set of elements that might hold value
    :param search_value: value of interest that might be in submitted set
    :return: False if not found, True if found (boolean)
    """
    return search_value in search_set


if __name__ == '__main__':
    #initialize set
    test_set = {"Pegasus", "Hercules", "Hazel"}
    #initialize test value
    test_value = "Akira"
    #call method with parameters
    value_in_set = in_set(test_set, test_value)
    #set result to the appropriate response from the method for printing
    if not value_in_set:
        result = " not "
    else:
        result = " "
    #Print results:
    print("The value '" + test_value + "' is" + str(result) + "in the set " + str(test_set))
    #new test value, same process:
    test_value = "Hazel"
    value_in_set = in_set(test_set, test_value)
    if not value_in_set:
        result = " not "
    else:
        result = " "
    print("The value '" + test_value + "' is" + str(result) + "in the set " + str(test_set))

    """
    Testing:
    The value 'Akira' is not in the set {'Hercules', 'Pegasus', 'Hazel'}
    The value 'Hazel' is in the set {'Hercules', 'Pegasus', 'Hazel'}

    Process finished with exit code 0
    """