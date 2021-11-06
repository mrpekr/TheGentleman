from os import replace
import random
from datetime import datetime
from pypresence import Presence
import time
from os.path import exists
import sys
import os

clearConsole = lambda: print('\n' * 150)

#Config:
richpresence = True #Default: True (Shows That you are using "The Gengleman" as you discord activity)
customsalutation = False #Default: False ("The Gentleman" will be calling you by custom name)

def rpc():
    client_id = "906113842969460746"
    RPC = Presence(client_id=client_id)
    RPC.connect()
    start_time=time.time()
    RPC.update(large_image="logo",large_text="The Gentleman it self" ,small_image="pfp" ,small_text="Created By: Mr. Pekr | mrpekr.github.io" ,details = "Im Using The Gentleman", state="He is a small Chatbot" ,buttons=[{"label": "Gentleman's GitHub Repo", "url": "https://github.com/mrpekr/thegentleman"}, {"label": "Gentleman's Creator", "url": "https://mrpekr.github.io"}], start=start_time)

def Menu():  
    if richpresence == True:
        rpc()
    print("\x1b[38;5;220m")    
    print("==============================================================================================")
    print("=        ==  ==================      =======================  ================================")
    print("====  =====  =================   ==   ======================  ================================")
    print("====  =====  =================  ====  =================  ===  ================================")
    print("====  =====  ======   ========  =========   ===  = ===    ==  ===   ===  =  = ====   ===  = ==")
    print("====  =====    ===  =  =======  ========  =  ==     ===  ===  ==  =  ==        ==  =  ==     =")
    print("====  =====  =  ==     =======  ===   ==     ==  =  ===  ===  ==     ==  =  =  =====  ==  =  =")
    print("====  =====  =  ==  ==========  ====  ==  =====  =  ===  ===  ==  =====  =  =  ===    ==  =  =")
    print("====  =====  =  ==  =  =======   ==   ==  =  ==  =  ===  ===  ==  =  ==  =  =  ==  =  ==  =  =")
    print("====  =====  =  ===   =========      ====   ===  =  ===   ==  ===   ===  =  =  ===    ==  =  =")
    print("==============================================================================================")
    print(" ")
    print('Created By: Mr. Pekr | https://mrpekr.github.io ')
    print("\x1b[38;5;255m")
    print("What can i do for You?")
    print("\x1b[38;5;199m[1] Tell me a Joke")
    print("[2] Tell me my Future")
    print("[3] Tell me what time it is")
    print("[4] Tell me why we still here ... Just to suffer")
    menu = input("\x1b[38;5;85mEnter Number: ")
    print("\x1b[38;5;255m")
    if menu == "1":
        def Joke():

            clearConsole()
            jokes = [
                "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
                "Why do we tell actors to “break a leg?” Because every play has a cast.",
                "Heard about the new restaurant called Karma? There’s no menu: You get what you deserve.",
                "Did you hear about the actor who fell through the floorboards? He was just going through a stage.",
                "Did you hear about the claustrophobic astronaut? He just needed a little space.",
                "Why don’t scientists trust atoms? Because they make up everything.",
                "How do you drown a hipster? Throw him in the mainstream.",
                "What did the Buddhist say to the hot dog vendor? Make me one with everything."
            ]
            print("Sure Here: \x1b[38;5;158m" + random.choice(jokes))
            print("\x1b[38;5;15m")
            joke = input("Do You Want Another Joke? [Yes / No]: ")
            if joke == "Yes":
                clearConsole()
                print(Joke())
            elif joke == "No":
                clearConsole()
                print(Menu())
            else:
                clearConsole() 
                print("Invalid Input!")
                Joke()          
        Joke()
    elif menu == "2":
        def Future():
            clearConsole()
            futures = [
                "You Will Be Rich With a lot of Woman/Man on your side with a LOT of money in your wallet",
                "You became Poor and lost everything. How Sad ....",
                "You Died in an Acident ... Sorry i can't see what happend only you in Hospital ... Dieing",
                "You Have Kid and a family you are finnaly happy. (if you already have kid/s turn me off and take care of them)",
                "Sorry ... My powers don't see anything",
                "I took ever your body and took over the world. Haha I was acting ... or Was I?"
            ]
            print("My Powers Tell Me That ...: \x1b[38;5;158m" + random.choice(futures))
            print("\x1b[38;5;15m")
            future = input("Do You Want To Try Again? [Yes / No]: ")

            if future == "Yes":
                clearConsole()
                print(Future())

            if future == "No":
                clearConsole()
                print(Menu())
        Future()
    elif menu == "3":
        def Time():
            print("Current Time Is: " + datetime.now().strftime('%H:%M:%S'))
            back = input("Do You want back to main menu? [Yes / No]: ")
            if back == "Yes":
                clearConsole()
                print(Menu())

            if back == "No":
                clearConsole()
                print(Time())
        Time()
    elif menu == "4":
        def placeholder():
            print("You Have Selected A Place Holder")
            print("You Stupid")
            back = input("Return To Menu? [Yes / No]: ")
            if back == "Yes":
                clearConsole()
                print(Menu())
            elif back == "No":
                clearConsole()
                print(placeholder())
            else:
                clearConsole()
                print("Invalid Input")
                print(placeholder())
        placeholder()
    else:
        clearConsole()
        print("Invalid input!")
        print(Menu())

