import pygame

class Ball():
    def __init__(self, x=0, y=0, radius=0, color=(0,0,0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.circle = (self.x, self.y, self.radius)
        self.velocity = 2
        self.xVel = self.velocity
        self.yVel = self.velocity

    def update(self):
        self.x += self.xVel
        self.y += self.yVel
    def render(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
