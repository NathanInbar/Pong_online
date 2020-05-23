import socket, threading, pickle
from player import Player
from message import Message

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5052
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

players = [Player(30,300,20,100,(255,255,255)),Player(550,300,20,100,(255,255,255))]

def handle_client(conn, addr, connNum):
    print(f"[CONNECTION]{addr}, player: {connNum} has connected.")
    msg = Message("Connection Successful!")
    conn.send(pickle.dumps(msg))

def start():
    print("[STARTING] Server is starting...")
    server.listen(2)
    print(f"[LISTENING] Server is listening on {SERVER}")
    connNum = 0
    while True:
        conn,addr = server.accept()#accept incoming connections
        thread = threading.Thread(target=handle_client,args=(conn, addr, connNum))#start new thread for the connection
        thread.start()

        connNum+=1

start()
