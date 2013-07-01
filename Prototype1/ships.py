# Copyright (c) 2013 Spacecow Gaming
"Ship classes, sizes, whatever. But they all inherit from matter"
import matter

class Ship(matter.Matter):
    "A spaceship"
    position = (0, 0)
    shortdesc = "Ship"
    # Will implement these methods eventually
    def attack(self, target):
        "Deal damage to some matter"

    def talk(self, target, mood):
        "Say something in in a mood to a ship/planet"
        # Means you will have options like:
        # 1. Hail ship threateningly
        # 2. Hail ship friendlily
        # Resulting in similar responses and maybe a fight
        # or trading or something

    def getpos(self):
        "Returns pos tuple"
        return self.position

    def setpos(self, newpos):
        "Takes pos tuple"
        self.position = newpos

class Player(Ship):
    "Ship, but with text output and status functions"
    output = ""
    shortdesc = "Player"

    def scan(self, target):
        "Scan some matter, returning a detailed string"
        self.output = ""+ target.getdesc() + "\n"
        for res, amt in target.getres().items():
            self.output += str(amt) + " tonnes of "
            self.output += str(res).lower() + "\n"


    def viewinv(self):
        "Shows resources on player"
        self.output = "Inventory contains:\n"
        for res, amt in self.getres().items():
            self.output += str(amt) + " tonnes of "
            self.output += str(res).lower() + "\n"

    def getout(self):
        "Gets output - only useful for player instances"
        return self.output

    def setout(self, newout):
        "Sets output to be displayed to player"
        self.output = newout

    def mine(self, target):
        "Mine some matter for resources"
        self.output = ""
        # The 's' and 't' prefixes mean self and target 
        snewres = self.getres()
        tnewres = target.getres()
        for tres, tamt in target.getres().items():
            for sres, samt in self.getres().items():
                if sres == tres:
                    snewres[sres] += tamt
        target.setres(tnewres)
        self.output = "Mined " 
        self.output += target.getshortdesc().lower()

    def attack(self, target):
        "Deal damage to some matter"
        self.output = "Attacked" + target.getshortdesc().lower()



