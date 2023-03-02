"""
Program: topic_2_assignment_1.py
Author: Lily Ellison
Last date modified: 03/02/2023

The purpose of this program is to accept a number of test scores from the user and return the average score using a
dictionary container.

"""


def get_test_scores():
    """
    Asks user for number of test scores and then prompts them to enter that number of scores. All input is validated.
    :return: scores_dict, a dictionary container of score name ("Score1", "Score2", etc) and the score.
    """
    #creates empty dictionary:
    scores_dict = dict()
    #primes the sentinel value for the while loop:
    valid_input = False
    #enters while loop:
    while not valid_input:
        num_scores = input("Please enter the number of scores you would like to average: ")
        try:
            #checks if input was int:
            scores = int(num_scores)
            #checks if input was a positive number:
            if 0 < scores:
                #if it is a positive number, passes tests:
                valid_input = True
            else:
                #informs user entry not valid if negative:
                print("Not a valid entry. Value out of range.")
                #goes back to top of loop:
                continue
        except:
            #informs user entry not valid if not an integer:
            print("Not a valid entry. Please enter a whole number.")
        else:
            #counter gets primed to enter next loop:
            counter = 1
    #loop runs until counter and scores are equal values
    while scores > 0 and counter <= scores:
        #primes sentinel value for next loop:
        valid_score = False
        score_in = input("Please enter a score: ")
        #enters loop:
        while not valid_score:
            try:
                #check for integer:
                score_value = int(score_in)
                #check if in range:
                if 0 <= score_value <= 100:
                    #Valid if both conditions met:
                    valid_score = True
                #out of range:
                else:
                    print("Not a valid entry. Value out of range.")
                    #repeats loop that asks for score value
                    break
            #not an integer:
            except:
                print("Not a valid entry. Please enter a number.")
                break
            # if valid:
            else:
                #key name is created:
                score_key = "Score" + str(counter)
                #key and value added to dictionary:
                scores_dict.update({score_key : score_value})
                #valid entries are counted:
                counter += 1
    #returns dictionary when done:
    return scores_dict


def average_scores(a_dict):
    """
    Calculates average of scores submitted in a dictionary container
    :param a_dict: contains keys and values for each test/score
    :return: average of scores entered
    """
    to_average = a_dict.values()
    #selects non-empty dictionaries:
    if len(to_average) > 0:
        #calucates average:
        result = sum(to_average)/len(to_average)
    #for empty dictionaries:
    else:
        result = "Values in dictionary not valid."
    #average returned
    return result
    #calculate ave - use len() to determine num of scores

#calls methods when main starts
if __name__ == '__main__':
    #prints results of the average of the scores received in the get test scores method
    print("The average score is: " + str(average_scores(get_test_scores())))
