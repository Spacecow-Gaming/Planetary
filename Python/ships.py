# Copyright (c) 2013 Spacecow Gaming
"Ship classes, sizes, whatever. But they all inherit from matter"
import matter

class Ship(matter.Matter):
    "A spaceship"
    position = (0, 0)
    output = ""
    # Will implement these methods eventually
    def mine(self, target):
        "Mine some matter for resources"
        self.output = ""
        # The 's' and 't' prefixes mean self and target 
        for tres, tamt in target.getres().items():
            tnewres = {}
            tnewres[tres] = 0
            target.setres(tnewres)
            for sres, samt in self.getres().items():
                snewres = self.getres()
                snewres[sres] += tamt
                self.setres(snewres)
        self.output = "INFO: Mined " 
        self.output += target.getshortdesc().lower()
        self.output += "\nINFO: Inventory now contains:"
        for sres, samt in self.getres().items():
            self.output += "\nINFO: "
            self.output += str(samt) + " tonnes of "
            self.output += str(sres).lower()
            self.output += "\n"
    def attack(self, target):
        "Deal damage to some matter"
        self.output = "\nINFO: Attacked something"

    def viewinv(self):
        "Shows resources on player"
        self.output = "INFO: Inventory contains:"
        for res, amt in self.getres().items():
            self.output += "\nINFO: "
            self.output += str(amt) + " tonnes of "
            self.output += str(res).lower() + "\n"

    def talk(self, target, mood):
        "Say something in in a mood to a ship/planet"
        # Means you will have options like:
        # 1. Hail ship threateningly
        # 2. Hail ship friendlily
        # Resulting in similar responses and maybe a fight
        # or trading or something

    def scan(self, target):
        "Scan some matter, returning a detailed string"
        self.output = "INFO: "+ target.getdesc() + "\n"

    def getout(self):
        "Gets output - only useful for player instances"
        return self.output

    def setout(self, newout):
        "Sets output to be displayed to player"
        self.output = newout

    def getpos(self):
        "Returns pos tuple"
        return self.position

    def setpos(self, newpos):
        "Takes pos tuple"
        self.position = newpos

