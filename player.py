import pygame

class Player:
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self):

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)
