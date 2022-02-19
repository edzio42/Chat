import socket
import select
import sys
import threading
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name=input('Choise your name: ')
client.connect(('127.0.0.1',8090))
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message=='NICK':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print('errors')
            client.close()
            break
def write():
    while True:
        message= f'{name}: {input("")}'
        client.send(message.encode('utf-8'))
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()