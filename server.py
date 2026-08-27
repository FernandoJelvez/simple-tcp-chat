from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
print('El servidor está listo para recibir')
serverSocket.listen(1)
while True:
    connectionSocket, addr = serverSocket.accept()
    while True:
        try:
            sentence = connectionSocket.recv(1024).decode()
            if sentence=="":
                break
            connectionSocket.send(sentence.encode())
        except ConnectionResetError:
            break
    connectionSocket.close()
