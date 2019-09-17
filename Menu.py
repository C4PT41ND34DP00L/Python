#!/usr/bin/python3
# Version 1
## Show menu ##
def main():
    print (10 * '-' + "C4PT41ND34DP00L's Tools" + 10 * '-')
    print ("1. Backup")
    print ("2. User management")
    print ("3. Reboot the server")
    print ("4. Exit")
    print (43 * '-')

## Get input ###
    choice = input('Enter your choice [1-4] : ')

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
    elif choice == 4:
            print("sayonara, Robocop")
    else:    ## default ##
            print ("Invalid number. Try again...")
main()