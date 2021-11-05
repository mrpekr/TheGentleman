from os import replace
import random
from datetime import datetime
from pypresence import Presence
import time

clearConsole = lambda: print('\n' * 150)

#Config:
richpresence = True #Default: True (Shows That you are using "The Gengleman" as you discord activity)
customsalutation = False#COMING SOON | Default: False ("The Gentleman" will be calling you by custom name)

def rpc():
    client_id = "906113842969460746"
    RPC = Presence(client_id=client_id)
    RPC.connect()
    start_time=time.time()
    RPC.update(large_image="logo",large_text="The Gentleman osobně" ,small_image="pfp",small_text="Vytvořil: Mr. Pekr | mrpekr.github.io" ,details = "Používám The Gentleman", state='Je jednoduchý Chatbot' , buttons=[{"label": "Gentlemanovo GitHub Repo", "url": "https://github.com/mrpekr/thegentleman"}, {"label": "Gentlemanovo Tvůrce", "url": "https://mrpekr.github.io"}], start=start_time)

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
    print('Vytvořil: Mr. Pekr | https://mrpekr.github.io ')
    print("\x1b[38;5;255m")
    print("Co pro tebe můžu udělat?")
    print("\x1b[38;5;199m[1] Řekni mi vtip (Bez Překladu)")
    print("[2] Řekni mi mou budoucnost (Bez Překladu)")
    print("[3] Řekni mi kolik je hodin")
    print("[4] Tady Nic Není")
    menu = input("\x1b[38;5;85mZadej Čáslo: ")
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
            print("Tady to máš: \x1b[38;5;158m" + random.choice(jokes))
            print("\x1b[38;5;15m")
            joke = input("Chceš Další Vtip? [Ano / Ne]: ")
            if joke == "Ano":
                clearConsole()
                print(Joke())
            elif joke == "Ne":
                clearConsole()
                print(Menu())
            else:
                clearConsole() 
                print("Neplatná Volba")
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
            future = input("Do You Want To Try Again? [Ano / Ne]: ")

            if future == "Ano":
                clearConsole()
                print(Future())

            if future == "Ne":
                clearConsole()
                print(Menu())
        Future()
    elif menu == "3":
        def Time():
            print("Aktuálně je: " + datetime.now().strftime('%H:%M:%S'))
            back = input("Cheš zpátky do Menu? [Ano / Ne]: ")
            if back == "Ano":
                clearConsole()
                print(Menu())

            if back == "Ne":
                clearConsole()
                print(Time())
        Time()
    elif menu == "4":
        def placeholder():
            print("You Have Selected A Place Holder")
            print("You Stupid")
            back = input("Return To Menu? [Ano / Ne]: ")
            if back == "Ano":
                clearConsole()
                print(Menu())
            elif back == "Ne":
                clearConsole()
                print(placeholder())
            else:
                clearConsole()
                print("Neplatná Volba")
                print(placeholder())
        placeholder()
    else:
        clearConsole()
        print("Neplatná Volba")
        print(Menu())
Menu()