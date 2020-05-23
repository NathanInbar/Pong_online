import socket, threading, pickle
from message import Message
from player import Player
from ball import Ball

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5052
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []
players = [Player(30,250,20,100,(211,38,38)),Player(770,250,20,100,(0,173,181))]
ball = Ball(400,300,10,(255,255,255))

msg = Message(Player(), Player(), ball)#create an empty message to be modified when p1 / p2 joins

def handle_client(conn, addr, connNum):
    global msg
    print(f"[CONNECTION]{addr}, player: {connNum} has connected.")
    clients.append(conn)
    connected = True
    while connected:
        if connNum == 0:#if player 1,
            msg.player1 = players[0]
        else: msg.player2 = players[1]

        #msg = Message(players[0],players[1],ball)#create a message containing player & ball info

        update_all()
        #print(f"message sent to client {connNum}")

def update_all(): #ask server to update all clients
    global msg
    for client in clients:
        client.send(pickle.dumps(msg))

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
