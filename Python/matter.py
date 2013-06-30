# Copyright (c) 2013 Spacecow Gaming
"Types of matter, things made of matter etc"

from random import choice

# As good a place as any to put this
def weightedchoice(choiceprobs):
    "Takes a dictionary of choices and probabilities, returns a choice"
    # This list comprehension takes a dictionary of choice keys and
    # probability values and generates a list where each choice
    # occurs a number of times equal to the probability value. This is
    # because the values supplied are relative to each other i.e.
    # don't add up to 1. What the values add up to doesn't matter, as 
    # long as they are integral.
    weightedlist = [x for choice, prob in choiceprobs.items() 
                    for x in [choice]*prob ]
    return choice(weightedlist)


class Matter:
    "Everything on the map is matter"

    # What is returned when scanned
    description = "It's made of rocks"

    shortdesc = "Asteroid"

    # Resources you get when you mine it, in tons
    resources = {"Rocks":10}

    def getdesc(self):
        "Returns string"
        return self.description

    def setdesc(self, newdesc):
        "Takes string"
        self.description = newdesc

    def getshortdesc(self):
        "Returns nonspecific description"
        return self.shortdesc

    def setshortdesc(self, newdesc):
        "Sets nonspecifc description"
        self.shortdesc = newdesc

    def getres(self):
        "Returns dict"
        return self.resources

    def setres(self, newres):
        "Takes dict"
        self.resources = newres

class Planet(Matter):
    "Planets have populations, atmospheres etc which matter does not"
    # Will implement later. Things to do:
    # 1. Traders units and their inventories
    # 2. Planet subsectors, for landing and exploring


