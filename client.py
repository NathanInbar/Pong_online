import socket, threading
import time, pygame
from player import Player
from ball import Ball

pygame.font.init()

SERVER = "192.168.86.174"#.174 lappy / .30 deskky
PORT = 5052
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
# - - -
WIDTH = 800
HEIGHT = 600

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
win = pygame.display.set_mode((WIDTH, HEIGHT))

msg = ""
#                                   h
#          Player(100,100,100,100,1000,(100,0,0))
players = [Player(1,80,100,50,(100,200,60)),Player(0,0,0,0,(0,0,0))]
ball = Ball(0,0,0,(0,0,0))

def receive():
    global msg
    while True:
        msg = client.recv(256).decode(FORMAT)
        interpret_msg()

    #print(f"p0: {players[0]}")

def interpret_msg():
    global msg, ball, players
    p1 = []
    p2 = []
    bl = []
    #print(msg)
    #string sanitization:
    #('((30, 250, 20, 100), (211, 38, 38), 3)', '((770, 250, 20, 100), (0, 173, 181), 3)', '((400, 300, 10), (255, 255, 255), 2, 2)')
    print(msg)
    msg = "".join(list([val for val in msg if val.isalnum() or val==" " or val=="/"]))
    c = msg.rfind('/')+1
    msg = msg[c:]
    msg = msg.split()
    for i in range(len(msg)):
        #print(f"MSG:'{msg}'")
        msg[i] = int(msg[i])
    #[30, 250, 20, 100, 211, 38, 38, 3, 770, 250, 20, 100, 0, 173, 181, 3, 400, 300, 10, 255, 255, 255, 2, 2]
    for i in range(len(msg)):
        if i < 8:
            p1.append(msg[i])
        elif i < 16:
            p2.append(msg[i])
        else: bl.append(msg[i])
        #p1#[30, 250, 20, 100, 211, 38, 38, 3]
        #p2#[770, 250, 20, 100, 0, 173, 181, 3]
        #ball#[400, 300, 10, 255, 255, 255, 2, 2]
    #the result of 4am coding:
    players[0].x = p1[0]
    players[0].y = p1[1]
    players[0].width = p1[2]
    players[0].height = p1[3]
    players[0].color = (p1[4], p1[5], p1[6])
    players[0].velocity = p1[7]

    players[1].x = p1[0]
    players[1].y = p1[1]
    players[1].width = p1[2]
    players[1].height = p1[3]
    players[1].color = (p1[4], p1[5], p1[6])
    players[1].velocity =p1[5]

    ball.x = bl[0]
    ball.y = bl[1]
    ball.radius = bl[2]
    ball.color = (bl[3], bl[4], bl[5])
    ball.xVel = bl[6]
    ball.yVel = bl[7]

    #todays forcast: cloudy with a chance of meatballs, folks
    #fuck me.

def renderText(txt, font="consolas",size=30, color=(255,255,255)):
    font = pygame.font.SysFont(font, size)
    text = font.render(txt, 1, color, True)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()

# def update():
#     for player in players:
#         player.update()
#     ball.update()
def update_server():
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_w]):
        client.send("w".encode(FORMAT))
    if(keys[pygame.K_s]):#PROB NEEDS TO BE AN ELIF
        client.send("s".encode(FORMAT))


def render():
    for player in players:
        #print(player.color)
        player.update()#re-set the Rect's correct dims
        player.render(win)
    ball.render(win)
    pygame.display.update()

def start():
    run = True
    clock = pygame.time.Clock()

    while run:
            clock.tick()
            win.fill((30,30,30))
            renderText("Click to Connect...")
            #render()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    try:
                        client.connect(ADDR)
                        print("Connected")
                        thread = threading.Thread(target=receive)
                        thread.start()
                        run = False
                    except ConnectionRefusedError:
                        print("Connection Refused...")
    main()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        win.fill((30,30,30))
        #SEND SERVER (pygame.key.get_pressed())
        update_server()
        render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

start()
