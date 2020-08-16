from Color import Color
from math import sqrt
import pygame


class Ball(object):
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x-self.radius <= 0 or self.x+self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y-self.radius <= 0 or self.y+self.radius >= screen.get_width():
            self.sy = -self.sy

    def eat(self, other):
        if self.alive and other.alive and self != other:
            dx, dy = self.x-other.x, self.y-other.y
            distance = sqrt(dx**2+dy**2)
            if distance < self.radius+other.radius and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius+int(other.radius*0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)
