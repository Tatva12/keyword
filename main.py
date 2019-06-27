

# Importing Stuff and setting certain defaults


import random
from Lists import *
from keywords import *

myrohit()

from Items import *

# Asking for general details


trainer = input("What would you like to call your trainer?\n")


# Defining Wild Battle


def wildbattle():
    global currentfoehp, currentkeywordhp, currentfoe, currentkeyword
    currentfoe = random.choice(keywords)
    if currentfoe == "Darshan":
        foedarshan()
    elif currentfoe == "Rohit":
        foerohit()
    print("A wild " + currentfoe + " appeared!")
    print(trainer + " sent out Rohit!")
    while currentkeywordhp > 0 and currentfoehp > 0:
        print(*menuactions, sep="/")
        action1 = input("What would you like to do?\n")

        # If User wants to use an item

        if action1 == "Use Item":

            print("Items available in bag are:")
            print(*bag, sep="/")
            action2 = input("Which item do you wish to use?\n")
            if action2 in bag and action2 == "Potion":
                potion()
            elif action2 in bag and action2 == "Super Potion":
                superpotion()
            elif action2 in bag and action2 == "Hyper Potion":
                hyperpotion()

        # If user wants to run

        elif action1 == "Run":  # Run
            x = random.randrange(1, 101)
            run = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
            if x in run:
                print("You failed to run away...")
                continue
            else:
                print("You successfully ran away...")
                break

        # If user wants to swap keywords

        elif action1 == "Swap Keywords":
            print("Keywords available are: ")
            print(*mykeywords, sep="/")
            action2 = input("Which Keyword do you choose? \n")
            if action2 == currentkeyword:
                print(currentkeyword + " is already in battle!")
                continue
            elif action2 == "Darshan" and action2 in mykeywords:
                print("You withdrew " + currentkeyword + ".")
                print("You sent out Darshan.")
                mydarshan()
                continue

# Defining Main function


def main():
    print(trainer + " walked into grass in search of wild keywords...")
    x = random.randrange(1, 10)
    wildprob = [1, 3, 4, 7]
    if x in wildprob:
        wildbattle()
    else:
        print("No keyword appeared...Try again!")


# Calling Main Function
main()
