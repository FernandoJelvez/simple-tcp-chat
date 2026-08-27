from socket import *
import msvcrt
import threading
import os

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
            if not sentence =="":
                print("\b \b" ,end="", flush=True)
                sentence = sentence[:-1]
        elif key=="\r":
            if sentence == '//exit':
                active=False
                break
            clientSocket.send(sentence.encode())
            clear()
            messages.append(("me> "+sentence))
            sentence=""
            for m in messages:
                print(m)
            print("> ", end="", flush=True)
    clientSocket.close()

while True:
    serverName = input("server name: ")
    serverPort = 12000
    print("connecting to",serverName+":"+str(serverPort))
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
    except gaierror:
        print("could no connect to",serverName,"- please check your connection or typing mistakes")
    else:
        break
print("connected")
name=input("name: ")
clientSocket.send(name.encode())
print("wait...")
t = threading.Thread(target=press, args=())
t.start()
messages=[]
print("startup complete")
while active:
    receivedSentence = clientSocket.recv(1024)
    messages.append(receivedSentence.decode())
    clear()
    for m in messages:
        print(m)
    print("> "+sentence, end="", flush=True)
input()
