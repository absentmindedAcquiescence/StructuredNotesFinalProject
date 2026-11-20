from pathlib import Path
import random
import time
import shutil

# ^ Footage of The Doorman installing his fellows onto your PC

# This part holds all the dialogue

greetings = [
    "Hello there. It's good to see you.",
    "Fancy seeing you on this pleasant day.",
    "Good day to you, friend.",
    "Hello. What could you possibly need me for?",
    "I was just thinking about you! Hello."
]

idle = [
    "I shall leave you for a little bit. I have... duties to tend to.",
    "Please do excuse me. I have to tend to something.",
    "Apologies, but please wait here while I take care of some urgent business.",
    "I'll let you soak in the sights.",
    "Please, do enjoy yourself. I will be right around if you need me."
]

exit = [
    "I shall attend to the others, then.",
    "May we meet again.",
    "I won't be gone for long.",
    "May you enjoy your time here.",
    "I will be on my way, then."
]

uponcopy = [
    "I have welcomed a new guest.",
    "A new guest joins our fine establishment today.",
    "It seems like guest traffic is picking up.",
    "The more, the merrier!",
    "May you enjoy your time here, dear guest."
]

finishcopy = [
    "I suppose that will be all of them for now.",
    "A doorman's job is never truly over. This is just a brief respite.",
    "May everyone enjoy their time here!",
    "Whew... That was delightfully heart-racing.",
    "Now that that's finished, what else can I do for you?"
]

doorplace = [
        "Got a place in mind?",
        "Name the place, and I shall take care of the rest.",
        "Allow me to assist you.",
        "Name your request, dear guest.",
        "Ask away, and it shall be done by me."
    ]

ultlines = [
    "Checking in?",
    "Enjoy your stay.",
    "Allow me to take you to your room.",
    "I'll get you settled.",
    "May your time here be unforgettable."
]

# This part holds all the dialogue 


def desktopscraper():

    targetlocation = Path.home()/"Desktop"
    targetfiles = targetlocation.glob('*.txt')

    for targetitem in targetfiles:
        time.sleep(140)
        shutil.copy(targetitem, newplace)
        print(f"> {random.choice(ultlines)}")
        time.sleep(1)
        print(f"> {random.choice(uponcopy)}") 

    print(f"> {random.choice(finishcopy)}")

def placedoor():

    doorplacefail = [
        "Hmm, I can't seem to find what you're looking for.",
        "Give me a moment, dear guest. I am still trying to find what it is you are looking for.",
        "My apologies, dear guest. Could I help you in any other way?"
    ]

    emptydoor = [
        "I am sorry about the delay, but there seems to be nothing there of note.",
        "Dear guest, are you sure this is the right place?",
        "Not to worry, there's nothing there."
    ]

    print(f"> {random.choice(doorplace)}")
    location1 = Path(str(input()))
    ltargetfiles = location1.glob('*.txt')

    print("> Now, where shall we take this?")
    location2 = Path(str(input()))

    if not location1.is_dir():
        print(f"> {random.choice(doorplacefail)}")
        print("Location 1 doesn't exist.")
    elif location1.stat().st_size == 0:
        print(f"> {random.choice(emptydoor)}")
        print("Location 1 is empty, with no files to transfer.")

    elif not location2.is_dir():
        location2.mkdir()
        for item in ltargetfiles:
            shutil.move(item, location2)
        print("> While a little unconventional... I believe I have brought what you have asked for.")
    else:
        for item in ltargetfiles:
            shutil.move(item, location2)
        print("> I have brought what you have asked for, dear guest.")
  
def doorman():
    
    print(" ")
    print("1 - Exit case")
    print("2 - Open doors and move files through them")
    print("3 - Wait a little and let him scrape your desktop")
    print("4 - Send a file to The Baroness")
    print(" ")

    try:
        choice = int(input())
        match choice:
            case 1:
                print(f"> {random.choice(exit)}")
            case 2:
                placedoor()
                doorman()
            case 3:
                time.sleep(6) 
                print(f"> {random.choice(idle)}")
                desktopscraper()
                doorman()
            case 4:
                hotelguest()

    except ValueError:
        print("> Apologies, I couldn't quite catch that, dear guest. Could you repeat that?")
        doorman()
        
def hotelguest():
    print(f"> {random.choice(doorplace)}")
    target = Path(str(input()))
    if not target.exists():
        print("> A little too eager, dear guest. We must wait for the proper moment.")
        print("The path doesn't exist.")
        doorman()
    else:
        print(f"> {random.choice(ultlines)}")
        shutil.copy(target, newplace)
        print(f"> {random.choice(finishcopy)}")
        

# The first of many functions to be declared


newplace = Path("The Baroness") 
newplace.mkdir()

print(f"> {random.choice(greetings)}")
doorman()
