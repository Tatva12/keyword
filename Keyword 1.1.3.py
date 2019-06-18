import random

# Variables

currentfoe = "Darshan"
currentkeyword = "Rohit"
menuactions = ["use item", "swap keyword", "fight", "run"]
bag = ["Potion 50 coins", "Super Potion - 100 coins", "Hyper Potion - 500 coins"]
mykeywords = ["Tatva", "Varun", "Rushil", "Rithik", "Darshan", "Rohit"]
bag = ["Potion - 50 coins", "Super Potion - 100 coins", "Hyper Potion - 500 coins"]
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
dmgdealer = currentkeyword
dmgreceiver = currentfoe
totalcoins = 1000
lostcoins = random.randrange(45, 90, 5)
gainedcoins = random.randrange(45, 100, 5)

# Moves


def rap():
    global rapd, currentkeyword, foehp, myhp, myhitmultiplier, foehitmultiplier, mydefmultiplier, foedefmultiplier, currentfoe, dmgdealer, dmgreceiver
    if dmgreceiver == currentfoe or dmgdealer == currentkeyword:
        rapd = random.randint(22, 35) * myhitmultiplier * foedefmultiplier
        foehp -= int(rapd)
    elif dmgreceiver == currentkeyword or dmgdealer == currentfoe:
        rapd = random.randint(22, 35) * foehitmultiplier * mydefmultiplier
        myhp -= int(rapd)
    print(dmgdealer + " used Rap")
    print("It did " + str(rapd) + " damage")


def gk():
    global gkd, currentkeyword, currentfoe, foehp, myhp, myhitmultiplier, foedeftmultiplier, foehitmultiplier, mydefmultiplier, dmgdealer, dmgreceiver
    if dmgreceiver == currentfoe or dmgdealer == currentkeyword:
        gkd = random.randint(15, 25) * myhitmultiplier * foedefmultiplier
        foehp -= gkd
    elif dmgreceiver == currentkeyword or dmgdealer == currentfoe:
        gkd = random.randint(15, 25) * mydefmultiplier * foehitmultiplier
        myhp -= gkd
    print(dmgdealer + " used GK")
    print("It did " + str(gkd) + " damage")


def bite():
    global bited, currentkeyword, currentfoe, myhp, foehp, foehitmultiplier, mydefmultiplier, myhitmultiplier, foedefmultiplier, dmgdealer, dmgreceiver
    if dmgreceiver == currentfoe or dmgdealer == currentkeyword:
        bited = random.randint(20, 25) * foehitmultiplier * mydefmultiplier
        myhp -= bited
    elif dmgreceiver == currentkeyword or dmgdealer == currentfoe:
        bited = random.randint(20, 25) * myhitmultiplier * foedefmultiplier
        foehp -= bited
    print(dmgdealer + " used Bite")
    print("It did " + str(bited) + " damage")


def football():
    global currentkeyword, currentfoe, footballd, myhp, foehp, foehitmultiplier, foedefmultiplier, mydefmultiplier, myhitmultiplier, dmgreceiver, dmgdealer
    footballd = random.randint(30, 40)
    chance = [1]
    print(dmgdealer + " used Football!")
    print(dmgreceiver + " started playing football with " + dmgdealer)
    if dmgreceiver == currentkeyword or dmgdealer == currentfoe:
        if x in chance:
            print(dmgreceiver + " fell down and hurt himself ")
            print(dmgreceiver + " lost " + str(footballd) + " HP!")
            myhp -= footballd
        else:
            print("Both of them got tired...")
            print(dmgdealer + "'s and " + dmgreceiver + "'s defense fell")
            if foedefmultiplier <= 0.5:
                print(dmgdealer + "'s defense is already low")
            else:
                foedefmultiplier -= 0.1
            if mydefmultiplier <= 0.5:
                print(dmgreceiver + "'s defense is already low")
            else:
                mydefmultiplier -= 0.1
    elif dmgreceiver == currentfoe or dmgdealer == currentkeyword:
        if x in chance:
            print(dmgreceiver + " fell down and hurt himself ")
            print(dmgreceiver + " lost " + str(footballd) + " HP!")
            foehp -= footballd
        else:
            print("Both of them got tired...")
            print(dmgdealer + "'s and " + dmgreceiver + "'s defense fell")
            if foedefmultiplier <= 0.5:
                print(dmgreceiver + "'s defense is already low")
            else:
                foedefmultiplier -= 0.1
            if mydefmultiplier <= 0.5:
                print(dmgdealer + "'s defense is already low")
            else:
                mydefmultiplier -= 0.1


