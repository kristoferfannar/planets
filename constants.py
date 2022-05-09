import math
import pygame
HEIGHT = 800
WIDTH  = 1200
G = 6.674e-11
AU = 1.496e11

SUNMASS = 1.989e30 #kg
MERCURYMASS = 3.29e23
VENUSMASS = 4.87e24
EARTHMASS = 5.97e24
MARSMASS = 6.39e23
JUPITERMASS = 1.9e27

SUNRADIUS = 6.9634e9 #meters
MERCURYRADIUS = 2.44e7
VENUSRADIUS = 6.05e7
EARTHRADIUS = 6.371e7
MARSRADIUS = 3.38e7
JUPITERRADIUS = 6.99e8


MERCURYSPEED = 47_870 
VENUSSPEED = 35_020 
EARTHSPEED = 29_720 #m/s
MARSSPEED = 24_000 #m/s




DISTANCESCALE = 70 / AU
RADIUSSCALE = 10 / SUNRADIUS
TIMESTEP =  5 / 1e5 #3600 * 24 # one day


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60




WHITE =   (255, 255, 255)
YELLOW =  (255, 255, 0  )
BLUE =    (  0,   0, 255)
GREEN =   (  0, 255,   0)
RED =     (255,   0,   0)
BLACK =   (0  ,   0,   0)

MARS =    (188, 39 , 49 )
EARTH =   (39 , 168, 208)
VENUS =   (149, 26 , 26 )
MERCURY = (150, 140, 140)
JUPITER = (209, 150, 89 )