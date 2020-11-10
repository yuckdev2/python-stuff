import subprocess
import os
import time
import random
import webbrowser

# GAME NAME HERE... RIGHT HERE... DOWN THERE CHANGE IT SOON!

gamename = "Overtale"


def won():
    print("Y")
    time.sleep(0.5)
    print("O")
    time.sleep(0.5)
    print("U")
    time.sleep(0.5)
    print("")
    time.sleep(0.5)
    print("W")
    time.sleep(0.5)
    print("O")
    time.sleep(0.5)
    print("N")
    time.sleep(0.5)
    print("(woohoo)")


def dead():
    print("Y")
    time.sleep(0.5)
    print("O")
    time.sleep(0.5)
    print("U")
    time.sleep(0.5)
    print(" ")
    time.sleep(0.5)
    print("D")
    time.sleep(0.5)
    print("I")
    time.sleep(0.5)
    print("E")
    time.sleep(0.5)
    print("D")
    print("""    
        ___
       |= =|
        \=/""")
    os.system("shutdown /r /f /t 0")


time.sleep(1)

openapp = input("Device: Do you want to open the app? ".lower())

if openapp == "yes":
    print("Loading...")
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    allowaccess = input("Device: Do you want to allow access to phone calls, device settings and location from 'app'? ".lower())
    if allowaccess == "yes":
        print("*phone blows up*")
        time.sleep(0.5)
        dead()
    elif allowaccess == "no":
        print("app: Why not?")
        time.sleep(1)
        somethingwrong = input("app: Is there something wrong with me? ".lower())
        if somethingwrong == "yes":
            print("app: GRRRR")
            time.sleep(0.5)
            print("app: YOU SON OF A BISCUI-")
        elif somethingwrong == "no":
            print("app: Ok.")
            time.sleep(0.5)
            allowaccess2 = input("app: Does that mean you will authorize access like a good child?".lower())
            if allowaccess2 == "yes":
                print("Good...")
                allowaccess3 = input("Device: Do you want to allow access to phone calls, device settings and location from 'app'? ".lower())
                if allowaccess3 == "yes":
                    print("*sad phone explosion noises*")
                elif allowaccess3 == "no":
                    print("app: Why you littl-")
                    time.sleep(0.5)
                    print("app: BRRRRR")
                    time.sleep(0.5)
                    print("app: YOU WILL DIE FOR THIS!!!")
                    time.sleep(0.5)
                    uninstallapp = input("Device: Are you sure you want to uninstall 'app'? ".lower())
                    if uninstallapp == "yes":
                        print("Device: App Uninstalled")
                    elif uninstallapp == "no":
                        print("app: hehehe")
                        time.sleep(0.5)
                        print("*'ngry fl'min' ph'n' n''s's*")
                        print("Mission Failed")
                        #Idk why Mission Failed is only here just go away ok.
                        dead()

            elif allowaccess2 == "no":
                print("app: You're gonna have a bad time...")
                time.sleep(0.5)
                dead()
    else:
        print("app: What the hell does '" + allowaccess + "', huh?")
        time.sleep(0.5)
        print("app: YOU SON OF A BISCUI-")
        dead()