if customsalutation == False:
    Menu()
else:
    file_exists = exists("data")
    if file_exists == True:
            f = open("data","r")
            lines = f.readline()
            name = lines
            def MenuN():  
                if richpresence == True:
                    rpc()
                print("\x1b[38;5;220m")    
                print("==============================================================================================")
                print("=        ==  ==================      =======================  ================================")
                print("====  =====  =================   ==   ======================  ================================")
                print("====  =====  =================  ====  =================  ===  ================================")
                print("====  =====  ======   ========  =========   ===  = ===    ==  ===   ===  =  = ====   ===  = ==")
                print("====  =====    ===  =  =======  ========  =  ==     ===  ===  ==  =  ==        ==  =  ==     =")
                print("====  =====  =  ==     =======  ===   ==     ==  =  ===  ===  ==     ==  =  =  =====  ==  =  =")
                print("====  =====  =  ==  ==========  ====  ==  =====  =  ===  ===  ==  =====  =  =  ===    ==  =  =")
                print("====  =====  =  ==  =  =======   ==   ==  =  ==  =  ===  ===  ==  =  ==  =  =  ==  =  ==  =  =")
                print("====  =====  =  ===   =========      ====   ===  =  ===   ==  ===   ===  =  =  ===    ==  =  =")
                print("==============================================================================================")
                print(" ")
                print('Created By: Mr. Pekr | https://mrpekr.github.io ')
                print("\x1b[38;5;255m")
                print("What can i do for You " + name + "?")
                print("\x1b[38;5;199m[1] Tell me a Joke")
                print("[2] Tell me my Future")
                print("[3] Tell me what time it is")
                print("[4] Tell me why is there 4 if there is no 4 option")
                menu = input("\x1b[38;5;85mEnter Number: ")
                print("\x1b[38;5;255m")
                if menu == "1":
                    def Joke():

                        clearConsole()
                        jokes = [
                            "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
                            "Why do we tell actors to “break a leg?” Because every play has a cast.",
                            "Heard about the new restaurant called Karma? There’s no menu: You get what you deserve.",
                            "Did you hear about the actor who fell through the floorboards? He was just going through a stage.",
                            "Did you hear about the claustrophobic astronaut? He just needed a little space.",
                            "Why don’t scientists trust atoms? Because they make up everything.",
                            "How do you drown a hipster? Throw him in the mainstream.",
                            "What did the Buddhist say to the hot dog vendor? Make me one with everything."
                        ]
                        print("Sure Here: \x1b[38;5;158m" + random.choice(jokes))
                        print("\x1b[38;5;15m")
                        joke = input("Do You Want Another Joke? [Yes / No]: ")
                        if joke == "Yes":
                            clearConsole()
                            print(Joke())
                        elif joke == "No":
                            clearConsole()
                            print(MenuN())
                        else:
                            clearConsole() 
                            print("Invalid Input!")
                            Joke()          
                    Joke()
                elif menu == "2":
                    def Future():
                        clearConsole()
                        futures = [
                            "You Will Be Rich With a lot of Woman/Man on your side with a LOT of money in your wallet",
                            "You became Poor and lost everything. How Sad ....",
                            "You Died in an Acident ... Sorry i can't see what happend only you in Hospital ... Dieing",
                            "You Have Kid and a family you are finnaly happy. (if you already have kid/s turn me off and take care of them)",
                            "Sorry ... My powers don't see anything",
                            "I took ever your body and took over the world. Haha I was acting ... or Was I?"
                        ]
                        print("My Powers Tell Me That ...: \x1b[38;5;158m" + random.choice(futures))
                        print("\x1b[38;5;15m")
                        future = input("Do You Want To Try Again? [Yes / No]: ")

                        if future == "Yes":
                            clearConsole()
                            print(Future())

                        if future == "No":
                            clearConsole()
                            print(MenuN())
                    Future()
                elif menu == "3":
                    def Time():
                        print("Current Time Is: " + datetime.now().strftime('%H:%M:%S'))
                        back = input("Do You want back to main menu? [Yes / No]: ")
                        if back == "Yes":
                            clearConsole()
                            print(MenuN())

                        if back == "No":
                            clearConsole()
                            print(Time())
                    Time()
                elif menu == "4":
                    def placeholder():
                        print("You Have Selected A Place Holder")
                        print("You Stupid")
                        back = input("Return To Menu? [Yes / No]: ")
                        if back == "Yes":
                            clearConsole()
                            print(MenuN())
                        elif back == "No":
                            clearConsole()
                            print(placeholder())
                        else:
                            clearConsole()
                            print("Invalid Input")
                            print(placeholder())
                    placeholder()
                else:
                    clearConsole()
                    print("Invalid input!")
                    print(MenuN())
            MenuN()
    else:
        print("Hello Im TheGentleman. I don't know you... I'll need your name.")
        time.sleep(5)
        name = input("Please Enter Your Name: ")
        with open("data", "w") as f:
            f.write(name)
            f = open("data","r")
            lines = f.readline()
            names = lines
            print("Name Saved.")
        os.execv(sys.executable, ['python'] + sys.argv)
