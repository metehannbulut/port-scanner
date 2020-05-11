#!/bin/python3

import sys
import datetime
import socket
import time

starttime = time.time()

if len(sys.argv) == 4:
	target = socket.gethostbyname(sys.argv[1])
	startport = int(sys.argv[2])
	endport = int(sys.argv[3])
	
else:
	print(" Invalid Syntax.")
	print("   Syntax is:\"python3 portscanner.py <ip>/<hostname> <startport> <endport>\"")
	print("   Ex: \"python3 portscanner.py google.com 21 445\"")
	exit()
	
print("-" * 50)
print("Scanning target: {}".format(target))
print("Scanning Ports: [{}, {}]".format(startport, endport))
print("Time started: {}".format(datetime.datetime.now().strftime("%H:%M:%S")))
print("-" * 50)

try:
	for port in range(startport, endport):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.25)
		result = s.connect_ex((target, port))
		if result == 0:
				print("Port {} is open".format(port))
		s.close()
	
except KeyboardInterrupt:
	print("\n")
	print("Stopping the process...")
	
except socket.gaierror:
	print("Host couldn't found.")
	
except socket.error:
	print("Couldn't connect to host")
	
print("Time taken: " + str(int(time.time() - starttime)) + " second(s).")
