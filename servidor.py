import socket 
import threading

HOST = 'localhost'
PORT = 8089

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print("Aguardando conexões...")

cliente, addr = servidor.accept()
print(f'Conexão estabelecida com {addr}')

while True:
    try:
        mensagem = cliente.recv(1024).decode('utf-8')

        if not mensagem:
            print(f"Cliente {addr} desconectou-se")
            break

        else:
            print(f"Fulano: {mensagem}")

    except ConnectionAbortedError:
        print(f"Cliente {addr} desconectou-se abruptamente")
        break

    except KeyboardInterrupt:
        print("\nServidor encerrado")
        break

cliente.close()
servidor.close()