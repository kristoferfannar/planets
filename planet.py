from constants import *
import pygame
import math
from time import time

class Planet:
    start = time()
    def __init__(self, distance, color, mass, radius, speed = 0) -> None:
        self.distance = distance
        self.x = distance * DISTANCESCALE + WIDTH / 2 
        self.y = HEIGHT / 2
        self.color = color
        self.mass = mass
        self.radius = radius
        self.sun = True
        self.x_vel = 0
        self.y_vel = 0
        self.multiple = ((distance * DISTANCESCALE ) * 2) / 118
        self.speed = 0

        if distance != 0:
            self.sun = False
            self.radius *= 10
            self.speed = speed/ 10000#TIMESCALE / (self.distance / AU)



    def calc_vel(self):
        if self.sun: return
        self.y_vel = -math.cos((time() - self.start ) * self.speed) * self.multiple * self.speed#* self.distance * DISTANCESCALE / 70
        self.x_vel = -math.sin((time() - self.start ) * self.speed) * self.multiple * self.speed#* self.distance * DISTANCESCALE / 70

        # if abs(self.x_vel) <= 0.08:
        #     print(self.x)

 
    
    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.calc_vel()

    
    def draw(self):
        pygame.draw.circle(WINDOW, self.color, (self.x, self.y), self.radius * RADIUSSCALE)
        self.update()
