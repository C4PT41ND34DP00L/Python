#!/usr/bin/python3

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.settimeout(int(input("Enter time out in seconds ")))

host = input("Enter IP Address to scan ") #137.74.187.100
port = int(input("Enter port to scan ")) #443


def portScanner(port):
    if socket.connect_ex((host, port)):
        print("Port is closed")
    else:
        print("The port is open")

portScanner(port)