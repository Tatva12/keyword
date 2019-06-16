import random

# Variables

currentfoe = "Darshan"
currentkeyword = "Rohit"
menuactions = ["use item", "swap keyword", "fight", "run"]
bag = ["Potion", "Super Potion", "Hyper Potion"]
mykeywords = ["Tatva", "Varun", "Rushil", "Rithik", "Darshan"]
run = [99, 34, 56, 83, 12, 25, 8, 6]
foehp = 100
myhp = 100
foehitmultiplier = 1
myhitmultiplier = 1
foedefmultiplier = 1
mydefmultiplier = 1
rapd = 0
gkd = 0
bited = 0
footballd = 0
stard = 0
pjd = 0
bangd = 0
x = 0
steps = 0
totalcoins = 1000
lostcoins = random.randrange(45, 90, 5)
gainedcoins = random.randrange(45, 100, 5)

# Moves


def rap():
    global rapd, currentkeyword, foehp, myhitmultiplier, foehitmultiplier
    rapd = random.randint(11, 25) * myhitmultiplier * foedefmultiplier
    print(currentkeyword + " used Rap")
    print("It did " + str(rapd) + " damage")
    foehp -= int(rapd)


def gk():
    global gkd, currentkeyword, foehp, myhitmultiplier, foedeftmultiplier
    gkd = random.randint(10, 20) * myhitmultiplier * foedefmultiplier
    print(currentkeyword + " used GK")
    print("It did " + str(gkd) + " damage")
    foehp -= gkd


def bite():
    global bited, currentkeyword, myhp, foehitmultiplier, mydefmultiplier
    bited = random.randint(20, 25) * foehitmultiplier * mydefmultiplier
    print(currentfoe + " used Bite")
    print("It did " + str(bited) + " damage")
    myhp -= bited


def football():
    global currentkeyword, currentfoe, footballd, myhp, foedefmultiplier, mydefmultiplier
    footballd = random.randint(30, 40)
    chance = [1]
    print(currentfoe + " used Football!")
    print(currentkeyword + " started playibg football with " + currentfoe)
    if x in chance:
        print(currentkeyword + " fell down and hurt himself ")
        print(currentkeyword + " lost " + str(footballd) + " HP!")
        myhp -= footballd
    else:
        print("Both of them got tired...")
        print(currentfoe + "'s and " + currentkeyword + "'s defense fell")
        if foedefmultiplier <= 0.5:
            print(currentfoe + "'s defense is already low")
        else:
            foedefmultiplier -= 0.1
        if mydefmultiplier <= 0.5:
            print(currentkeyword + "'s defense is already low")
        else:
            mydefmultiplier -= 0.1


def stare():
    global stared, currentkeyword, myhitmultiplier
    print(currentfoe + " used Stare")
    print(currentkeyword + " is feeling awkward")
    if myhitmultiplier <= 0.5:
        print(currentkeyword + "'s hitmultiplier is already low")
    else:
        print(currentkeyword + "'s hitmultiplier fell")
        myhitmultiplier -= 0.1


def pj():
    global pjd, currentkeyword, myhp, bangd
    print(currentfoe + " used PJ.")
    print(currentkeyword + " hates his life.")
    print(currentkeyword + " feels like banging his head on the wall!")
    print(currentkeyword + " learned Bang")
    print(currentkeyword + " Banged his head on the wall")
    print(currentkeyword + " forgot Bang")
    bangd = random.randint(50, 75)
    myhp -= bangd


def lipstick():
    global currentfoe, currentkeyword, foehitmultiplier
    print(currentkeyword + " used Lipstick")
    print(currentfoe + " fell in love with " + currentkeyword)
    if foehitmultiplier <= 0.5:
        print(currentfoe + "'s hitmultiplier is already low")
    else:
        print(currentfoe + "'s hitmultiplier fell harshly")
        foehitmultiplier -= 0.3


def pokemon():
    global currentkeyword, currentfoe, foehitmultiplier, foehp, x
    print(currentkeyword + " used Pokemon")
    print(currentfoe + " started playing Pokemon with " + currentkeyword)
    print(currentfoe + " died in a gym battle in Pokemon.")
    print(currentfoe + " hates his life.")
    print(currentfoe + " feels like jumping off the roof.")

    x = random.randint(1, 10)
    chance = [2, 4]

    if x in chance:
        print(currentfoe + " jumped off the roof. He couldn't take it anymore...")
        foehp = 0
    else:
        print(currentfoe + " decided not today! I'll kill this retard's ***!")
        print(currentfoe + "'s hitmultiplier rose harshly!")
        foehitmultiplier += 0.3


