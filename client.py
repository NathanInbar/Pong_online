import socket, pickle, threading
import time, pygame
from message import Message
pygame.font.init()

SERVER = "192.168.86.30"
PORT = 5052
ADDR = (SERVER, PORT)
# - - -
WIDTH = 800
HEIGHT = 600

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
win = pygame.display.set_mode((WIDTH, HEIGHT))

msg = Message("!msg")

def receive():
    global msg
    while True:
        msg = pickle.loads(client.recv(2048))

def renderText(txt, font="consolas",size=30, color=(255,255,255)):
    font = pygame.font.SysFont(font, size)
    text = font.render(txt, 1, color, True)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()

def render():
    pygame.display.update()

def start():
    run = True
    clock = pygame.time.Clock()

    while run:
            clock.tick()
            win.fill((30,30,30))
            renderText("Waiting for Player...")
            render()
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
        renderText(f"{msg.txt}")
        render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

start()