def stare():
    global stared, currentkeyword, myhitmultiplier
    print(dmgdealer + " used Stare")
    print(dmgreceiver + " is feeling awkward")
    if dmgreceiver == currentkeyword or dmgdealer == currentfoe:
        if myhitmultiplier <= 0.5:
            print(dmgreceiver + "'s hitmultiplier is already low")
        else:
            print(dmgreceiver + "'s hitmultiplier fell")
            myhitmultiplier -= 0.1
    elif dmgreceiver == currentfoe or dmgdealer == currentkeyword:
        if foehitmultiplier <= 0.5:
            print(dmgreceiver + "'s hitmultiplier is already low")
        else:
            print(dmgreceiver + "'s hitmultiplier fell")
            foehitmultiplier -= 0.1


def pj():
    global pjd, myhp, foehp, bangd, mycurrentmoveset, dmgdealer, dmgreceiver, currentkeyword, currentkeyword, dmgreceiver, dmgdealer
    print(dmgdealer + " used PJ.")
    print(dmgreceiver + " hates his life.")
    print(dmgreceiver + " feels like banging his head on the wall!")
    print(dmgreceiver + " learned Bang")
    print(dmgreceiver + " Banged his head on the wall")
    print(dmgreceiver + " forgot Bang")
    bangd = random.randint(50, 75)
    if dmgreceiver == currentfoe:
        foehp -= bangd
        print(dmgreceiver + " lost " + str(bangd) + " HP")
    elif dmgreceiver == currentkeyword:
        myhp -= bangd
        print(dmgreceiver + " lost " + str(bangd) + " HP")


def lipstick():
    global currentfoe, currentkeyword, foehitmultiplier, myhitmultiplier, dmgreceiver, dmgdealer
    print(dmgdealer + " used Lipstick")
    print(dmgreceiver + " fell in love with " + dmgdealer)
    if dmgreceiver == currentfoe:
        if foehitmultiplier <= 0.5:
            print(dmgdealer + "'s hitmultiplier is already low")
        elif foehitmultiplier > 0.5:
            print(currentfoe + "'s hitmultiplier fell harshly")
            foehitmultiplier -= 0.3
    elif dmgreceiver == currentkeyword:
        if myhitmultiplier <= 0.5:
            print(dmgreceiver + "'s hitmultiplier is already low")
        else:
            print(dmgreceiver + "'s hitmultiplier fell harshly")
            myhitmultiplier -= 0.3


def pokemon():
    global currentkeyword, currentfoe, foehitmultiplier, myhitmultiplier, foehp, myhp, x, dmgdealer, dmgreceiver
    print(dmgdealer + " used Pokemon")
    print(dmgreceiver + " started playing Pokemon with " + dmgdealer)
    print(dmgreceiver + " died in a gym battle in Pokemon.")
    print(dmgreceiver + " hates his life.")
    print(dmgreceiver + " feels like jumping off the roof.")

    x = random.randint(1, 10)
    chance = [2, 4]

    if x in chance:
        print(dmgreceiver + " jumped off the roof. He couldn't take it anymore...")
        if dmgreceiver == currentfoe:
            foehp = 0
        elif dmgreceiver == currentkeyword:
            myhp = 0
    else:
        print(dmgreceiver + " decided not today! I'll kick this retard's ***!")
        print(dmgreceiver + "'s hitmultiplier rose harshly!")
        if dmgreceiver == currentfoe:
            foehitmultiplier += 0.3
        elif dmgreceiver == currentkeyword:
            myhitmultiplier += 0.3


def foemove():
    global randmove, foecurrentmoveset, currentfoe, dmgdealer, dmgreceiver
    randmove = random.choice(foecurrentmoveset)
    dmgdealer = currentfoe
    dmgreceiver = currentkeyword
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
tatvamoveset = ["Smile"]
varunmoveset = []
rithikmoveset = []
rushilmoveset = []


