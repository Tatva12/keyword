import random

# Defining Keywords


class my():
    def myrohit(myrohitlv):
        global currentkeywordhp, currentmoveset, currentkeyword
        currentkeyword = "Rohit"
        currentkeywordhp = 139 + (myrohitlv * 8)
        currentmoveset = ["Rap", "GK", "Lipstick", "Pokemon"]

    def mydarshan(mydarshanlv):
        global currentkeywordhp, currentmoveset, currentkeyword
        currentkeyword = "Darshan"
        currentkeywordhp = 139 + (mydarshanlv * 11)
        currentmoveset = ["Football", "PJ", "Stare", "Bite"]


class foe():
    def foerohit(foerohitlv):
        global currentfoehp, foemoveset, currentfoe
        currentfoehp = 141 + (foerohitlv * 9)
        foemoveset = ["Rap", "GK", "Lipstick", "Pokemon"]
        currentfoe = "Rohit"

    def foedarshan(foedarshanlv):
        global currentfoehp, foemoveset, currentfoe
        currentfoehp = 141 + (foedarshanlv * 12)
        foemoveset = ["Football", "PJ", "Stare", "Bite"]
        currentfoe = "Darshan"

# Lists


keywords = ["Darshan", "Rohit"]
mykeywords = ["Darshan", "Rohit"]

menuactions = ["use item", "swap keywords", "fight", "run"]
bag = ["potion", "super potion", "hyper potion"]

choices1 = ["go", "dont go"]
choices2 = ["run", "stay"]

fallprob = [1]
wildprob = [1, 2, 5, 6, 9]
runprob = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
suicidechance = [2, 4]

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

# MY MOVES


class myMoves():
    def gk():
        global currentfoehp
        print(currentkeyword + " used his general knowledge")
        gkd = random.randrange(10, 25)
        currentfoehp = currentfoehp - gkd
        print("It did " + str(gkd) + " damage to " + currentfoe + "!")

    def rap():
        print(currentkeyword + " started Rapping.")
        print("Kaun bola? Tujhse na ho paayega?")
        print("...")
        print("Mere jaisa shaana laala tujhko na mil paayega!")
        print("...")
        print("Ab hausle se jeetenge, kaamyaabi cheerenge, sabkuch mila paseene se,")
        print("...")
        print("KUKI APNA TIME AAYEGA!")

        print(currentfoe + " started cheering.")
        print(currentfoe + " has an idol now.")

    def lipstick():
        print(currentkeyword + " applied Lipstick")
        print(currentfoe + " is in love with " + currentkeyword + " now!")

    def pokemon():
        global currentfoehp
        print(currentkeyword + " used Pokemon")
        print(currentfoe + " started playing Pokemon with " + currentkeyword)
        print(currentfoe + " died in a gym battle in Pokemon.")
        print(currentfoe + " hates his life.")
        print(currentfoe + " feels like jumping off the roof.")

        x = random.randint(1, 10)

        if x in suicidechance:
            print(currentfoe + " jumped off the roof. He couldn't take it anymore...")
            currentfoehp = 0
        else:
            print(currentfoe + " decided not today! I'll kick this retard's ***!")
            print(currentfoe + "'s hitmultiplier rose harshly!")

    def bite():
        global currentfoehp
        print(currentkeyword + " bit " + currentfoe)
        print("Wondering where?")
        print("HAHA. Youre lucky for now i havent added that feature to the game yet. Ill add it later.")
        bited = random.randrange(25, 30)
        print("It did " + str(bited) + " damage to " + currentfoe)
        currentfoehp = currentfoehp - bited

    def pj():
        global currentfoehp
        print(currentkeyword + " cracked a pakau joke.")
        print(currentfoe + " hates his life.")
        print(currentfoe + " feels like banging his head on the wall!")
        print(currentfoe + " learned Bang")
        print(currentfoe + " Banged his head on the wall")
        print(currentfoe + " forgot Bang")
        bangd = random.randint(50, 75)
        currentfoehp -= bangd
        print(currentfoe + " lost " + str(bangd) + " HP")

    def football():
        global currentfoehp
        footballd = random.randint(30, 40)
        x = random.randrange(1, 10)
        print(currentkeyword + " used Football!")
        print(currentfoe + " started playing football with " + currentfoe)
        if x in fallprob:
            print(currentfoe + " fell down and hurt himself ")
            print(currentfoe + " lost " + str(footballd) + " HP!")
            currentfoehp = currentfoe - footballd
        else:
            print("Both of them got tired...")
            print(currentfoe + "'s and " + currentkeyword + "'s defense fell")

    def stare():
        print(currentkeyword + " used Stare")
        print(currentfoe + " is feeling awkward")
        print(currentfoe + "'s hitmultiplier fell")

# FOE MOVES


