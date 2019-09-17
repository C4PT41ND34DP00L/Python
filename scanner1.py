#!/usr/bin/python3

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.settimeout(10)

host = input("[*] Enter Hostname or IP Address to scan: ") #"10.0.0.107"
port = int(input("[*] Enter Port to scan: "))
ip = socket.gethostbyname(host)

def portscanner(port):
    print(60 * "-")
    print("     Please wait while we scan the Port on ",ip)
    print(60 * "-")
    if sock.connect_ex((ip,port)):
        print ("Port %d is closed" % (port))
    else:
        print ("Port %d is open" % (port))

portscanner(port)