import random

# Defining Keywords


class my():
    def myrohit(myrohitlv):
        global currentkeywordhp, currentmoveset, currentkeyword
        currentkeywordhp = 139 + (myrohitlv * 8)
        print("Rohit's HP = " + str(currentkeywordhp))
        currentmoveset = ["Rap", "GK", "Lipstick", "Pokemon"]
        currentkeyword = "Rohit"
        return currentkeywordhp

    def mydarshan(mydarshanlv):
        global currentkeywordhp, currentmoveset, currentkeyword
        currentkeywordhp = 139 + (mydarshanlv * 11)
        print("Darshan's HP = " + str(currentkeywordhp))
        currentmoveset = ["Football", "PJ", "Stare", "Bite"]
        currentkeyword = "Darshan"


class foe():
    def foerohit(foerohitlv):
        global currentfoehp, foemoveset, currentfoe
        currentfoehp = 141 + (foerohitlv * 9)
        print("Foe Rohit's HP = " + str(currentfoehp))
        foemoveset = ["Rap", "GK", "Lipstick", "Pokemon"]
        currentfoe = "Rohit"

    def foedarshan(foedarshanlv):
        global currentfoehp, foemoveset, currentfoe
        currentfoehp = 141 + (foedarshanlv * 12)
        print("Foe Darshan's HP = " + str(currentfoehp))
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
runprob = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]


# Items


class items():
    potions = 2
    superpotions = 1
    hyperpotions = 1

    def potion():
        global currentkeyword, currentkeywordhp, potions
        if potions >= 1:
            print(currentkeyword + " used a Potion. It gained 20 HP!")
            currentkeywordhp += 20
            print(currentkeyword + " has " + str(currentkeywordhp) + "HP now!")
            potions -= 1
        else:
            print("No Potions Left")

    def superpotion():
        global currentkeyword, currentkeywordhp, superpotions
        if superpotions >= 1:
            print(currentkeyword + " used a Super Potion. It gained 50 HP!")
            currentkeywordhp += 50
            print(currentkeyword + " has " + str(currentkeywordhp) + "HP now!")
            superpotions -= 1
        else:
            print("No Super Potions Left")

    def hyperpotion():
        global currentkeyword, currentkeywordhp, hyperpotions
        if hyperpotions >= 1:
            print(currentkeyword + " used a Hyper Potion. It gained 150 HP!")
            currentkeywordhp += 150
            print(currentkeyword + " has " + str(currentkeywordhp) + "HP now!")
            hyperpotions -= 1
        else:
            print("No Hyper Potions Left")

# Experience and levelling up.


rohitexp = 0
darshanexp = 0
expgain = random.randrange(100, 500)

if rohitexp >= 0 and rohitexp <= 500:
    rohitlv = 1
elif rohitexp > 500 and rohitexp <= 1200:
    rohitlv = 2
elif rohitexp > 1200 and rohitexp <= 2500:
    rohitlv = 3
elif rohitexp > 2500 and rohitexp <= 4000:
    rohitlv = 4
elif rohitexp > 4000 and rohitexp <= 7000:
    rohitlv = 5
elif rohitexp > 7000 and rohitexp <= 11000:
    rohitlv = 6
elif rohitexp > 11000 and rohitexp <= 17000:
    rohitlv = 7
elif rohitexp > 17000 and rohitexp <= 25000:
    rohitlv = 8
elif rohitexp > 25000 and rohitexp <= 35000:
    rohitlv = 9
elif rohitexp > 35000 and rohitexp <= 50000:
    rohitlv = 10
elif rohitexp > 50000:
    rohitlv = 10

if darshanexp >= 0 and darshanexp <= 500:
    darshanlv = 1
elif darshanexp > 500 and darshanexp <= 1200:
    darshanlv = 2
elif darshanexp > 1200 and darshanexp <= 2500:
    darshanlv = 3
elif darshanexp > 2500 and darshanexp <= 4000:
    darshanlv = 4
elif darshanexp > 4000 and darshanexp <= 7000:
    darshanlv = 5
elif darshanexp > 7000 and darshanexp <= 11000:
    darshanlv = 6
elif darshanexp > 11000 and darshanexp <= 17000:
    darshanlv = 7
elif darshanexp > 17000 and darshanexp <= 25000:
    darshanlv = 8
elif darshanexp > 25000 and darshanexp <= 35000:
    darshanlv = 9
elif darshanexp > 35000 and darshanexp <= 50000:
    darshanlv = 10
elif darshanexp > 50000:
    darshanlvr = 10

# Defining certain other functions.


def grass():
    f = 1
    while f == 1:
        print("You start walking in grass...")
        x = random.randrange(1, 10)
        if x in wildprob:
            wildbattle()
            f += 1
        else:
            tryagain = input(
                "You see something far away over there in the grass...\n[go/dont go]\n")
            if tryagain == "go":
                continue
            elif tryagain == "dont go":
                break


def wildbattle():
    global rohitexp, darshanexp
    currentfoe = random.choice(keywords)
    print("A wild " + currentfoe + " appeared!")

    if currentfoe == "Darshan":
        foe.foedarshan(1)
    elif currentfoe == "Rohit":
        foe.foerohit(1)
    currentkeyword = "Rohit"
    print("You sent out " + currentkeyword + "!")
    my.myrohit(rohitlv)
    if currentkeywordhp == 0:
        print(currentkeyword + " has no HP.")
        print("You sent out Darshan")
        my.mydarshan(darshanlv)
    while currentkeywordhp > 0 and currentfoehp > 0:
        action3 = input(
            "What would you like to do?\nfight/swap keyword/use item/run\n")

        # USE ITEM
        if action3 == "use item":
            print("Items available in bag are:")
            print(*bag, sep="/")
            action4 = input("Which item do you wish to use?\n")
            if action4 in bag and action4 == "potion":
                items.potion()
            elif action4 in bag and action4 == "super potion":
                items.superpotion()
            elif action4 in bag and action4 == "hyper potion":
                items.hyperpotion()

        # RUN
        elif action3 == "run":
            x = random.randrange(1, 101)
            if x in runprob:
                print("You failed to run away...")
                continue
            else:
                print("You successfully ran away...")
                break

        # SWAP KEYWORD
        elif action3 == "swap keyword":
            print("Keywords available:")
            print(*mykeywords, sep="/")
            action4 = input("Which keyword do you choose?\n")

            if action4 == currentkeyword:
                print(currentkeyword + " is already in battle.")
                continue
            elif action4 == "Rohit":
                print("You sent out Rohit!")
                my.myrohit(rohitlv)
                continue
            elif action4 == "Darshan":
                print("You sent out Darshan!")
                my.mydarshan(darshanlv)
                continue
        # FIGHT
        elif action3 == "fight":
            print(*currentmoveset, sep="/")
            action4 = input("Which move do you wish to use?\n")
            continue

    if currentkeywordhp == 0:
        print("You lost the battle.")

    elif currentfoehp == 0:
        print("You won the battle.")
        print(currentkeyword + " gained " + expgain + " EXP.")
        if currentkeyword == "Rohit":
            rohitexp = rohitexp + expgain
        elif currentkeyword == "Darshan":
            darshanexp = darshanexp + expgain
