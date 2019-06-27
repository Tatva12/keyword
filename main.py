# Importing Stuff

import random
from Lists import *
from Items import *


# Asking for general details


trainer = input("What would you like to call your trainer?\n")


# Defining Wild Battle


def wildbattle():
    print(trainer + " sent out Rohit!")
    rohit()
    print(*menuactions, sep="/")
    action1 = input("What would you like to do?\n")

    if action1 == "use item":
        print("Items available in bag are:")
        print(*bag, sep="/")
        action2 = input("Which item do you wish to use?\n")
        if action2 in bag and action2 == "Potion":
            potion()

# Defining Main function


def main():
    print(trainer + " walked into grass in search of wild keywords...")
    x = random.randrange(1, 10)
    wildprob = [1, 3, 4, 7]
    if x in wildprob:
        currentfoe = random.choice(keywords)
        print("A wild " + currentfoe + " appeared")
        wildbattle()
    else:
        print("No keyword appeared...Try again later!")


# Calling Main Function
main()
