currentfoehp = 100

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
