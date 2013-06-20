#!/bin/env python
# Copyright (c) 2013 Spacecow Gaming
"Planetary, the game. Needs no more explanation"
import sys
from random import choice
from os import name
from subprocess import call

def line(header):
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
    print ("Planetary: A game of sorts")
    print ("(1) Start Game\n(2) Continue Game\n(3) Exit")
    action = int(input("SELECT: "))
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
    # The description doesn't actually do anything, hence
    # it being a string, not something nicer
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

    def getobjstr(self):
        "Turns list into string, then returns"
        objstr = ""
        for obj in self.objects:
            objstr += obj 
            objstr += "\n\t\t\t\t "
        # Since I'm new to Python, there might be a more pythonic
        # way to do this which I don't know about
        tmplist = list(objstr)
        tmplist = tmplist[:-6]
        objstr = "".join(tmplist)
        return objstr

    def setobj(self, newobj):
        "Modifies list of things in sector"
        self.objects = newobj

    def addobj(self, newobj):
        "Adds object to list"
        self.objects.append(newobj)

class Matter:
    "Catch-all object"
    position = (0, 0)

    def __init__(self, inpos):
        self.position = inpos

    def getpos(self):
        "Returns position tuple"
        return self.position

    def setpos(self, newpos):
        "Sets position, takes a tuple"
        self.position = newpos

class Ship(Matter):
    "A spaceship"
    # Ship specific methods will come eventually...

class Board:
    "Essentially a container for a data structure of sectors"

    # As of now, the structure de jour is a dictionary
    starsys = {}

    # List of objects and their relative probabilities of occurring
    objprobs = { "Planet":1, "Asteroids":10, "Gas and dust":30 }

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
            if "You are here" in cursect.getobj():
                mapstr += "P"
            elif "Planet" in cursect.getobj():
                mapstr += "O"
            elif "Asteroids" in cursect.getobj():
                mapstr += "A"
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
    "Takes action list, calls a function or returns output"
    output = ""
    starsys = gamestate[0]
    player1 = gamestate[1]
    if action[0] == "help" and len(action) == 1:
        output = """\nHELP: help - prints this output
HELP: move x y - moves to sector (x,y)
HELP: mine - mines at current sector
HELP: scan - scans with range 1
HELP: build - coming soon
HELP: abandon - abandons current game
HELP: exit - exits program
HELP: help <command> - help on specific command
HELP: help list - a list of help topics\n"""
    elif action[0] == "help":
        output = gethelp(action[1])
    elif action[0] == "move" :
        newy = int(action[1])
        newx = int(action[2])
        if newx < 11 and newy < 11:
            player1.setpos((newx, newy))
            output = "\nINFO: Player has moved\n"
        else:
            output = "\nERROR: Out of bounds movement index\n"
    elif action[0] == "abandon":
        output = "terminate"
    elif action[0] == "exit":
        sys.exit()
    elif action[0] == "print":
        output = ""
        for key, val in starsys.getstarsys().items():
            output += str(key)
            output += str(val.getobj())
            output += "\n"
    else:
        output = "\nERROR: Not a valid action.\n"
    return output

def gethelp(command):
    "Returns help for command"
    maph  = """\nHELP: Below, you will find a key for the map
HELP: 'symbol' - what it means
HELP: '-' - Nothing
HELP: 'P' - You, the player
HELP: 'A' - Asteroids
HELP: 'O' - A planet
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
    "Starts the game, returns to menu on return"
    starsys = Board()
    player1 = Ship((0, 0))
    output = """\nHELP: Type help for a list of commands
HELP: The "P" on the map represents your position\n"""
    prevsect = starsys.getsect((10, 10))
    
    # This is needed as context for any convenience functions,
    # which would otherwise be lumped in with this one
    gamestate = (starsys, player1)

    while True:
        cursect = starsys.getsect(player1.getpos())
        cursect.addobj("You are here")
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
                player1.getpos() )
        print ("INFO: Sector description:\t", 
                cursect.getdesc())
        print ("INFO: Things in sector:\t\t", 
                cursect.getobjstr())
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
