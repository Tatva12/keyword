from keywords import *
from main import currentkeyword
# Declaring HPs

if currentkeyword == "Rohit":
    myrohit()
elif currentkeyword == "Darshan":
    mydarshan()

# Default initial items

potions = 2
superpotions = 1
hyperpotions = 1


def potion():
    global currentkeyword, currentkeywordhp, potions
    if potions >= 1:
        print(currentkeyword + " used a Potion. It gained 20 HP!")
        currentkeywordhp += 20
        print(currentkeyword + "has " + str(currentkeywordhp) + " now!")
        potions -= 1
    else:
        print("No Potions Left")


def superpotion():
    global currentkeyword, currentkeywordhp, superpotions
    if superpotions >= 1:
        print(currentkeyword + " used a Super Potion. It gained 50 HP!")
        currentkeywordhp += 50
        print(currentkeyword + "has " + str(currentkeywordhp) + " now!")
        superpotions -= 1
    else:
        print("No Super Potions Left")


def hyperpotion():
    global currentkeyword, currentkeywordhp, hyperpotions
    if hyperpotions >= 1:
        print(currentkeyword + " used a Hyper Potion. It gained 150 HP!")
        currentkeywordhp += 150
        print(currentkeyword + "has " + str(currentkeywordhp) + " now!")
        hyperpotions -= 1
    else:
        print("No Hyper Potions Left")
