"Some utility functions"
from random import choice

def weightedchoice(choiceprobs):
    "Takes a dictionary of choices and probabilities, returns a choice"
    weightedlist = [x for choice, prob in choiceprobs.items() 
                    for x in [choice]*prob ]
    return choice(weightedlist)
