#!/usr/bin/python3

import socket
s = socket.socket()
target_host = input("Enter Target Host: ")
target_ip = socket.gethostbyname(target_host)
target_port = input("Enter Traget Port: ")
socket.setdefaulttimeout(20)
try:
    s.connect((target_ip, target_port))

    responce = s.recv(1024)

    print("Service running on " + str(target_port) + ": " + responce)
except:
    print("Unable to connect")
