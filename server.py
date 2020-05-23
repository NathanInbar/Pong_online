import socket
import pygame

HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5052
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DC_MSG = "/disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DC_MSG:
                connected = False
                print(f"[DISCONNECTED] {addr} has disconnected")
            else:
                game_update(msg)

def game_update(msg):
    pass

def start():
    print("STARTING] Server is starting...")

    server.listen(2)
    print(f"[LISTENING] Server is listening on {SERVER}")
    connections = 0
    while connections < 2:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))

start()
