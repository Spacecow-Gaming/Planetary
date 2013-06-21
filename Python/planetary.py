#!/bin/env python
# Copyright (c) 2013 Spacecow Gaming
"Planetary, the game. Needs no more explanation"
import sys
from random import choice
from os import name
from subprocess import call

def line(header):
    "Returns nicely formatted header with '=' line"
    output = "="
    output += header
    output += "="*(69-len(header))
    return output

def clear():
    "Queries OS name to find out how to clear screen, then does it"
    if name == "posix":
        call(["clear"])
    elif name == "nt":
        call(["cls"])
    else:
        # Important debug cat. Don't remove.
        print("You're using an OS I can't be bothered to support.\n"
              "Your screen cannot be cleared. Instead...\n"  
              "Enjoy this cat chasing a mouse\n\n"
              "               )\\._.,--....,'``.      \n"
              " .b--.        /;   _.. \\   _\\  (`._ ,.\n"
              "`=,-,-'~~~   `----(,_..'--(,_..'`-.;.'\n")
def mainmenu():
    "Simple main menu function"
    clear()
    print ("""
  _____   _                      _                      
 |  __ \ | |                    | |                     
 | |__) || |  __ _  _ __    ___ | |_  __ _  _ __  _   _ 
 |  ___/ | | / _` || '_ \  / _ \| __|/ _` || '__|| | | |
 | |     | || (_| || | | ||  __/| |_| (_| || |   | |_| |
 |_|     |_| \__,_||_| |_| \___| \__|\__,_||_|    \__, |
                                                   __/ |
           A game of some sort, I believe         |___/ \n""")
    print ("\t\t(1) Start Game\n\t\t(2) Continue Game\n\t\t(3) Exit")
    action = int(input("\nSELECT: "))
    if action == 1:
        clear()
        print (line("") + "\nINFO: Your journey into the cosmos is beginning.\n"
                "INFO: You think you are high. Is any of this real?\n"
                "INFO: The only way to find out is to engage your inner\n" 
                "INFO: demons in space combat!\n" + line(""))
        # Short for "prompt", if you were wondering
        input("PRMT: Press any key to continue\n")
        start()
    elif action == 2:
        print ("There is no save game function")
    elif action == 3:
        print ("Exiting game...")
        sys.exit()
    else:
        print ("That is not an option, try again")
    mainmenu()

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
        

class Ship(Matter):
    "A spaceship"
    position = (0, 0)
    # Will implement these methods eventually
    def mine(self, target):
        "Mine some matter for resources"

    def attack(self, target):
        "Deal damage to some matter"

    def talk(self, target, mood):
        "Say something in in a mood to a ship/planet"
        # Means you will have options like:
        # 1. Hail ship threateningly
        # 2. Hail ship friendlily
        # Resulting in similar responses and maybe a fight
        # or trading or something

    def scan(self, target):
        "Scan some matter, returning a detailed string"

    def getpos(self):
        return self.position

    def setpos(self, newpos):
        self.position = newpos

class Planet(Matter):
    "Planets have populations, atmospheres etc which matter does not"

class Board:
    "Essentially a container for a data structure of sectors"

    # As of now, the structure de jour is a dictionary
    starsys = {}
    
    # Generic objects
    planet, asteroid, nothing = Planet(), Matter(), Matter()
    planet.setshortdesc("Planet")
    asteroid.setshortdesc("Asteroid")
    nothing.setshortdesc("Gas and dust")

    # Special, rarer ones
    pcolony, acolony, ruins, hulk = Planet(), Matter(), Matter(), Matter()
    pcolony.setshortdesc("Planetary colony")
    acolony.setshortdesc("Asteroid colony")
    ruins.setshortdesc("Abandoned alien colony")
    hulk.setshortdesc("Abandoned ship hulk")

    # List of objects and their relative probabilities of occurring
    objprobs = { planet:10, asteroid:30, nothing:300,
                 pcolony:5, acolony:15, hulk:5,
                 ruins:1}

    def __init__(self):
        for xpos in range(11):
            for ypos in range(11):

                # Iterates through dictionary, using the weighted choice
                # function to pick an object to assign as a value, which 
                # is a list of strings, for the key, which is a tuple
                newsect = Sector("Nothing of note", [])
                newsect.addobj(weightedchoice(self.objprobs))
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
            for obj in cursect.getobj():
                curobjdescs.append(obj.getshortdesc())
            if "You are here" in curobjdescs:
                mapstr += "@"
            elif "Planet" in curobjdescs:
                mapstr += "P"
            elif "Planetary colony" in curobjdescs:
                mapstr += "C"
            elif "Asteroid" in curobjdescs:
                mapstr += "a"
            elif "Asteroid colony" in curobjdescs:
                mapstr += "c"
            elif "Abandoned alien colony" in curobjdescs:
                mapstr += "A"
            elif "Abandoned ship hulk" in curobjdescs:
                mapstr += "s"
            else:
                mapstr += "-"
        mapstr += "\n"
    return mapstr

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

