# Copyright (c) 2013 Spacecow Gaming
"Abstract game objects which don't really affect the player"

import matter
from useful import weightedchoice

class Sector:
    "Base unit of board" 
    description = ""
    objects = []

    def __init__(self, indesc, inobj):
        self.description = indesc
        self.objects = inobj

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
                objstr += "\n\t\t\t "
        tmplist = list(objstr)
        tmplist = tmplist[:-5]
        objstr = "".join(tmplist)
        return objstr

    def setobj(self, newobj):
        "Modifies list of things in sector"
        self.objects = newobj
    
    # Used for fear of "object" becoming some other structure later on
    def addobj(self, newobj):
        "Adds object to list"
        self.objects.append(newobj)

class Supersector(Sector):
    "Like a sector and a stripped down Board had a baby"
    submap = {}
    objprobs = {matter.Shop():1, matter.Gas():120}
    def __init__(self, indesc, inobj):
        self.description = indesc
        self.objects = inobj
        for xpos in range(11):
            for ypos in range(11):
                newsect = Sector("Nothing", [])
                newsect.addobj(weightedchoice(self.objprobs))
                self.submap[(xpos, ypos)] = newsect

    def getmap(self):
        return self.submap

class Board:
    "Essentially a container for a data structure of sectors"

    # As of now, the structure de jour is a dictionary
    starsys = {}
    
    # List of objects and their relative probabilities of occurring
    objprobs = { matter.Planet():10, matter.Asteroid():30, matter.Gas():300,
                 matter.PColony():5, matter.AColony():15 }

    def __init__(self):
        for xpos in range(11):
            for ypos in range(11):

                # Iterates through dictionary, using the weighted choice
                # function to pick an object to assign as a value, which 
                # is a list of strings, for the key, which is a tuple
                newsect = Supersector("Nothing of note", [])
                newsect.addobj(weightedchoice(self.objprobs))
                self.starsys[(xpos, ypos)] = newsect

    def getstarsys(self):
        "Returns starsys dictionary"
        return self.starsys

    def getsect(self, coords):
        "Returns sector object"
        return self.starsys[coords]

def generatemap(tomap, size):
    "Turns a starsystem dictionary into a nice string"
    mapstr = ""
    for xpos in range(size):
        for ypos in range(size):
            # Iterates through all sectors in the starsystem, picking an
            # appropriate character to put into the map string
            cursect = tomap[(xpos, ypos)]
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
            elif "Shop" in curobjdescs:
                mapstr += "$"
            else:
                mapstr += "-"
        mapstr += "\n"
    return mapstr
