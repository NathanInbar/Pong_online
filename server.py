import socket, threading, time
from player import Player
from ball import Ball
from message import Message

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5052
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []
client_input = [-1,-1]
players = [Player(30,250,20,100,(211,38,38)), Player(770,250,20,100,(0,173,181))]
ball = Ball(400,300,10,(255,255,255))

#message is just a combination of the players + ball. i.e the game state
msg = Message(players[0], players[1], ball)#init msg
#print(f"FUCK: {msg}")
def handle_client(conn,addr,connNum):
    print(f"[CONNECTION]{addr}, player: {connNum} has connected.")
    connected = True

    while connected:
        #must send key as string like: "w" or "s"
        client_input[connNum] = clients[connNum].recv(256).decode(FORMAT)
        #update_all(f"/{msg}/")

def update_all(): #ask server to update all clients
    global msg
    while True:
        #we want to recieve faster than we send (helps with message confusion)
        time.sleep(0.05)#20hz server LULW
        msg.p1 = players[0]
        msg.p2 = players[1]
        msg.ball = ball

        _msg = str(msg)#turn into string version
        #print(msg)
        for client in clients:#send to all clients
            client.send(_msg.encode(FORMAT))
def start():
    print("[STARTING] Server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    connNum = 0
    while True:
        conn,addr = server.accept()#accept incoming connections
        clients.append(conn)
        #start a thread to update clients and a thread to get client input updates
        thread_u = threading.Thread(target=update_all)
        thread_c = threading.Thread(target=handle_client, args=(conn,addr,connNum))
        thread_c.start()#client update thread
        thread_u.start()#client recieve thread
        connNum+=1

start()