def handleaction(action, gamestate):
    "Takes action list, calls a function and/or returns output"
    # This is a convenience function, could be in the "start" function
    # but is not, because massive functions are not good, hard to debug
    output = ""

    # This processes the context given by the main game
    starsys = gamestate[0]
    player1 = gamestate[1]
    # Checks if help is only arg, returns generic help
    if action[0] == "help" and len(action) == 1:
        output = """\nHELP: help - prints this output
HELP: move x y - moves to sector (x,y)
HELP: mine - coming soon
HELP: scan - coming soon
HELP: build - coming soon
HELP: talk - coming soon
HELP: abandon - abandons current game
HELP: exit - exits program
HELP: help <command> - help on specific command
HELP: help list - a list of help topics\n"""
    # If help is longer, return specific help
    elif action[0] == "help":
        output = gethelp(action[1])
    # Checks if move args are within board bounds, moves player
    elif action[0] == "move" :
        newy = int(action[1])
        newx = int(action[2])
        if newx < 11 and newy < 11:
            player1.setpos((newx, newy))
            output = "\nINFO: Player has moved\n"
        else:
            output = "\nERROR: Out of bounds movement index\n"
    # Causes a return to the main menu
    elif action[0] == "abandon":
        output = "terminate"
    # Exits the entire program abruptly
    elif action[0] == "exit":
        sys.exit()
    # Debug function, just for viewing sectors quickly
    elif action[0] == "print":
        output = ""
        for pos, sect in starsys.getstarsys().items():
            output += str(pos)
            output += str(sect.getobjstr(False))
            output += "\n"
    else:
        output = "\nERROR: Not a valid action.\n"
    return output

def gethelp(command):
    "Returns help for command"
    maph  = """\nHELP: Below, you will find a key for the map
HELP: 'symbol' - what it means
HELP: '-' - Nothing
HELP: '@' - You, the player
HELP: 'a' - Asteroids - mine for resources
HELP: 'c' - An asteroid colony - trade or mine
HELP: 'P' - A planet - Mine, land or build
HELP: 'C' - A planetary colony - Trade, land or mine
HELP: 's' - Another ship - Attack or trade
HELP: 'A' - Abandoned alien colony - Mine for tech
HELP: The map is numbered from top to bottom and left to right
HELP: This means the top left sector is (0,0) and bottom right is (10,10)\n"""

    listh = "\nHELP: List of help topics:\nHELP: map, list\n"
    if command == "map":
        return maph
    elif command == "list":
        return listh
    else:
        return "\nERROR: Command not found in database\n"

def start():
    "Starts the game"
    starsys = Board()
    player1 = Ship()
    player1.setshortdesc("You are here")
    player1.setpos((0, 0))
    output = """\nHELP: Type help for a list of commands
HELP: The "@" on the map represents your position\n"""
    prevsect = starsys.getsect((10, 10))
    
    # This is needed as context for any convenience functions,
    # which would otherwise be lumped in with this function
    gamestate = (starsys, player1)

    while True:
        # cursect is a convenient object, reduces number of calls
        cursect = starsys.getsect(player1.getpos())
        cursect.addobj(player1)

        # Removes the last object from the previous sector - should be the
        # player. This avoids leaving a "P" trail through the system
        prevsect.getobj().pop()
        clear()
        sys.stdout.write(
                    line("-MAP-")
                    + "\n"
                    + generatemap(starsys.getstarsys()) 
                    + line("-OUTPUT-")
                    + output 
                    + line("-INFORMATION-") 
                    + "\n")
        print ("INFO: You are in sector:\t", 
                str(player1.getpos()) )
        print ("INFO: Sector description:\t", 
                cursect.getdesc())
        print ("INFO: Things in sector:\t\t", 
                cursect.getobjstr(True))
        rawact = input (line("-INPUT PROMPT-") +
                    "\n"
                    # This is short for prompt, because 4 letters
                    "PRMT: ")
        if len(rawact) == 0:
            action = ["help"]
        else:
            action = rawact.split()
        output = handleaction(action, gamestate)
        if output == "terminate":
            return False
        prevsect = cursect

mainmenu()
