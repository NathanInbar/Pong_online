import socket, threading, pickle
from player import Player


SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5052
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

players = [Player(30,300,20,100,(255,255,255)),Player(550,300,20,100,(255,255,255))]

def handle_client(conn, addr, connNum):
    print(f"[CONNECTION] {conn}, {addr}, {connNum} has connected.")

def start():
    print("[STARTING] Server is starting...")
    server.listen(2)
    print(f"[LISTENING] Server is listening on {SERVER}")
    connNum = 0
    while True:
        conn,addr = server.accept()#accept incoming connections
        threading.Thread(target=handle_client,args=(conn, addr, connNum))#start new thread for the connection
        connNum+=1

start()
