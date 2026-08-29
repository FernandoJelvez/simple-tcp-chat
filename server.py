from socket import *
import threading
def chat_loop(connectionSocket, addr, name):
    while True:
        try:
            sentence = connectionSocket.recv(1024).decode()
            if sentence=="":
                break
                print("closing ",addr)
            print(sentence)
            others = threads.copy()
            others.pop(addr[0]+":"+str(addr[1]))
            for t in others:
                others[t].send((name+"< "+sentence).encode())
        except ConnectionResetError:
            print("closing a reset connection...")
            break
    connectionSocket.close()
    threads.pop(addr[0]+":"+str(addr[1]))
    print(threads)

threads = {}
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
print('El servidor está listo para recibir')
serverSocket.listen(2)
while True:
    connectionSocket, addr = serverSocket.accept()
    connectionSocket.send("CONNECTED".encode())
    name = connectionSocket.recv(1024).decode()
    connectionSocket.send(("Welcome "+name+"!").encode())
    t = threading.Thread(target=chat_loop, args=(connectionSocket,addr,name,))
    threads[addr[0]+":"+str(addr[1])]=connectionSocket
    t.start()
    
