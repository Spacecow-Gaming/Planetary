# Copyright (c) 2013 Spacecow Gaming
"Abstract game objects which don't really affect the player"

import matter

class Sector:
    "Base unit of board" 
    description = ""
    objects = []

    def __init__(self, indesc, inobj):
        self.description = indesc
        self.objects = inobj
    # This is shown every tick to the user - make it concise, 
    # no more than 1 line
    def getdesc(self):
        "Returns description string"
        return self.description

    def setdesc(self, newdesc):
        "Sets description string"
        self.description = newdesc

    def getobj(self):
        "Returns a list of things in sector"
        return self.objects

    def getobjstr(self, formatted):
        "Turns list into string, then returns"
        objstr = ""

        for obj in self.objects:
            objstr += obj.getshortdesc() 
            if formatted:
                objstr += "\n\t\t\t\t "
        # Since I'm new to Python, there might be a more pythonic
        # way to do str manipulation which I don't know about
        tmplist = list(objstr)
        tmplist = tmplist[:-6]
        objstr = "".join(tmplist)
        return objstr

    def setobj(self, newobj):
        "Modifies list of things in sector"
        self.objects = newobj
    
    # Used for fear of "object" becoming some other structure later on
    def addobj(self, newobj):
        "Adds object to list"
        self.objects.append(newobj)

class Board:
    "Essentially a container for a data structure of sectors"

    # As of now, the structure de jour is a dictionary
    starsys = {}
    
    # Generic objects
    planet, asteroid = matter.Planet(), matter.Asteroid()
    nothing = matter.Gas()

    # Special, rarer ones
    pcolony, acolony = matter.PColony(), matter.AColony()

    # List of objects and their relative probabilities of occurring
    objprobs = { planet:10, asteroid:30, nothing:300,
                 pcolony:5, acolony:15 }

    def __init__(self):
        for xpos in range(11):
            for ypos in range(11):

                # Iterates through dictionary, using the weighted choice
                # function to pick an object to assign as a value, which 
                # is a list of strings, for the key, which is a tuple
                newsect = Sector("Nothing of note", [])
                newsect.addobj(matter.weightedchoice(self.objprobs))
                self.starsys[(xpos, ypos)] = newsect

    def getstarsys(self):
        "Returns starsys dictionary"
        return self.starsys

    def getsect(self, coords):
        "Returns sector object"
        return self.starsys[coords]

def generatemap(starsys):
    "Turns the starsystem dictionary into a nice string"
    mapstr = ""
    for xpos in range(11):
        for ypos in range(11):
            # Iterates through all sectors in the starsystem, picking an
            # appropriate character to put into the map string
            cursect = starsys[(xpos, ypos)]
            curobjdescs = [""]

            # Translates shortdesc to map symbol
            for obj in cursect.getobj():
                curobjdescs.append(obj.getshortdesc())
            if "You are here" in curobjdescs:
                mapstr += "@"
            elif "Planet" in curobjdescs:
                mapstr += "P"
            elif "Planetary Colony" in curobjdescs:
                mapstr += "C"
            elif "Asteroid" in curobjdescs:
                mapstr += "a"
            elif "Asteroid Colony" in curobjdescs:
                mapstr += "c"
            else:
                mapstr += "-"
        mapstr += "\n"
    return mapstr


