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
        print("Yes you had an elevator and you still walked down 20 flights of stairs...Naked...")
        print("As the lift almost reaches the ground floor, you hear noises from the elevator.")
        print("Its probably children.")

        while True:
            action2 = input("What would you like to do?\n[run/stay]\n")
            if action2 in choices2 and action2 == "run":
                print("You run towards the only way you see. Out.")
                print("Theres grass all around.")
                print("You'd think running around naked in grass won't be fun.")
                print("Trust me. You were in for a ride.")
                grass()
                break
            elif action2 in choices2 and action2 == "stay":
                print("You wait there anxiously.")
                print("Still waiting...")
                print("The elevator bell goes 'DINGGGG!'")
                print("The door opens. Its your crush.")
                print("You turn red. No don't worry im just talking about your face.")
                print("Why what did you think lol?")
                print("Anyways, She is with her father and her little brother.")
                print("Her father looks you in the eye. (You know, cause he's a man)")
                print(
                    "Her father lifts you with one hand and throws you into the dirt outside.")
                print(
                    "With the little bit of shame left, you ...cover... and run into the woods.")
                grass()
                break
            else:
                print("Invalid action. Try again.")
                continue
    else:
        print("Invalid action. Try again.")
        continue

print("In the tall grass you find a small piece of cloth.")
print("Its plastic actually.")
print("Maybe one of those plastics they use as roofs in India.")
print("Going with the 'drinking pee in the desert' saying, you decide to use it to cover yourself.")
print("You try it on and notice it can cover only half of your body at a time.")
while True:
    action5 = input(
        "Which part of the body do you wish to cover?\n[upper/lower]\n")
    if action5 == "upper":
        print("You quickly tie it around your chest.")
        trainer.sex()
        print("Nice to know. Okay lets not get out of flow.")
        print("You tie it around your chest. It slides down and hangs on your hips.")
        print("You're way to lazy to bring it back up...")
        print("Its hanging barely by the edges of your hips.")
        print("You feel like a modern-aged recycled body-builder Tarzan.")
        print("Except that you're not a body builder.")
        print("Or a modern person.")
        print("Or a Tarzan.")
        print("But you may be recycled though...like...who knows where that sperm came from bruh?")
        break
    elif action5 == "lower":
        print("You quickly tie it around your chest.")
        sex = input(
            "That brings me to the question. Are you a boy or a girl?\n")
        print("Nice to know. Okay lets not get out of flow.")
        print("You quickly tie the piece of **** around your waste.")
        print("Its hanging barely by the edges of your hips.")
        print("You feel like a modern-aged recycled body-builder Tarzan.")
        print("Except that you're not a body builder.")
        print("Or a modern person.")
        print("Or a Tarzan.")
        print("But you may be recycled though...like...who knows where that sperm came from bruh?")
        break
    else:
        print("Invalid action. Try again.")

print("Now that you are half-clad, with a piece of garbshit, you are ready to RUN.")
print("You patiently wait for the way to be clear.")

while True:
    print("You see no one as far as you can see.")
    print("Which even though is not a lot, but yeah you can still manage to see the Amogh in the far left trapped in a hole.")
    action6 = input(
        "What would you like to do?\n[help amogh/run for my appartment]\n")
    if action6 == "help amogh":
        print("You slowly, quietly tread towards amogh.")
        print("Wild amogh has his head stuck in a hole.")
        print("You dont know what to do.")
        print("Neither does Amogh.")
        print("Which is obvious or he wouldve been out already.")
        print("Wild Amogh notices you.")
        print("Amogh turns silent.")
        print("You send out Rohit.")
        print("Rohit Uses GK!")
        print("With the knowledge of basic physics, Rohit helps Amogh out of the hole.")
        print("Amogh immediately jumps out and asks what is your name?")
        trainer.name()
        print("Amogh: Thank you " + name + ".")
        print("I'd like to join your keyword squad!")
        print("Amogh goes and grabs one of your pokeballs and jumps into it.")
        print("Amogh was caught!")
        mykeywords.append("Amogh")
        print("You take a run towards your appartment now.")
        print("You send out Amogh, behind whom you casually hide while he walks.")
        print("Amogh charmingly waves towards the watchman with you barely following his gigantic ***.")
        print("You improvise. Instead of the elevator, you take stairs.")
        print("After climbing 20 flights of stairs, you realise you dont have keys. Cause youre naked!")
        print("Amogh casually breaks the lock of the door with one hand.")
        print("You hug Amogh.")
        print("You enter the bedroom...With Amogh...")
        print("Dont worry Amogh is in his pokeball.")
        break
    elif action6 == "run to my appartment":
        print("You go for it.")
        print("You spot the watchman is awake from a distance.")
        print("You realise you could use some help.")
        print("You send out Rohit!")
        print("Rohit uses Lipstick on you.")
        print("Now you look like a modern-aged recycled topless woman.")
        print("Except that...")
        print("Nevermind.")
        print("You go run towards the door.")
        print("The Watchman asks for your name.")
        trainer.name()
        print("The watchman, speechless, staring at your bare chest, faints.")
        print("This time, improvisation helps. You dont go for the elevator.")
        print("You climb 20 flights of stairs and make it home.")
        print("Yeah I just realised. You dont have keys.")
        print("You send out Rohit.")
        print("Rohit used GK.")
        print("With the simple art of lockpicking, Rohit Opens the door.")
        print("You hug Rohit.")
        print("You enter the bedroom...With Rohit...")
        print("Dont worry Rohit is in his pokeball.")
        break
    else:
        print("Invalid action. Try again.")
