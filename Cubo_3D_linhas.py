import pygame,sys
from pygame.locals import *

import time
import random

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("3D agora vai")

white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

clock = pygame.time.Clock()

tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

ground_height = 35

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont  = pygame.font.SysFont("comicsansms", 85)


def square (startPoint ,fullSize):
    node_1 = [startPoint[0],startPoint[1]]
    node_2 = [startPoint[0] + fullSize,startPoint[1]]
    node_3 = [startPoint[0],startPoint[1] + fullSize]
    node_4 = [startPoint[0] + fullSize,startPoint[1] + fullSize]

    offset = int (fullSize/2)
    node_5 = [node_1[0]+offset, node_1[1] - offset]
    node_6 = [node_2[0]+offset, node_2[1] - offset]
    node_7 = [node_3[0]+offset, node_3[1] - offset]
    node_8 = [node_4[0]+offset, node_4[1] - offset]

    #top line
    pygame.draw.line(gameDisplay,white,node_1,node_2)
    #bottom line
    pygame.draw.line(gameDisplay, white, node_3, node_4)
    #left line
    pygame.draw.line(gameDisplay, white, node_1, node_3)
    #right line
    pygame.draw.line(gameDisplay, white, node_2, node_4)

    #top line
    pygame.draw.line(gameDisplay,white,node_5,node_6)
    #bottom line
    pygame.draw.line(gameDisplay, white, node_7, node_8)
    #left line
    pygame.draw.line(gameDisplay, white, node_5, node_7)
    #right line
    pygame.draw.line(gameDisplay, white, node_6, node_8)

    pygame.draw.circle(gameDisplay,light_green,node_1,5)
    pygame.draw.circle(gameDisplay,light_green,node_2,5)
    pygame.draw.circle(gameDisplay,light_green,node_3,5)
    pygame.draw.circle(gameDisplay,light_green,node_4,5)

    pygame.draw.circle(gameDisplay,light_green,node_5,5)
    pygame.draw.circle(gameDisplay,light_green,node_6,5)
    pygame.draw.circle(gameDisplay,light_green,node_7,5)
    pygame.draw.circle(gameDisplay,light_green,node_8,5)

    # top line
    pygame.draw.line(gameDisplay, white, node_1, node_5)
    # bottom line
    pygame.draw.line(gameDisplay, white, node_2, node_6)
    # left line
    pygame.draw.line(gameDisplay, white, node_3, node_7)
    # right line
    pygame.draw.line(gameDisplay, white, node_4, node_8)


def gameloop():

    location = [300,200]
    size = 200
    current_move = 0
    local = 0

    z_move=0
    z_location = 1
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == K_LEFT:
                    current_move = -5
                elif evento.key == K_RIGHT:
                    current_move = 5
                elif evento.key == K_UP:
                    z_move = -5
                    x_move =-1
                elif evento.key == K_DOWN:
                    z_move = 5
                    x_move = 1

            elif evento.type == pygame.KEYUP:
                if evento.key == K_LEFT or evento.key == K_RIGHT :
                    current_move =0
                if evento.key == K_UP or evento.key == K_DOWN:
                    z_move = 0
                    x_move = 0
        if z_location > 200:
            z_move = 0

        z_location += z_move
        current_size = int(size/(z_location*0.1))
        location[0] += current_move

        gameDisplay.fill(black)
        square(location,current_size)
        clock.tick(60)
        pygame.display.update()
gameloop()