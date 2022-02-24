import socket
import tkinter
from tkinter import *
from tkinter import ttk, Text
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = input('Choise your name: ')
client.connect(('127.0.0.1', 8090))
root = Tk()
root.geometry('400x300')
text_view = ttk.Label(root, text='', width=200, anchor=W)
text_view.pack()
text_send = Text(root, width=40, height=2,padx=5,pady=5)
text_send.place(anchor=S)
text_send.pack()

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(name.encode('utf-8'))
            else:
                text_view['text'] += message + '\n'
                text_view.pack()
        except:
            print('errors')
            client.close()
            break


def write(event):
    msg = text_send.get("1.0", "end - 1 chars").strip()
    if msg[:2] == '`d':
        client.close()
        root.quit()
    message = f'{name}: {msg}'
    client.send(message.encode('utf-8'))
    text_send.delete("1.0", "end - 1 chars")
    text_send.pack()


receive_thread = threading.Thread(target=receive)
receive_thread.start()
root.bind('<Return>', write)
root.mainloop()
