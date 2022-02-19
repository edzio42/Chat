import socket
import select
import sys
import threading
host = '127.0.0.1'   #adres lokalny tzw loopback
port = 8090   #port serwera
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients=[]
names=[]
def brodcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            meessage=client.recv(1024)
            brodcast(meessage)
        except:
            index=clients.index(client)
            clients.remove(client)
            name=names[index]
            brodcast(f'{name} left from chat :O')
            names.remove(name)
            break
def receive():
    while True:
        client, address = server.accept()
        print(f'Connect with{str(address)}')
        client.send('NICK'.encode('utf-8'))
        name=client.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(client)
        print(f'{name} join')
        brodcast(f'{name} join'.encode('utf-8'))
        client.send('Conected'.encode('utf-8'))
        thread= threading.Thread(target=handle,args=(client,))
        thread.start()
print('server running zium')
receive()