from socket import *
import threading
def chat_loop(connectionSocket, addr):
    while True:
        try:
            sentence = connectionSocket.recv(1024).decode()
            if sentence=="":
                break
            connectionSocket.send(sentence.encode())
        except ConnectionResetError:
            break
    connectionSocket.close()

threads = []
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
print('El servidor está listo para recibir')
serverSocket.listen(2)
while True:
    connectionSocket, addr = serverSocket.accept()
    t = threading.Thread(target=chat_loop, args=(connectionSocket,addr,))
    threads.append(t)
    t.start()
    
