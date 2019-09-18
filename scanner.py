#!/usr/bin/python3

from socket import *
import sys, time
from datetime import datetime

host = ''
max_port = 5000
min_port = 1

def scan_host(host, port, r_code = 1):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		code = s.connect_ex((host, port))
		if code ==0:
			r_code = code
		s.close()
	except:
		pass
	return r_code

try:
	host = input("[*] Enter Target Host Address")
except KeyboardInterrupt:
	print("\n\n[*] User Requested an Interrupt.")
	print("[*] Application Shutting Down.")
	sys.exit(1)

hostip = gethostbyname(host)
print("\n[*] Host: %s IP: %s" % (host, hostip))
print("[*] Scanning Started at %s...\n" % (time.strftime("%H:%M:%s")))
start_time = datetime.now()

for port in range(min_port, max_port):
	try:
		response = scan_host(host, port)

		if response == 0:
			print("[+] Port %d: Open" % (port))
	except:
		pass
stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("\n[*] Scannig Finished at %s ..." % (time.strftime("%H:%M:%s")))
print("[*] Scanning Duration: %s ..." % (total_time_duration))
print("[*] Have a nice day ... Sergeant Exploiter ( Sploit )")
