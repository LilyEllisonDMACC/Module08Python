"""
Program: assign_level.py
Author: Lily Ellison
Last date modified: 03/02/2023

The purpose of this program is to implement a switch/case with a dictionary. Assign points for reaching levels in a
game.

"""

def switch_level():
    """
    Requests and validates user level input and assigns points based on level. Returns point value
    :return: user_points - the values associated with the level keys in the dictionary, options are 50, 150, 300, or 500
    """
    #primes sentinel value for loop:
    valid_input = False
    #create level_points dictionary to assign points to levels:
    level_points = {'N': 50, 'B': 150, 'E': 300, 'A': 500}
    while not valid_input:
        # prompts user for specific input:
        level = input("Please enter your level using the first letter of the level name: [N]ovice, [B]eginner, "
                      "[E]xperienced, or [A]dvanced: ")
        try:
            # validates that user entry is a letter, converts it to upper case, and checks if it's one of the keys in
            #the dictionary
            user_points = level_points[level.upper()]
        except KeyError:
            #informs user of invalid entry:
            print("Invalid entry. Please try again.")
            #continues loop
            continue
        else:
            valid_input = True
            #valid keys are found and the associated values are returned
            return user_points


if __name__ == '__main__':
    #calls method:
    points = switch_level()
    #displays results:
    print("Congratulations! You now have " + str(points) + " points!")

    '''
    Testing:
    
    Please enter your level using the first letter of the level name: [N]ovice, [B]eginner, [E]xperienced, or [A]dvanced: n
    Congratulations! You now have 50 points!

    Please enter your level using the first letter of the level name: [N]ovice, [B]eginner, [E]xperienced, or [A]dvanced: b
    Congratulations! You now have 150 points!
    
    Please enter your level using the first letter of the level name: [N]ovice, [B]eginner, [E]xperienced, or [A]dvanced: e
    Congratulations! You now have 300 points!
    
    Please enter your level using the first letter of the level name: [N]ovice, [B]eginner, [E]xperienced, or [A]dvanced: i
    Invalid entry. Please try again.
    Please enter your level using the first letter of the level name: [N]ovice, [B]eginner, [E]xperienced, or [A]dvanced: 9
    Invalid entry. Please try again.
    Please enter your level using the first letter of the level name: [N]ovice, [B]eginner, [E]xperienced, or [A]dvanced: A
    Congratulations! You now have 500 points!
        
    '''
