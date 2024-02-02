import random

class Hero():

    def __init__(self, number, team, lvl):
        self.number = number
        self.team = team
        self.lvl = lvl

    def lvlUp(self, up):
        self.lvl += up

class Soldier():

    def __init__(self, number, team):
        self.number = number
        self.team = team

    def followHero(self, Hero):
        print("Следует за " + Hero + "героем")

Teams = ["Red", "Blue"]

heroRed = Hero(1, "Red", 1)
heroBlue = Hero(2, "Blue", 1)

BlueArmy = []
RedArmy = []

for i in range (10):

    soldier = Soldier(2+i, random.choice(Teams))

    if soldier.team == "Red":
        RedArmy.append("RedSoldier") 
    else:
        BlueArmy.append("BlueSoldier")

if len(RedArmy) > len(BlueArmy):
    heroRed.lvlUp(1)
    print(soldier.followHero("Red "))
else:
    heroBlue.lvlUp(1)
    print(soldier.followHero("Blue "))

print("Уровень синего героя: ", heroBlue.lvl, "\nУровень красного героя: ", heroRed.lvl)
print("Армия красных: ", len(RedArmy), "\nАрмия синих: ", len(BlueArmy))