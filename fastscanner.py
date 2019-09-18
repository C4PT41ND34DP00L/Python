#!/usr/bin/env python3
import socket, threading
from datetime import datetime

def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''



def scan_ports(host_ip, delay):

    threads = []        # To run TCP_connect concurrently
    output = {}         # For printing purposes

    # Spawning threads to scan ports
    for i in range(10000):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(10000):
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(10000):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(10000):
        if output[i] == 'Listening':
            print('\033[1;32;48m' + str(i) + ': ' + output[i])




def main():
    host_ip = input("Enter host IP: ")
    delay = int(input("How many seconds the socket is going to wait until timeout: "))
    remoteServerIP  = socket.gethostbyname(host_ip)
    t1 = datetime.now()
    print("")
    print ("-" * 80)
    print ("\033[1;37;48mPlease wait, scanning remote host\033[0;36;48m", remoteServerIP, "\033[1;37;48mat, ", t1)
    print ("-" * 80)
    print("")
    scan_ports(host_ip, delay)
    t2 = datetime.now()

    total =  t2 - t1

# Printing the information to screen
    print ('\033[1;37;48mScanning Completed in: ', total)
if __name__ == "__main__":
    main()