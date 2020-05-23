import pygame

class Player:
    def __init__(self, x=0, y=0, width=0, height=0, color=(0,0,0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.velocity = 3

    def update(self):
        if(pygame.keys[pygame.K_w]):
            self.x -= self.velocity
        if(pygame.keys[pygame.K_s]):
            self.x += self.velocity
        self.rect = self.rect(self.x, self.y, self.width, self.height)

    def render(self, win):
        pygame.draw.rect(win, self.color, self.rect)