def darshanmove():
    global randmove
    randmove = random.choice(darshanmoveset)
    if randmove == "Bite":
        bite()
    elif randmove == "Football":
        football()
    elif randmove == "Stare":
        stare()
    elif randmove == "PJ":
        pj()


# Movesets
rohitmoveset = ["Rap", "GK", "Lipstick", "Pokemon"]
darshanmoveset = ["Bite", "Football", "Stare", "PJ"]
tatvamoveset = []
varunmoveset = []
rithikmoveset = []
rushilmoveset = []

print("A wild " + currentfoe + " appeared")
print("You sent " + currentkeyword + "!")


while myhp > 0 and foehp > 0:
    steps += 1
    print(currentfoe + "'s HP = " + str(foehp))
    print(currentkeyword + "'s HP = " + str(myhp))

    action1 = input("What would you like to do?\n")
    if action1 == menuactions[0]:  # Use Item
        print("Items in bag")
        print(*bag, sep="\n")
        action2 = input("What do you want to use?\n")

        if action2 in bag and action2 == "Potion":
            myhp += 20
            print(currentkeyword + " gained 20 HP")
            print(currentkeyword + " has " + str(myhp) + "HP now")
            darshanmove()
            continue
        elif action2 in bag and action2 == "Super Potion":
            myhp += 50
            print(currentkeyword + " gained 50 HP")
            print(currentkeyword + " has " + str(myhp) + "HP now")
            continue
        elif action2 in bag and action2 == "Hyper Potion":
            myhp += 100
            print(currentkeyword + " gained 100 HP")
            print(currentkeyword + " has " + str(myhp) + "HP now")
            continue
        else:
            print("invalid action")
            continue
        break
    elif action1 == menuactions[1]:
        print(*mykeywords, sep="\n")
        action2 = input("Which keyword do you choose?\n")  # Swap Keyword
        if action2 == currentkeyword:
            print(currentkeyword + " is already in battle!")
            continue
        elif action2 == mykeywords[0]:
            print("You sent out " + mykeywords[0])
            currentkeyword = mykeywords[0]
            continue
        elif action2 == mykeywords[1]:
            print("You sent out " + mykeywords[1])
            currentkeyword = mykeywords[1]
            continue
        elif action2 == mykeywords[2]:
            print("You sent out " + mykeywords[2])
            currentkeyword = mykeywords[2]
            continue
        elif action2 == mykeywords[3]:
            print("You sent out " + mykeywords[3])
            currentkeyword = mykeywords[3]
            continue
        elif action2 == mykeywords[4]:
            print("You sent out " + mykeywords[4])
            currentkeyword = mykeywords[4]
            continue
    elif action1 == menuactions[2]:
        print(*rohitmoveset, sep="\n")
        action2 = input("Which move do you want to use?\n")  # Fight
        if action2 in rohitmoveset and action2 == "Rap":
            rap()
            darshanmove()
            continue
        elif action2 in rohitmoveset and action2 == "GK":
            gk()
            darshanmove()
            continue
        elif action2 in rohitmoveset and action2 == "Lipstick":
            lipstick()
            darshanmove()
            continue
        elif action2 in rohitmoveset and action2 == "Pokemon":
            pokemon()
            if foehp == 0:
                continue
            else:
                darshanmove()
                continue
            continue
    elif action1 == menuactions[3]:
        x = random.randrange(1, 101)
        if x in run:  # Run
            print("You failed to run away...")
            continue
        else:
            print("You successfully ran away...")
            break
    else:
        print("Invalid action. Try again...")
        continue
if myhp <= 0:
    print(currentkeyword + " fainted")
    if steps <= 3:
        print("You lost badly. Thats embarassing!")
        print("You lost " + str(lostcoins + 20) + " coins")
        totalcoins -= lostcoins - 20
        print("Current coin balance = " + str(totalcoins))
    else:
        print("You lost " + str(lostcoins) + " coins")
        totalcoins -= lostcoins
        print("Current coin balance = " + str(totalcoins))
elif foehp <= 0:
    print(currentfoe + " fainted")
    if steps <= 3:
        print("You embarassed the opponent!")
        print("You gained " + str(gainedcoins + 20) + " coins")
        totalcoins += gainedcoins + 20
        print("Current coin balance = " + str(totalcoins))
    else:
        print("You gained " + str(gainedcoins) + "coins")
        totalcoins += gainedcoins
        print("Current coin balance = " + str(totalcoins))


# Tatva
