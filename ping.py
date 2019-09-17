#!/usr/bin/python3
import socket

hostname=input("Enter Hostname ")
hostname_ip= socket.gethostbyname(hostname)
print(hostname_ip)
