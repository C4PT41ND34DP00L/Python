#!/usr/bin/python3
# Version 1
## Show menu ##
import os
import time
import socket

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("\033[0;31;48m .______     ______     ______    __           ______   ______   .______      .______     _______.")
    print("\033[0;31;48m |   _  \   /  __  \   /  __  \  |  |         /      | /  __  \  |   _  \     |   _  \   /       |")
    print("\033[0;31;48m |  |_)  | |  |  |  | |  |  |  | |  |        |  ,----'|  |  |  | |  |_)  |    |  |_)  | |   (----`")
    print("\033[0;31;48m |   ___/  |  |  |  | |  |  |  | |  |        |  |     |  |  |  | |      /     |   ___/   \   \    ")
    print("\033[0;31;48m |  |      |  `--'  | |  `--'  | |  `----.   |  `----.|  `--'  | |  |\  \----.|  |   .----)   |   ")
    print("\033[0;31;48m | _|       \______/   \______/  |_______|    \______| \______/  | _| `._____|| _|   |_______/    ")
    print("")
    print("\033[0;31;48m                             _______  .---.   .---.  ,-.      .---.                              ")
    print("\033[0;31;48m                            |__   __|/ .-. ) / .-. ) | |     ( .-._)                             ")
    print("\033[0;31;48m                              )| |   | | |(_)| | |(_)| |    (_) \                                ")
    print("\033[0;31;48m                             (_) |   | | | | | | | | | |    _  \ \                               ")
    print("\033[0;31;48m                               | |   \ `-' / \ `-' / | `--.( `-'  )                              ")
    print("\033[0;31;48m                               `-'    )---'   )---'  |( __.'`----'                               ")
    print("\033[0;31;48m                                     (_)     (_)     (_)                                         ")
    print("")
    print("\033[0;31;48m                                     BY: C4PT41ND34DP00L")
    print("")
    print (97 * '\033[1;37;48m-')
    print ("\033[1;32;48m1. Get Ip Address from Domain/Host name") #\033[1;32;48m Bright Green   \033
    print ("\033[1;34;48m2. Scan for open port/ports")
    print ("\033[0;31;48m3. TBD")
    print ("\033[0;31;48m99. Exit Application")
    print (97 * '\033[1;37;48m-')
    print ("")

## Get input ###
    choice = input('\033[1;32;48mEnter your choice [1-4] :\033[1;37;48m ')

### Convert string to int type ##
    choice = int(choice)

### Take action as per selected menu-option ###
    if choice == 1:
            print ("Starting backup...")
            main()
    elif choice == 2:
            print ("Starting user management...")
            main()
    elif choice == 3:
            print ("Rebooting the server...")
            main()
    elif choice == 99:
            print("\033[0;31;48m      _______.     ___   ____    ____  ______   .__   __.      ___      .______           ___      ")
            print("    /       |    /   \  \   \  /   / /  __  \  |  \ |  |     /   \     |   _  \         /   \     ")
            print("   |   (----`   /  ^  \  \   \/   / |  |  |  | |   \|  |    /  ^  \    |  |_)  |       /  ^  \    ")
            print("    \   \      /  /_\  \  \_    _/  |  |  |  | |  . `  |   /  /_\  \   |      /       /  /_\  \   ")
            print(".----)   |    /  _____  \   |  |    |  `--'  | |  |\   |  /  _____  \  |  |\  \----. /  _____  \  ")
            print("|_______/    /__/     \__\  |__|     \______/  |__| \__| /__/     \__\ | _| `._____|/__/     \__\ ")
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
    else:    ## default ##
            print ("Invalid number. Try again...")
            main()
main()
