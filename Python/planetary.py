#!/bin/env python
# Copyright (c) 2013 Spacecow Gaming
"Planetary, the game. Needs no more explanation"
import sys
from os import name
from subprocess import call
import ships
import game
import matter
import json

def line(header):
    "Returns nicely formatted header with '=' line"
    output = "="
    output += header
    output += "="*(69-len(header))
    output += "\n"
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
    action = ""
    action = input("\n> ")
    if action == "":
        clear()
    else:
        action = int(action)

    if action == 1:
        clear()
        sys.stdout.write (line("-INFORMATION-") +
                "Your journey into the cosmos is beginning.\n"
                "You think you are high. Is any of this real?\n"
                "The only way to find out is to engage your inner" 
                "demons in space combat!\n" 
                "Press Enter to continue...\n"
                + line("-INPUT PROMPT-"))
        # Short for "prompt", if you were wondering
        input("> ")
        start()
    elif action == 2:
        print ("There is no save game function")
    elif action == 3:
        print ("Exiting game...")
        sys.exit()
    else:
        print ("That is not an option, try again")
    mainmenu()


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
HELP: mine - mines object at current sector
HELP: view inv - views current inventory
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
            player1.setout("")
            output = "Player has moved\n"
        else:
            output = "ERROR: Out of bounds movement index\n"
    elif action[0] == "mine":
        player1.mine(starsys.getsect(player1.getpos()).getobj()[0])
    elif action[0] == "view" and action[1] == "inv":
        player1.viewinv()
    elif action[0] == "scan":
        player1.scan(starsys.getsect(player1.getpos()).getobj()[0])
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
        output = "ERROR: Not a valid action.\n"
    return output

def gethelp(command):
    "Returns help for command"
    helpfile = open("help.json", "r").read()
    helpdict = json.loads(helpfile)
    if command in helpdict:
        helplist = helpdict[command]
        output = "\n".join(helpdict[command])
    else:
        output = "ERROR: Command not found."
    return output


def start():
    "Starts the game"
    starsys = game.Board()
    player1 = ships.Player()
    player1.setshortdesc("You are here")
    player1.setpos((0, 0))
    output = """HELP: Type help for a list of commands
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
                    + game.generatemap(starsys.getstarsys()) 
                    + line("-OUTPUT-")
                    + player1.getout()
                    + output 
                    + line("-INFORMATION-"))
        print ("You are in sector:\t", 
                str(player1.getpos()) )
        print ("Sector description:\t", 
                cursect.getdesc())
        print ("Things in sector:\t", 
                cursect.getobjstr(True))
        rawact = input (line("-INPUT PROMPT-") +
                    "> ")
        if len(rawact) == 0:
            action = ["help"]
        else:
            action = rawact.split()
        output = handleaction(action, gamestate)
        if output == "terminate":
            return False
        prevsect = cursect

mainmenu()