class foeMoves():
    def bite():
        global currentkeywordhp
        print(currentfoe + " bit " + currentkeyword)
        print("Wondering where?")
        print("HAHA. Youre lucky for now i havent added that feature to the game yet. Ill add it later.")
        bited = random.randrange(25, 30)
        print("It did " + str(bited) + " damage to " + currentkeyword)
        currentkeywordhp = currentkeywordhp - bited

    def pj():
        global currentkeywordhp
        print(currentfoe + " cracked a pakau joke.")
        print(currentkeyword + " hates his life.")
        print(currentkeyword + " feels like banging his head on the wall!")
        print(currentkeyword + " learned Bang")
        print(currentkeyword + " Banged his head on the wall")
        print(currentkeyword + " forgot Bang")
        bangd = random.randint(50, 75)
        currentkeywordhp -= bangd
        print(currentkeyword + " lost " + str(bangd) + " HP")

    def football():
        global currentkeywordhp
        footballd = random.randint(30, 40)
        x = random.randrange(1, 10)
        print(currentfoe + " used Football!")
        print(currentkeyword + " started playing football with " + currentfoe)
        if x in fallprob:
            print(currentkeyword + " fell down and hurt himself ")
            print(currentkeyword + " lost " + str(footballd) + " HP!")
            currentkeywordhp = currentkeyword - footballd
        else:
            print("Both of them got tired...")
            print(currentfoe + "'s and " + currentkeyword + "'s defense fell")

    def stare():
        print(currentfoe + " used Stare")
        print(currentkeyword + " is feeling awkward")
        print(currentkeyword + "'s hitmultiplier fell")

    def gk():
        global currentkeywordhp
        print(currentfoe + " used his general knowledge")
        gkd = random.randrange(10, 25)
        currentkeywordhp = currentkeywordhp - gkd
        print("It did " + str(gkd) + " damage to " + currentfoe + "!")

    def rap():
        print(currentfoe + " started Rapping.")
        print("Kaun bola? Tujhse na ho paayega?")
        print("...")
        print("Mere jaisa shaana laala tujhko na mil paayega!")
        print("...")
        print("Ab hausle se jeetenge, kaamyaabi cheerenge, sabkuch mila paseene se,")
        print("...")
        print("KUKI APNA TIME AAYEGA!")

        print(currentkeyword + " started cheering.")
        print(currentkeyword + " has an idol now.")

    def lipstick():
        print(currentfoe + " applied Lipstick")
        print(currentkeyword + " is in love with " + currentfoe + " now!")

    def pokemon():
        global currentkekywordhp
        print(currentfoe + " used Pokemon")
        print(currentkeyword + " started playing Pokemon with " + currentkeyword)
        print(currentkeyword + " died in a gym battle in Pokemon.")
        print(currentkeyword + " hates his life.")
        print(currentkeyword + " feels like jumping off the roof.")

        x = random.randint(1, 10)

        if x in suicidechance:
            print(currentkeyword +
                  " jumped off the roof. He couldn't take it anymore...")
            currentkeywordhp = 0
        else:
            print(currentkeyword + " decided not today! I'll kick this retard's ***!")
            print(currentkeyword + "'s hitmultiplier rose harshly!")

# Defining certain other functions.


def randfoemove():
    randmove = random.choice(foemoveset)
    if randmove == "PJ":
        foeMoves.pj()
    elif randmove == "Football":
        foeMoves.football()
    elif randmove == "Bite":
        foeMoves.bite()
    elif randmove == "Stare":
        foeMoves.stare()
    elif randmove == "GK":
        foeMoves.gk()
    elif randmove == "Rap":
        foeMoves.rap()
    elif randmove == "Lipstick":
        foeMoves.lipstick()
    elif randmove == "Pokemon":
        foeMoves.pokemon()


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
    my.myrohit(rohitlv)
    print("You sent out " + currentkeyword + "!")

    if currentkeywordhp == 0:
        print(currentkeyword + " has no HP.")
        print("You sent out Darshan")
        my.mydarshan(darshanlv)

    while currentkeywordhp > 0 and currentfoehp > 0:
        print(currentkeyword + "'s HP = " + str(currentkeywordhp))
        print(currentfoe + "'s HP = " + str(currentfoehp))

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

            if action4 in currentmoveset and action4 == "Rap":
                myMoves.rap()
                randfoemove()
            elif action4 in currentmoveset and action4 == "GK":
                myMoves.gk()
                randfoemove()
            elif action4 in currentmoveset and action4 == "Lipstick":
                myMoves.lipstick()
                randfoemove()
            elif action4 in currentmoveset and action4 == "Pokemon":
                myMoves.pokemon()
                randfoemove()
            elif action4 in currentmoveset and action4 == "Football":
                myMoves.football()
                randfoemove()
            elif action4 in currentmoveset and action4 == "Bite":
                myMoves.bite()
                randfoemove()
            elif action4 in currentmoveset and action4 == "Stare":
                myMoves.stare()
                randfoemove()
            elif action4 in currentmoveset and action4 == "PJ":
                myMoves.pj()
                randfoemove()
            continue

    if currentkeywordhp == 0:
        print("You lost the battle.")
        print("You gained no EXP .")

    elif currentfoehp == 0:
        print("You won the battle.")
        print(currentkeyword + " gained " + expgain + " EXP.")
        if currentkeyword == "Rohit":
            rohitexp = rohitexp + expgain
        elif currentkeyword == "Darshan":
            darshanexp = darshanexp + expgain
