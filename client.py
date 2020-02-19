from socket import *

def talk():
	strg = input('Voce: ')
	strg = strg.encode()
	#msg = [strg]
	print(strg)
	return strg

serverHost = ''
serverPort = 16384


socOb = socket(AF_INET, SOCK_STREAM)
socOb.connect((serverHost, serverPort))

while True:
	msg = talk()
	#for linha in msg:
		
	socOb.send(msg)

	data = socOb.recv(1024)
	print('Cliente recebeu: ', data)

	dt = socOb.recv(1024)
	print("SERVER: ", dt)

	if(msg == 'qt'):
		socOb.close()
		break
#	socOb.close()