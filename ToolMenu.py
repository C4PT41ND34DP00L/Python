#!/usr/bin/python3
import os
import time
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
global savePath
savePath = os.path.expanduser("~/Desktop")
def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\033[0;31;48m")
    print(" _   _ _   _ _ _ _           ____       _ _   ")
    print("| | | | |_(_) (_) |_ _   _  | __ )  ___| | |_ ")
    print("| | | | __| | | | __| | | | |  _ \ / _ \ | __|")
    print("| |_| | |_| | | | |_| |_| | | |_) |  __/ | |_ ")
    print(" \___/ \__|_|_|_|\__|\__, | |____/ \___|_|\__|")
    print("                     |___/                    ")
    print("")
    print("              BY: C4PT41ND34DP00L               ")
    print("\033[1;37;48m")
    print(60 * "-")
    print("[1] Choice 1")
    print("[2] Scan Port")
    print("[3] Option 3")
    print("[99] Exit")
    print(60 * "-")
    print("")

    choice = input("Pick an option [1-4] 99 to Exit. ")

    choice = int(choice)

    if choice == 1:
        print("Choice 1")
        main()
    elif choice == 2:
        sock.settimeout(10)

        host = input("[*] Enter Hostname or IP Address to scan: ") #"10.0.0.107"
        port = int(input("[*] Enter Port to scan: "))
        ip = socket.gethostbyname(host)

        def portscanner(port):
            print("")
            print(60 * "-")
            print("     Please wait while we scan the Port on ",ip)
            print(60 * "-")
            if sock.connect_ex((ip,port)):
                print ("Port %d is closed" % (port))
            else:
                print ("Port %d is open" % (port))

        portscanner(port)
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass
        main()
    elif choice == 3:
        print(savePath) #Prints out the path Variabel
        #pauses script until enter is pressed
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass
            #returns to the main menu
        main()
    elif  choice == 99:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[0;31;48mOh, hello there! I bet you’re wondering, why the red suit? Well, that’s so bad guys can’t see me bleed!")
        time.sleep(20)
    else:
        print("Please choose a valid option")
        main()

main()