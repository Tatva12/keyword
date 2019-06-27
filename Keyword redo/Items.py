from keywords import rohit, darshan
from main import currentkeyword, currentkeywordhp

# Default initial items

potions = 2
superpotions = 1
hyperpotions = 1


def potion():
    global currentkeyword, currentkeywordhp, potions
    if potions >= 1:
        print(currentkeyword + " used a Potion. It gained 50 HP!")
        currentkeywordhp += 50
        potions -= 1
    else:
        print("No Potions Left")
