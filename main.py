#!/usr/bin/env python
import pygame, sys, random, math
from pygame.locals import *

# FPS
FPS = 200

# Colors
WHITE = pygame.Color(255, 255, 255)
COOLWHITE = pygame.Color(100, 100, 100)
BLACK = pygame.Color(0, 0, 0)
ICEBLUE = pygame.Color(150, 170, 255)
DARKBLUE = pygame.Color(0, 0, 10)

def main():
    pygame.init()

    FPSCLOCK = pygame.time.Clock()

    # Globals
    global SCREEN_WIDTH, SCREEN_HEIGHT, DISPLAYSURF
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    global LINETHICKNESS
    LINETHICKNESS = 1

    snowspeed = 1.5

    # Set window title
    pygame.display.set_caption('Snowflakes!')

    # Set display surface and background
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    snow = generateSnowArray(90, 5, 25)

    while True:
        # loop through all events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # clear screen
        DISPLAYSURF.fill(DARKBLUE)

        # draw snowflakes
        for flake in snow:
            drawSnowflake(DISPLAYSURF, (flake[0], flake[1]), flake[2], flake[3], COOLWHITE, 10, False, True, LINETHICKNESS)
            flake[1] += snowspeed * (random.choice([snowspeed, 2 * (snowspeed/3)]))
            flake[0] += random.randint(-1, 1) * snowspeed
            flake[3] += flake[4] * snowspeed

            if flake[1] > SCREEN_HEIGHT:
                flake[1] = 0

        # Update screen
        pygame.display.update()

        # Tick
        FPSCLOCK.tick(FPS)

def generateSnowArray(n, l, h):
    array = []
    for i in range(n):
        array.append([random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), random.randint(l, h), random.randint(0, 360), random.choice([-1, 1])])

    return array


def drawAsterisk(surface, (x, y), r, rot, color, thickness):
    # Draw main spokes
    for i in range(0, 6):
        # Get the degree angle to draw line, then convert to radians
        deg = (360 / 6) * i + rot
        rad = math.radians(deg)

        # Translate into x and y vectors
        xv = math.sin(rad)
        yv = math.cos(rad)

        # Draw spoke
        pygame.draw.line(surface, color, (x, y), (x + (xv * r), y + (yv * r)), thickness)

def drawSnowflake(surface, (x, y), r, rot, color, linesize, outline, fancy, thickness):
    if outline or not fancy:
        drawAsterisk(surface, (x, y), r, rot, color, thickness)

    if fancy:
        for i in range(0, 6):
            # Get the degree angle to draw line, then convert to radians
            deg = (360 / 6) * i + rot
            rad = math.radians(deg)

            # Translate into x and y vectors
            xv = math.sin(rad)
            yv = math.cos(rad)

            for i in range(0, 10, 2):
                drawAsterisk(surface, (x + i * xv * (r / 10), y + i * yv * (r / 10)), math.log1p(i) * r / linesize, rot, color, thickness)

# Run main only if directly executed
if __name__ == '__main__':
    main()

