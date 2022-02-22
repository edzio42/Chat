import socket
import threading

host = '127.0.0.1'  # adres lokalny tzw loopback
port = 8090  # port serwera
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
names = []
def left_chat(client):
    index = clients.index(client)
    clients.remove(client)
    name = names[index]
    brodcast(f'{name} left from chat :O'.encode('utf-8'),client)
    names.remove(name)

def brodcast(message,client):
    for clien in clients:
        if client is not clien:
            clien.send(message)


def handle(client):
    while True:
        try:
            meessage = client.recv(1024)
            if meessage.decode('utf-8')[:2] == '`d':
                left_chat(client)
                break
            brodcast(meessage,client)
        except:
            left_chat(client)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f'Connect with{str(address)}')
        client.send('NICK'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(client)
        print(f'{name} join')
        brodcast(f'{name} join'.encode('utf-8'), client)
        client.send('Conected'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print('server running zium')
receive()
