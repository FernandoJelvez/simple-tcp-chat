from socket import *
import msvcrt
import threading
import os
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence=""
active=True
def clear():
    os.system("cls" if os.name=="nt" else "clear")
def press():
    global sentence
    global active
    while True:
        key = msvcrt.getwch()
        if len(key)==1 and not key=="\r" and not key =="\x08":
            print(key ,end="", flush=True)
            sentence=sentence+key
        elif key=="\x08":
            print("\b \b" ,end="", flush=True)
            sentence = sentence[:-1]
        elif key=="\r":
            if sentence == '//exit':
                active=False
                break
            sentence=sentence
            clientSocket.send(sentence.encode())
            sentence=""
    clientSocket.close()

t = threading.Thread(target=press, args=())
t.start()
messages=[]
while active:
    receivedSentence = clientSocket.recv(1024)
    messages.append(receivedSentence)
    clear()
    for m in messages:
        print('From Server: ', m.decode())
    print(sentence)
input()
