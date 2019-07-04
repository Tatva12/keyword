from lib import *


# Test
print("Test")

# Main program

print("You wake up in your bed.")
print("You start walking.")
print("You look down.")
print("You arent wearing any clothes.")
print("Yes I said ANY clothes.")
print("You keep walking anyway.")
print("You go to your apartment door.")
print("Walk down the flight of stairs.")
print("20 actually. You walk down 20 flights of stairs.")

while True:
    action1 = input(
        "There is grass ahead. What would you like to do?\n[go/dont go]\n")
    if action1 in choices1 and action1 == "go":
        grass()
        break
    elif action1 in choices1 and action1 == "dont go":
        print("You turn around. You press the elevator button.")
        print("Yes you had an elevator and you still walked down 20 flights of stairs naked.")
        print("As the lift almost reaches your floor, you hear noises from the elevator.")
        print("Its probably children.")
        while True:
            action2 = input("What would you like to do?\n[run/stay]\n")
            if action2 in choices2 and action2 == "run":
                print("It worked")
                break
            elif action2 in choices2 and action2 == "stay":
                print("It also worked")
                break
            else:
                print("Invalid action. Try again.")
                continue
    else:
        print("Invalid action. Try again.")
        continue
