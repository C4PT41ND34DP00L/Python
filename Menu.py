#!/usr/bin/python3
# Version 1
## Show menu ##
import os
import time
import socket
import subprocess
import sys
from datetime import datetime

os.system('cls' if os.name == 'nt' else 'clear')

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    global IP

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
    #print (97 * '\033[1;37;48m-')
    print (40 * '\033[1;37;48m-' + "Run In Order" + 45 * '-')
    print ("\033[1;33;48m1. Enter Host Name")
    print ("\033[1;32;48m2. Get Ip Address from Domain/Host name")
    print ("\033[1;34;48m3. Scan for open port/ports")
    print ("\033[0;31;48m4. TBD")
    print ("\033[0;31;48m99. Exit Application")
    print (97 * '\033[1;37;48m-')
    print ("")

## Get input ###
    choice = input('\033[1;32;48mEnter your choice [1-4] 99 to Exit :\033[1;37;48m ')

### Convert string to int type ##
    choice = int(choice)

### Take action as per selected menu-option ###
    if choice == 1:
        global hostx
        hostx = input("Enter Host Name ")
        main()
    elif choice == 2:
        hostname=hostx #input("Enter Hostname ")
        hostname_ip= socket.gethostbyname(hostname)
        IP = hostname_ip
        print(hostname_ip)
        main()
    elif choice == 3:

            soc.settimeout(int(input("Enter time out in seconds ")))
            #print(IP)
            host = IP
            port = int(input("Enter port to scan ")) #443


            def portScanner(port):
                if soc.connect_ex((host, port)):
                    print("Port is closed")
                else:
                    print("The port is open")

            portScanner(port)
            main()
    elif choice == 4:
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
