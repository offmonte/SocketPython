#ClienteTCP

from socket import *

servidor="127.0.0.1" #localhost
porta= 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor,porta))
msg = bytes(input("Digite algo: "), 'utf-8')
obj_socket.send(msg)
resposta = obj_socket.recv(1024)
print("Recebemos: ", resposta)
obj_socket.close()