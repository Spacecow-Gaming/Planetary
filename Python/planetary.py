#!/bin/env python
# Copyright (c) 2013 Spacecow Gaming
import sys

def mainMenu():
    "Prints the main menu"
    print ("Planetary: A game of sorts")
    print ("(1) Start Game\n(2) Continue Game\n(3) Exit")
    action = int(input("Selection: "))
    if action == 1:
        print ("\n\n\nYour journey into the cosmos is beginning. You think you are high.\nIs any of this real? The only way to find out is to engage your inner demons in space combat!\n\n\n")
        start()
    elif action == 2:
        print ("There is no save game function")
    elif action == 3:
        sys.exit()
    else:
        print ("That is not an option, try again")
    mainMenu()

class Sector:
    "Base unit of board" 
    description = "Nothing here."
    # Other things will be added here

class Player:
    "The player's spaceship"
    position = (0,0)
    dead = False

def generateBoard():
    board = {}
    for x in range(11):
        for y in range(11):
            board[(x, y)] = Sector()
    return board

def start():
    starSystem = generateBoard()
    newPlayer = Player()
    while True:
        print ("You are in sector:", newPlayer.position )
        print ("Sector description:", starSystem[newPlayer.position].description)
        action = input ("Enter action:")
        if action == "help":
            print ("\nType help for help.\n")
        else:
            print ("\nNot a valid action.\n")


mainMenu()
