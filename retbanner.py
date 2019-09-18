#!/usr/bin/python3

import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket()
        sock.connect(ip,port)
        banner = sock.recv(1024)
        return banner
    except:
        return


def main():
    ip = "10.0.0.45"
    for port in range(1,100):
        banner = retBanner(ip,port)
        if banner:
            print("[+]" + ip + ": " + port + ": " + banner)

main()