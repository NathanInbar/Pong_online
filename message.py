import pygame
from player import Player
from ball import Ball

class Message:
    def __init__(self, p1, p2, ball):
        self.p1 = p1
        self.p2 = p2
        self.ball = ball

    def __str__(self):
        #/30 250 20 100 211 38 38 3 770 250 20 100 0 173 181 3 400 300 10 255 255 255 2 2/
        return f"/{str(self.p1), str(self.p2), str(self.ball)}/"
