'''
This is a bot for an automatic battle resolutor where your imput is the army sizes, and you will see how the battle goes
''' 

import random
import time
import vikingsClasses

def warloop():
    while len(mainwar.vikingArmy) != 0 and len(mainwar.saxonArmy) != 0:
        battle()
        #time.sleep(0.2)
        print(f"there are {len(mainwar.vikingArmy)} vikings left")
        print(f"there are {len(mainwar.saxonArmy)} saxons left")


def battle():
    if random.choice([1,2]) != 1:
        viking = mainwar.vikingAttack()
        if len(mainwar.saxonArmy) > 0:
            saxon = mainwar.saxonAttack()
        print(f"{viking}")
    else:
        saxon = mainwar.saxonAttack()
        if len(mainwar.vikingArmy) > 0:
            viking = mainwar.vikingAttack()
        print(f"{saxon}")

def winner():
    if len(mainwar.vikingArmy) != 0 and len(mainwar.saxonArmy) == 0:
        print(mainwar.vikingArmy[0].battleCry())
        print("Vikings won this round")
    else:
        print("saxons won this round")

print("Welcome to battle resolver")
armySize = None
while armySize == None:
    try:
        armySize = int(input("Set the armys size: "))
    except:
        print("give me an int, no half bodies or letters allowed")
        pass


sodierhealth = 150
sodierstrengh = 30 

print("loading soldiers")

vikingsNames = ["Arne","Birger","Bjørn","Bo","Erik","Frode","Gorm",
"Halfdan","Harald","Knud","Kåre","Leif","Njal","Roar","Rune","Sten",
"Skarde","Sune","Svend","Troels","Toke","Torsten","Trygve","Ulf",
"Ødger","Åge","Astrid","Bodil","Frida","Gertrud","Gro","Estrid",
"Hilda","Gudrun","Gunhild","Helga","Inga","Liv","Randi","Signe",
"Sigrid","Revna","Sif","Tora","Tove","Thyra","Thurid","Yrsa",
"Ulfhild","Åse",]

mainwar = vikingsClasses.War()
for item in range(armySize):
    mainwar.vikingArmy.append(vikingsClasses.Viking(random.choice(vikingsNames), sodierhealth,sodierstrengh))
    mainwar.saxonArmy.append(vikingsClasses.Saxon(sodierhealth,sodierstrengh))

print("Armies are ready to fight lets start")


warloop()
winner()