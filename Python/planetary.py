#!/bin/env python
# Copyright (c) 2013 Spacecow Gaming
"Planetary, the game. Needs no more explanation"
import sys
import random
from os import name
from subprocess import call

def mainmenu():
    "Simple main menu function"
    print ("Planetary: A game of sorts")
    print ("(1) Start Game\n(2) Continue Game\n(3) Exit")
    action = int(input("Selection: "))
    if action == 1:
        line = "=" * 70
        print (line + "\nINFO: Your journey into the cosmos is beginning.\n"
                "INFO: You think you are high. Is any of this real?\n"
                "INFO: The only way to find out is to engage your inner\n" 
                "INFO: demons in space combat!\n" + line)
        # Short for "prompt", if you were wondering
        input("PRMT: Press any key to continue\n")
        start()
    elif action == 2:
        print ("There is no save game function")
    elif action == 3:
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
        "Returns description"
        return self.description
    def setdesc(self, newdesc):
        description = newdesc
    def getobj(self):
        "Returns a list of things in sector"
        return self.objects
    def getobjstr(self):
        "Turns list into string, then returns"
        objstr = ""
        for obj in self.objects:
            objstr += obj 
            objstr += "\n\t\t"
        return objstr
    def setobj(self, newobj):
        "Modifies list of things in sector"
        self.objects = newobj

class Matter:
    "Catch-all object"
    position = (0,0)
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
    starsys = {}
    def __init__(self):
        for xpos in range(11):
            for ypos in range(11):
                if random.random() < 0.3:
                    self.starsys[(xpos, ypos)] = Sector("Thick asteroid field", ["Asteroids"])
                else:
                    self.starsys[(xpos, ypos)] = Sector("Nothing here", ["Gas and dust"])

    def getstarsys(self):
        return self.starsys
    def getsect(self, coords):
        return self.starsys[coords]

def generatemap(starsys):
    "Will turn the starsystem dictionary into a nice string"
    mapstr = ""
    for xpos in range(11):
        for ypos in range(11):
            cursect = starsys[(xpos, ypos)]
            if "You are here" in cursect.getobj():
                mapstr += "P"
            elif "Planet" in cursect.getobj():
                mapstr += "O"
            elif "Asteroids" in cursect.getobj():
                mapstr += "A"
            else:
                mapstr += "*"
        mapstr += "\n"
    return mapstr

def start():
    "Starts the game, returns to menu on return"
    starsys = Board()
    player1 = Ship((0, 0))
    output = """\nHELP: Type help for a list of commands
HELP: The "P" on the map represents your position\n"""
    line = "=" * 70
    while True:
        cursect = starsys.getsect(player1.getpos())
        cursect.setobj(["You are here"])
        if name == "posix":
            call(["clear"])
        elif name == "nt":
            call(["cls"])
        else:
            print("You're using an OS I can't be bothered to support.\n"
                  "Your screen cannot be cleared. Instead...\n"  
                  "Enjoy this cat chasing a mouse\n\n"
                  "               )\._.,--....,'``.      \n"
                  " .b--.        /;   _.. \   _\  (`._ ,.\n"
                  "`=,-,-'~~~   `----(,_..'--(,_..'`-.;.'\n")
        sys.stdout.write(generatemap(starsys.getstarsys()) 
                + line
                + output 
                + line 
                + "\n")
        print ("INFO: You are in sector:\t", 
                player1.getpos() )
        print ("INFO: Sector description:\t", 
                cursect.getdesc())
        print ("INFO: Things in sector:\t\t", 
                cursect.getobjstr())

        rawact = input (line +
                        "\n"
                        # This is short for prompt, because 4 letters
                        "PRMT: ")
        # This is really, really ugly. I mean /really/. Referring
        # to the shitty indentation
        if rawact == "":
            action = ["help"]
        else:
            action = rawact.split()

        if action[0] == "help":
            output = """\nHELP: help - prints this output
HELP: move x y - moves to sector (x,y)
HELP: mine - mines at current sector
HELP: scan - scans with range 1
HELP: build - coming soon
HELP: abandon - abandons current game
HELP: exit - exits program\n"""
        elif action[0] == "move":
            newx = int(action[1])
            newy = int(action[2])
            player1.setpos((newx, newy))
        elif action[0] == "abandon":
            return False
        elif action[0] == "exit":
            sys.exit()
        elif action[0] == "print":
            output = ""
            for k, val in starsys.getstarsys().items():
                output += str(k)
                output += str(val.getobj())
                output += "\n"

        else:
            output = "\nERROR: Not a valid action.\n"
mainmenu()
