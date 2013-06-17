#!/bin/env python
# Copyright (c) 2013 Spacecow Gaming
"Planetary, the game. Needs no more explanation"
import sys

def mainmenu():
    "Simple main menu function"
    print ("Planetary: A game of sorts")
    print ("(1) Start Game\n(2) Continue Game\n(3) Exit")
    action = int(input("Selection: "))
    if action == 1:
        print ("\n\n\nYour journey into the cosmos is beginning.\n"
                "You think you are high. Is any of this real?\n"
                "The only way to find out is to engage your inner\n" 
                "demons in space combat!\n\n\n")
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
    description = ""
    objects = "Some hydrogen atoms"
    def __init__(self, indesc):
        self.description = indesc
    def getdesc(self):
        "Returns description"
        return self.description
    def getobj(self):
        "Will return a list of things in sector, for now, a string"
        return self.objects
    def setobj(self, newobj):
        "Will modify list of things in sector, for now, takes a string"
        self.objects = newobj
    # Other things will be added here e.g. planets, other players

class Player:
    "The player's spaceship"
    position = (0, 0)
    def __init__(self, inpos):
        self.position = inpos
    def getpos(self):
        "Returns player position tuple"
        return self.position
    def setpos(self, newpos):
        "Sets player position, takes a tuple"
        self.position = newpos

def generateboard():
    "Returns a dictionary of Sectors with their coordinates as the key"
    board = {}
    for xpos in range(11):
        for ypos in range(11):
            board[(xpos, ypos)] = Sector("There are stars here, surprisingly")
    return board

def generatemap(starsys):
    "Will turn the starsystem dictionary into a nice string"
    mapstr = ""
    for xpos in range(11):
        for ypos in range(11):
            mapstr += "*"
        mapstr += "\n"
    return mapstr

    

def start():
    "Starts the game, returns to menu on return"
    starsystem = generateboard()
    player1 = Player((0, 0))
    clear = "\n" * 1000
    output = ""
    bar = "=" * 70
    while True:
        print (clear)
        print (generatemap(starsystem))
        print (output)
        print (bar)
        print ("INFO: You are in sector:\t", 
                player1.position )
        print ("INFO: Sector description:\t", 
                starsystem[player1.position].getdesc())
        print ("INFO: Things in sector:\t\t", 
                starsystem[player1.position].getobj())
        action = input (bar +
                        "\n"
                        "Enter action:")
        if action == "help":
            output =  "HELP: Type help for help.\n"
        else:
            output = "ERROR: Not a valid action.\n"


mainmenu()
