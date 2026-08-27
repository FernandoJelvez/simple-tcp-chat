from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True:
    sentence = input('Escribe una frase en minúsculas:')
    if sentence == '//exit':
        break
    clientSocket.send(sentence.encode())
    receivedSentence = clientSocket.recv(1024)
    print('From Server: ', receivedSentence.decode())
clientSocket.close()
