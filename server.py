import socket, threading, time
from player import Player
from ball import Ball

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5052
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []
players = [Player(0, 30,250,20,100,(211,38,38)),Player(1, 770,250,20,100,(0,173,181))]
ball = Ball(400,300,10,(255,255,255))

def handle_client(conn, addr, connNum):
    print(f"[CONNECTION]{addr}, player: {connNum} has connected.")
    clients.append(conn)
    connected = True
    while connected:
        time.sleep(0.1)#if we send the client information faster than it recieves the message, it wont be able
                       #to differentiate where one msg ends and where one begins
        update_all(players[0])

def update_all(msg): #ask server to update all clients
    msg = str(msg)
    for client in clients:
        client.send(msg.encode(FORMAT))

def start():
    print("[STARTING] Server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    connNum = 0
    while True:
        conn,addr = server.accept()#accept incoming connections
        thread = threading.Thread(target=handle_client,args=(conn, addr, connNum))#start new thread for the connection
        thread.start()
        connNum+=1

start()