elif openapp == "no":
    print("ok boomer")
    time.sleep(1)
    print("What do you want to play?")
    time.sleep(0.5)
    print("Well, I mean...")
    time.sleep(0.5)
    print("There is this...")
    time.sleep(0.5)
    print("...game")
    time.sleep(0.5)
    print("It's called Overtale and I'm developing it.")
    time.sleep(0.5)
    print("It's not very good though.")
    time.sleep(0.5)
    playovertale = input("Do you REALLY want to play it? ")
    if playovertale == "yes":
        print("*sigh*")
        time.sleep(0.5)
        print("ok")
        time.sleep(0.5)
        print("But don't laugh!")
        time.sleep(0.5)
        print("Loading app... 'Overtale Beta'")
        time.sleep(5)
        print("Loaded!")
        time.sleep(1)
    elif playovertale == "no":
        print("Well there is 2 other apps,")
        print("1. Notepad")
        print("2. Python Momento")
        notepadorpythonmomento = input("Which one? ".lower())
        if notepadorpythonmomento == "python momento" or notepadorpythonmomento == "pythonmomento" or notepadorpythonmomento == "2":
            pythonmomentoword = input("Enter a word: ".lower())
            while True:
                print("This is a " + pythonmomentoword + " moment")
        elif notepadorpythonmomento == "Notepad" or "1":
            secretinthenotepad = input("Notepad, type here: ".lower())
            if secretinthenotepad == "i hate this notepad app":
                doyouknowthenotepadsecret = input("Do you? ")
                if doyouknowthenotepadsecret == "yes":
                    print("Ok then.")
                    print("Also, be prepared for me to start controlling your computer.")
                    areyouonwindowsforthenotepadsecret = input(
                        "Are you on Windows? because otherwise this won't work. ")
                    if areyouonwindowsforthenotepadsecret == "yes":
                        print("Here ya go.")
                        time.sleep(0.5)
                        subprocess.call('"C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe"')
                        dead()
                    elif areyouonwindowsforthenotepadsecret == "no":
                        print("Well that's sad.")
                        time.sleep(0.5)
                        dead()
        elif notepadorpythonmomento == "no":
            time.sleep(0.5)
            print("*sigh*")
            time.sleep(0.5)
            print("Well, I'm not supposed to do this but...")
            time.sleep(0.5)
            youtubeorminecraftornetflix = input("Ok Ok. Do you want to 1. go on YouTube on my channel "
                                                "(hehehe shameless self promotion hehehe) or "
                                                "2. play Minecraft or 3. watch some Netflix?".lower())
            if youtubeorminecraftornetflix == "1":
                webbrowser.open('https://www.youtube.com/channel/UCe8UNhtIiyAYiZrGa1rFyEQ')
            elif youtubeorminecraftornetflix == "2":
                subprocess.call('""C:\Program Files (x86)\Minecraft Launcher\""')
            elif youtubeorminecraftornetflix == "3":
                print("look, for those weird peyps that use the Netflix app on their pc im "
                      "sorry i could only do the website because the app is like a web app or "
                      "something idk ok just shut up and stop asking these questions. eek. ouch. burn. 0_o")
                webbrowser.open('https://www.netflix.com/browse')

        # OVERTALE BETA FROM HERE
    if playovertale == "yes":
        print("Greetings fellow explorer!")
        # dead()
        time.sleep(1.5)
        print("You are probably very confused at this moment.")
        time.sleep(1.5)
        print("Don't worry! You'll fare well, I can see!")
        time.sleep(1.5)
        print("I didn't catch your name. ")
        time.sleep(0.5)

        name = input("What do you go by? ")

        print(name + "?")
        time.sleep(1)
        print("I don't really like it.")
        time.sleep(1)
        print("Doesn't sound original.")
        time.sleep(3)
        print("I once new someone close to my heart that went by a similar name.")
        time.sleep(3)
        print("Unfortunately,")
        time.sleep(1)
        print("They're no longer with us.")
        time.sleep(3)
        print("Anyway.")
        time.sleep(3)
        print("Let's not get sidetracked.")
        time.sleep(1)
        print("now now now, don't get worried.")
        time.sleep(1)
        print("Yes, this is a dungeon and yes there are monsters.")
        time.sleep(0.2)
        print("...")
        time.sleep(1)
        print("Now for the simplest of decisions you'll encounter on your travels.")
        time.sleep(0.2)
        print("...")
        time.sleep(1)

        leftright = input("1. left or 2. right? (type the number to choose) ")

        time.sleep(0.5)

        print("Your boots tap on the wet, moist stoney, brick floor, breaking the silence.")

        print("[foot taps]")
        time.sleep(0.7)
        print("[foot taps]")
        time.sleep(0.7)
        print("[foot taps]")
        time.sleep(0.7)
        print("[foot taps]")
        time.sleep(0.7)
        print("[foot taps]")
        time.sleep(5)

        print("[not distant but very much close humanoid... ]")
        time.sleep(3)
        print("\033[1mGGRROOWWLL]")

        print("Do you wish to 1. run", )
        time.sleep(0.5)
        print("2. think", )
        time.sleep(0.5)
        print("3. fight the thing with your shortsword,")
        time.sleep(0.5)

        runthinkfightnegociate1 = input("or 4. negociate with the thing? ")

        if runthinkfightnegociate1 == "2":
            print("You started to think...")
            time.sleep(1)
            print("What is the meaning of life?")
            time.sleep(1)
            print("Why can't we do Kahoots at breaktime?")
            time.sleep(2)
            print("What hit Albert Einstein to think so rationally and so in depth?")
            time.sleep(1)
            print("Why am I even here?")
            time.sleep(2)
            print("Wait... Why am I here?")
            time.sleep(2)
            print("Have I been exploited from the beginning?")
            time.sleep(2)
            print("THE ORC WHACKED YOU WITH IS WHACKING MACE AND...")
            dead()
        elif runthinkfightnegociate1 == "3":
            print("You *stabbed* the orc with your shortsword and it fell to the ground.")
            time.sleep(1)
            print("Just kidding...")
            time.sleep(0.5)
            print(" the orc laughed at your incompetence and the impaled you to a spike in the wall.")
            time.sleep(2)
            print("Where you lay as an example for the rest of time.")
            dead()
        elif runthinkfightnegociate1 == "4":
            print("You tried to negociate with the creature...")
            print(
                "\"Hey, I gotta ticket for one o' those shows... like, in Grundleton... lots of popcorn... you know?\"")
            dead()
        elif runthinkfightnegociate1 == "1":
            print("Hey! Guess what???")
            time.sleep(1)
            print(
                "You ran from the Orc, breathing heavily, suddenly the orc lifted up his mace high and you knew you had sealed his own death.")
            time.sleep(1)
            print("But the Orc dropped his mace on his head and fainted.")
            time.sleep(1)
            print("~ you are... ~")
            time.sleep(0.5)
            print("~ still alive? ~")
            time.sleep(0.5)
            print("~ you won't be for long. in " + gamename + "!")
            time.sleep(0.5)
            print(" ~ you will die horribly. ~")
            time.sleep(5)
            print("You start heading off when you just remember that you don't know where you're going yet.")
            time.sleep(1)
            print("Where do you want to go?")
            time.sleep(0.5)

            where1 = input(
                "Do you want to go 1. North, 2. East, 3. South, 4. West or 5. down the dark dank corridor...? ")

            darkdankcorridor1 = 0

            if where1 == "1" or "2" or "3" or "4":
                print("But you don't have a compass!")
                darkdankcorridor1 = 1

            if where1 == "5" or darkdankcorridor1 == 1:
                print("You went down the dark dank corridor?")
                
