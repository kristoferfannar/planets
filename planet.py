from constants import *
import pygame
import math

class Planet:
    def __init__(self, distance, color, mass, radius) -> None:
        self.distance = abs(distance)
        self.x = distance * DISTANCESCALE + WIDTH / 2 
        self.y = HEIGHT / 2
        self.color = color
        self.mass = mass
        self.radius = radius
        self.sun = True
        self.x_vel = 0
        self.y_vel = 0
        self.orbit = []

        if distance != 0:
            self.sun = False
            self.radius *= 100
            self.y_vel = math.sqrt(G*SUNMASS/self.distance)




    def calc_vel(self):
        if self.sun: return

        x_distance = WIDTH / 2 - self.x
        y_distance = HEIGHT / 2 - self.y
        distance = math.sqrt(x_distance**2 + y_distance**2)

        force = G*SUNMASS * self.mass / (distance**2)
        theta = math.atan2(y_distance, x_distance)
        x_force = math.cos(theta) * force
        y_force = math.sin(theta) * force


        self.x_vel += x_force / self.mass * TIMESTEP * DISTANCESCALE#tok mig allan dag að fatta að hafa * DISTANCESCALE. 
        self.y_vel += y_force / self.mass * TIMESTEP * DISTANCESCALE #var að klara nuna kl 1:20

        #print(x_force, y_force)
        #print(x_distance, y_distance)
        print(self.x_vel, self.y_vel)
        #print(theta)
 
    

    def update(self):
        self.calc_vel()
        self.x += self.x_vel * TIMESTEP
        self.y += self.y_vel * TIMESTEP
        self.orbit.append((self.x, self.y))

    
    def draw(self):
        self.draw_orbit()
        pygame.draw.circle(WINDOW, self.color, (self.x, self.y), self.radius * RADIUSSCALE)
        self.update()

    
    def draw_orbit(self):
        for coords in self.orbit:
            pygame.draw.circle(WINDOW, WHITE, coords, 1)




if __name__ == "__main__":
    print (AU / (1.496e11) )
    print ( 6.67e-11 / G)