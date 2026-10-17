import socket
import threading

HOST = 'localhost'
PORT = 8089

cliente = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

cliente.connect((HOST, PORT))
print("Conectado ao servidor")

while True:
    
    try:
        mensagem = input("")
        cliente.send(mensagem.encode('utf-8'))

    except (BrokenPipeError, ConnectionResetError):
        cliente.close()
        print("Você foi desconectado do servidor")
        break

    except KeyboardInterrupt:
        print("\nVocê se desconectou do servidor")
        break

cliente.close()