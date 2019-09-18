#!/usr/bin/python3

import socket


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.settimeout(25)

host = input("[*] Enter Hostname or IP Address to scan: ") #"10.0.0.107"
#port = int(input("[*] Enter Port to scan: "))
ip = socket.gethostbyname(host)

print(60 * "-")
print("     Please wait while we scan ports on",ip)
print(60 * "-")

def portscanner(port):
    if sock.connect_ex((ip,port)):
        print("\033[0;31;48m[!!] Port %d is closed" % (port))
    else:
        print ("\033[1;32;48m[+] Port %d is open" % (port))

for port in range(1,500):
    portscanner(port)