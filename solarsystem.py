import pygame
import math
from constants import *
from planet import Planet


pygame.display.set_caption("Solar System")

clock = pygame.time.Clock()
 


def main():
    
    sun = Planet(0, YELLOW, SUNMASS, SUNRADIUS)
    mercury = Planet(0.4*AU, MERCURY, MERCURYMASS, MERCURYRADIUS, MERCURYSPEED)
    venus = Planet(0.7*AU, VENUS, VENUSMASS, VENUSRADIUS, VENUSSPEED)
    earth = Planet(AU, EARTH, EARTHMASS, EARTHRADIUS, EARTHSPEED)
    mars = Planet(1.5*AU, MARS, MARSMASS, MARSRADIUS, MARSSPEED)
    jupiter = Planet(5.2*AU, JUPITER, JUPITERMASS, JUPITERRADIUS)


    planets = [sun, earth, mars, venus, mercury, jupiter]

    run = True
    
    while run:
        clock.tick(FPS)
        WINDOW.fill(BLACK)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()