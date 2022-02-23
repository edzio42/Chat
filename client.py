import socket
import tkinter
from tkinter import *
from tkinter import ttk
import threading
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name=input('Choise your name: ')
client.connect(('127.0.0.1',8090))
root =Tk()
root.geometry('400x300')
text_view=ttk.Label(root,text='nic',width=200,height=300,anchor=W)
text_view.pack()
text_send=tkinter.Text(root,width=40,height=200)

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message=='NICK':
                client.send(name.encode('utf-8'))
            else:
                text_view['text']+=message+'\n'
                text_view.pack()
        except:
            print('errors')
            client.close()
            break
def write():
    while True:
        msg=text_send.

        if msg[:2]=='`d':
            client.close()
            root.quit()
            break
        message= f'{name}: {msg}'
        client.send(message.encode('utf-8'))
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
root.mainloop()
