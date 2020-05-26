import pygame

class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.circle = (self.x, self.y, self.radius)
        self.velocity = 2
        self.xVel = self.velocity
        self.yVel = self.velocity
        self.package = (self.circle, self.color, self.xVel, self.yVel)

    def update(self):
        self.x += self.xVel
        self.y += self.yVel
    def render(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

    def __str__(self):
        return f"{self.package}"
