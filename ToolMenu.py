#!/usr/bin/python3

def main():
    print(" ____             _    ____                     ")
    print("|  _ \ ___   ___ | |  / ___|___  _ __ _ __  ___ ")
    print("| |_) / _ \ / _ \| | | |   / _ \| '__| '_ \/ __|")
    print("|  __/ (_) | (_) | | | |__| (_) | |  | |_) \__ \\")
    print("|_|   \___/ \___/|_|  \____\___/|_|  | .__/|___/")
    print("                                     |_|        ")
    print("            _____           _                   ")
    print("           |_   _|__   ___ | |___               ")
    print("             | |/ _ \ / _ \| / __|              ")
    print("             | | (_) | (_) | \__ \              ")
    print("             |_|\___/ \___/|_|___/              ")
    print(60 * "-")
    print("[1] Option 1")
    print("[2] Option 2")
    print("[3] Option 3")
    print("[99] Exit")

    choice = input("Pick an option ")

    choice = int(choice)

    if choice == 1:
        print("Option 1 chosen")
        main()
    elif choice == 2:
        print("Option 2 chosen")
        main()
    elif choice == 3:
        print("Option 3 chosen")
        main()
    elif  choice == 99:
        print("Good Bye")
    else:
        print("Please choose a valid option")
        main()

main()