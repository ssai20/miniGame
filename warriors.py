import random
import math
    
class Warrior:
    health = 100
    power = 20
    name = "noname"
    def hitToOtherWarrior(self, w):
        if self.health > 0:
            w.health -= self.power
        print("Unit " + str(self.name) + " to attack and unit " + str(w.name) + " has " + str(w.health) + " health")
        #print (w.health)

class Doctor:
    redCross = 10
    name = "noname"
    health = 100
    def toHealWarrior(self, w):
        if w.health < 100 and self.health > 0:
            w.health += self.redCross
        print("Unit " + str(self.name) + " to heal and unit " + str(w.name) + " has " + str(w.health) + " health")

class Magic:
    mana = 15
    health = 100
    name = "noname"
    def toActivatePowerWarrior(self, w):
        if self.health > 0:
            w.power += self.mana
        print("Unit " + str(self.name) + " to activate power and unit " + str(w.name) + " has " + str(w.power) + " power")

class Archer:
    power = 100
    name = "noname"
    def toKillDoctor(self, d):
        d.health -= self.power
        print("Unit " + str(self.name) + " to kill unit " + str(d.name) )
    def toKillMagic(self, d):
        m.health -= self.power
        print("Unit " + str(self.name) + " to kill unit " + str(m.name) )





a1 = Archer()
m1 = Magic()
m1.name = "Shpinat"
d1 = Doctor()
d2 = Doctor()
d1.name = "Merlin"
d2.name = "Sauron"
w1 = Warrior()
w1.name = "Mike"
w2 = Warrior()
w2.name = "Jhon"

m1.toActivatePowerWarrior(w2)

#turn = math.ceil(random.randint(0,1))
while w1.health>0 and w2.health > 0:
    WarTurn = math.ceil(random.randint(0,1))
    HospitalTurn = math.ceil(random.randint(0,1))
    if WarTurn == 1 and HospitalTurn == 1:
        w1.hitToOtherWarrior(w2)
        d1.toHealWarrior(w2)
    if WarTurn == 1 and HospitalTurn == 0:
        w1.hitToOtherWarrior(w2)
        d2.toHealWarrior(w1)
    if WarTurn == 0 and HospitalTurn == 1:
        w2.hitToOtherWarrior(w1)
        d1.toHealWarrior(w2)
    if WarTurn == 0 and HospitalTurn == 0:
        w2.hitToOtherWarrior(w1)
        d2.toHealWarrior(w1)
    if w1.health == 0:
        print(w1.name + " loose and " + str(w2.name) + " win!")
    elif w2.health == 0:
        print(w2.name + " loose and " + str(w1.name) + " win!")    
    
a1.toKillDoctor(d2)    

#w1.hitToOtherWarrior(w2)