print("A wild " + currentfoe + " appeared")
print("You sent " + currentkeyword + "!")
mycurrentmoveset = rohitmoveset
foecurrentmoveset = darshanmoveset

while myhp > 0 and foehp > 0:
    steps += 1
    print(currentfoe + "'s HP = " + str(foehp))
    print(currentkeyword + "'s HP = " + str(myhp))

    action1 = input("What would you like to do?\n")
    if action1 == menuactions[0]:    # Use Item
        print("Items in bag")
        print(*bag, sep="\n")
        action2 = input("What do you want to use?\n")

        if action2 == "Potion":
            if totalcoins >= 50:
                totalcoins -= 50
                myhp += 20
                print(currentkeyword + " gained 20 HP")
                print(currentkeyword + " has " + str(myhp) + "HP now")
                print("You have " + str(totalcoins) + " coins now.")
                foemove()
            else:
                print("Not enough coins!")
            continue
        elif action2 == "Super Potion":
            if totalcoins >= 100:
                totalcoins -= 100
                myhp += 50
                print(currentkeyword + " gained 50 HP")
                print(currentkeyword + " has " + str(myhp) + "HP now")
                print("You have " + str(totalcoins) + " coins now.")
                foemove()
        elif action2 == "Hyper Potion":
            if totalcoins >= 350:
                totalcoins -= 350
                myhp += 100
                print(currentkeyword + " gained 100 HP")
                print(currentkeyword + " has " + str(myhp) + "HP now")
                print("You have " + str(totalcoins) + " coins now.")
                foemove()
            else:
                print("Not enough coins")
            continue
        else:
            print("Invalid action")
            continue
        break
    elif action1 == menuactions[1]:  # Swap Keyword
        print(*mykeywords, sep="\n")
        action2 = input("Which keyword do you choose?\n")
        if action2 == currentkeyword:
            print(currentkeyword + " is already in battle!")
            continue
        elif action2 == mykeywords[0]:
            print("You sent out " + mykeywords[0])
            currentkeyword = mykeywords[0]
            mycurrentmoveset = tatvamoveset
            dmgdealer = currentkeyword
            continue
        elif action2 == mykeywords[1]:
            print("You sent out " + mykeywords[1])
            currentkeyword = mykeywords[1]
            mycurrentmoveset = varunmoveset
            dmgdealer = currentkeyword
            continue
        elif action2 == mykeywords[2]:
            print("You sent out " + mykeywords[2])
            mycurrentmoveset = rushilmoveset
            currentkeyword = mykeywords[2]
            dmgdealer = currentkeyword
            continue
        elif action2 == mykeywords[3]:
            print("You sent out " + mykeywords[3])
            currentkeyword = mykeywords[3]
            mycurrentmoveset = rithikmoveset
            dmgdealer = currentkeyword
            continue
        elif action2 == mykeywords[4]:
            print("You sent out " + mykeywords[4])
            currentkeyword = mykeywords[4]
            mycurrentmoveset = darshanmoveset
            dmgdealer = currentkeyword
            continue
    elif action1 == menuactions[2]:  # Fight
        print(*mycurrentmoveset, sep="\n")
        action2 = input("Which move do you want to use?\n")
        if action2 in mycurrentmoveset and action2 == "Rap":
            dmgdealer = currentkeyword
            rap()
            foemove()
            continue
        elif action2 in mycurrentmoveset and action2 == "GK":
            dmgdealer = currentkeyword
            gk()
            foemove()
            continue
        elif action2 in mycurrentmoveset and action2 == "Lipstick":
            dmgdealer = currentkeyword
            lipstick()
            foemove()
            continue
        elif action2 in mycurrentmoveset and action2 == "Pokemon":
            dmgdealer = currentkeyword
            pokemon()
            if foehp == 0:
                continue
            foemove()
            continue
        else:
            foemove()
            continue
        continue
    elif action1 == menuactions[3]:  # Run
        x = random.randrange(1, 101)
        if x in run:
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
