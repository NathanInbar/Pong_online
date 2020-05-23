import socket
import pygame, time
pygame.font.init()

HEADER = 64
SERVER = "192.168.86.36"
PORT = 5052
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DC_MSG = "/disconnect"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

width = 800
height = 600

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong - Client")

def main():
    clock.tick(60)
    win.fill(30,30,30)

def update():
    pass
def render():
    pass
def start():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((30,30,30))
        font = pygame.font.SysFont("consolas", 30)
        text = font.render("Click to Connnect to Server...", 1, (255,255,255), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    client.connect(ADDR)
                    run = False
                except:
                    print("connection failed")
    main()

start()
