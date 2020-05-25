import pygame

class Player:
    def __init__(self, id, x, y, width, height, color):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.velocity = 3
        self.package = (self.rect,self.color,self.velocity)

    def update(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.x -= self.velocity
        if(keys[pygame.K_s]):
            self.x += self.velocity
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def render(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def __str__(self):
        return f"P{self.id} {self.package}"
