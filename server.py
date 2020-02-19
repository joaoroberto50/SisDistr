from socket import *
import time
import _thread as th

myHost = ''
myPort = 32123

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))

sockobj.listen(5)

def agora():
	return time.ctime(time.time())

def lidaCliente(conexao):
	time.sleep(5)

	while True:
		data = conexao.recv(1024)

		if not data: break

		resp = 'Eco=>%s as %s' % (data, agora())

		conexao.send(resp.encode())


	conexao.close()

def despacha():
	while True:
		print("Server conectado por ", endereco, end=' ')
		print('as', agora())

		th.start_new_thread(lidaCliente, (conexao))

despacha()