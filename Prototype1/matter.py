# Copyright (c) 2013 Spacecow Gaming
"Types of matter, things made of matter etc"

from useful import weightedchoice
import json

class Matter:
    "Everything on the map is matter"

    # What is returned when scanned
    description = "It's very generic"
    shortdesc = "Matter"

    # Resources you get when you mine it, in tons
    resources = {}

    def __init__(self):
        "Reads and sets properties from JSON file"

        # Reads file
        matterfile = open("matter.json", "r").read()

        # Turns into dict with JSON, finds appropriate part for the type
        # of object this matter is
        dictfull = json.loads(matterfile)[self.shortdesc]

        # Sets description from weighted list in JSON file
        descdict = dictfull["Description"]
        self.setdesc(weightedchoice(descdict))

        # Sets resource counts from JSON file
        resdict = dictfull["Resources"]
        self.setres(eval(weightedchoice(resdict)))

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

# Top-level matter objects i.e. in space

class Gas(Matter):
    "Has effects on ships, sometimes"
    shortdesc = "Gas and dust"

class Planet(Matter):
    "Planets have atmospheres, subsectors etc which matter does not"
    shortdesc = "Planet"


class PColony(Planet):
    "Colonies have populations, shops etc"    
    shortdesc = "Planetary Colony"

class Asteroid(Matter):
    "Asteroids do not have vegetation and are smaller"
    shortdesc = "Asteroid"

class AColony(Asteroid):
    "People, shops, but also hull integrity and other ship-like things"
    shortdesc = "Asteroid Colony"

# Second level objects i.e. on the ground

class Shop(Matter):
    "Buy stuff here"
    shortdesc = "Shop"
