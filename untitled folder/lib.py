import random

# Defining MY Keywords


def myrohit(myrohitlv):
    global currentkeywordhp, currentmoveset, currentkeyword
    currentkeywordhp = 139 + (myrohitlv * 7)
    currentmoveset = ["Rap", "GK", "Lipstick", "Pokemon"]
    currentkeyword = "Rohit"
    return currentkeywordhp


def mydarshan(mydarshanlv):
    global currentkeywordhp, currentmoveset, currentkeyword
    currentkeywordhp = 130 + (mydarshanlv * 7)
    currentmoveset = ["Football", "PJ", "Stare", "Bite"]
    currentkeyword = "Darshan"

# Defining FOE Keywords


def foerohit(foerohitlv):
    global currentfoehp, foemoveset, currentfoe
    currentfoehp = 141 + (foerohitlv * 8)
    foemoveset = ["Rap", "GK", "Lipstick", "Pokemon"]
    currentfoe = "Rohit"


def foedarshan(foedarshanlv):
    global currentfoehp, foemoveset, currentfoe
    currentfoehp = 183 + (foedarshanlv * 8)
    foemoveset = ["Football", "PJ", "Stare", "Bite"]
    currentfoe = "Darshan"

# Lists


keywords = ["Darshan", "Rohit"]
mykeywords = ["Darshan", "Rohit"]

menuactions = ["use item", "swap keywords", "fight", "run"]
bag = ["potion", "super potion", "hyper potion"]

choices1 = ["go", "dont go"]
choices2 = ["run", "stay"]

wildprob = [1, 2, 5, 6, 9]

# Items

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

# Defining certain other functions.


def grass():
    f = 1
    while f == 1:
        print("You walk in grass...")
        x = random.randrange(1, 10)
        if x in wildprob:
            wildbattle()
            f += 1
        else:
            tryagain = input(
                "No keyword appeared...Type 1 to try again and 2 to give up...\n")
            if tryagain == "1":
                continue
            elif tryagain == "2":
                break


def wildbattle():
    currentfoe = random.choice(keywords)
    print("A wild " + currentfoe + " appeared!")

    if currentfoe == "Darshan":
        foedarshan(1)
    elif currentfoe == "Rohit":
        foerohit(2)

    myrohit(1)
    print("You sent out " + currentkeyword + "!")
    while currentkeywordhp > 0 and currentfoehp > 0:
        action3 = input(
            "What would you like to do?\nfight/swap keyword/use item/run\n")

        if action3 == "use item":
            print("Items available in bag are:")
            print(*bag, sep="/")
            action4 = input("Which item do you wish to use?\n")
            if action4 in bag and action4 == "potion":
                potion()
            elif action4 in bag and action4 == "super potion":
                superpotion()
            elif action4 in bag and action4 == "hyper potion":
                hyperpotion()

        elif action3 == "run":
            x = random.randrange(1, 101)
            run = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
            if x in run:
                print("You failed to run away...")
                continue
            else:
                print("You successfully ran away...")
                break
