import copy
import pygame
import math
import random
aaa,aab,aac,aad,aae,aaf,aag,aah,aai,aaj,aak,aal,aam,aan,aao,aap=3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.1,4.2,4.3,4.4,4.5,4.6,4.7


boards = [
[6.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, 5.0],
[3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 6.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 0.0, 9.0, 0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 6.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, 1.6, 3.0, 0.0, 6.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 1.2, 7.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 0.0, 3.0, aap, 7.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 0.0, 3.0, 1.8, 3.0, 3.0],
[3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, aam, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.9, 0.0, 0.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 9.0, 0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 0.0, 0.0, 0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 0.0, 9.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 0.0, 0.0, 1.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, aao, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 3.0],
[3.0, 1.1, 3.0, 0.0, 6.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, aan, 3.0, 0.0, 6.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, 1.7, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 7.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 0.0, 3.0, 2.2, 7.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 7.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 0.0, 9.0, 0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 0.0, 3.0, 3.0],
[3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 3.0],
[7.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 5.0],
[3.0, 6.0, 4.0, 8.0, 1.0, 7.0, 8.0, 1.0, 3.0, 3.0, 1.0, 7.0, 4.0, 4.0, 5.0, 6.0, 4.0, 4.0, 8.0, 1.0, 3.0, 3.0, 1.0, 7.0, 8.0, 1.0, 7.0, 4.0, 5.0, 3.0],
[3.0, 3.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.0, 3.0, 1.0, 1.0, 1.0, 1.0, 3.0, 3.0, 1.0, 1.0, 1.0, 1.0, 3.0, 3.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.0, 3.0],
[3.0, 3.0, 1.0, 6.0, 4.0, 4.0, 4.0, 4.0, 8.0, 7.0, 4.0, 4.0, 5.0, 1.0, 3.0, 3.0, 1.0, 6.0, 4.0, 4.0, 8.0, 7.0, 4.0, 4.0, 4.0, 4.0, 5.0, 1.0, 3.0, 3.0]
         ]

pygame.init()

WIDTH = 900
HEIGHT = 840
screen = pygame.display.set_mode([WIDTH, HEIGHT],pygame.RESIZABLE)
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = copy.deepcopy(boards)
color = 'teal'
PI = math.pi
player_images = []

player_images.append(pygame.transform.scale(pygame.image.load(f"3.png"), (45, 45)))

player_x = 445
player_y = 633
direction = 1

counter = 0
# R, L, U, D
turns_allowed = [False, False, False, False]
direction_command = 0
player_speed = 1
dc2=0
d2=3

def draw_board():
    num1 = ((HEIGHT ) // 30)
    num2 = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2 :
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
                
def yelvert(i,j,yel1,yel2,v,V,h,yel):
            if level[i][j] == v and v==yel:
                pygame.draw.line(screen, 'yellow', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            elif level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            if level[i][j] == V and V==yel:
                pygame.draw.line(screen, 'yellow', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            elif level[i][j] == V:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            
            
            if level[i][j] == h and h==yel:
                pygame.draw.line(screen, 'yellow', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            elif level[i][j] == h:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
                
                
def yelhorz(i,j,yel1,yel2,v,h,H,yel):
            if level[i][j] == v and v==yel:
                pygame.draw.line(screen, 'yellow', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            elif level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)


            if level[i][j] == h and h==yel:
                pygame.draw.line(screen, 'yellow', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            elif level[i][j] == h:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            if level[i][j] == H and H==yel:
                pygame.draw.line(screen, 'yellow', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            elif level[i][j] == H:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
                
                
def yelmid(i,j,yel1,yel2,v,V,h,H,yel):
            if level[i][j] == v and v==yel:
                pygame.draw.line(screen, 'yellow', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            elif level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            if level[i][j] == V and V==yel:
                pygame.draw.line(screen, 'yellow', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            elif level[i][j] == V:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)


            if level[i][j] == h and h==yel:
                pygame.draw.line(screen, 'yellow', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            elif level[i][j] == h:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            if level[i][j] == H and H==yel:
                pygame.draw.line(screen, 'yellow', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            elif level[i][j] == H:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)

def redvh(i,j,yel1,yel2,v,H):
            if level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            
            
            if level[i][j] == H:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)

def redvv(i,j,yel1,yel2,v,V):
            if level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            if level[i][j] == V:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            
def redhh(i,j,yel1,yel2,h,H):
            if level[i][j] == h:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            if level[i][j] == H:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)

def redmh(i,j,yel1,yel2,v,h,H):
            if level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)


            if level[i][j] == h:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            if level[i][j] == H:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
                
def redmv(i,j,yel1,yel2,v,V,h):
            if level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            if level[i][j] == V:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)


            if level[i][j] == h:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
                
def rednew(E,W,N,S,g1,g2,g3,g4):
    global ggs
    global k
    global run
    yel1 = ((HEIGHT) // 30)
    yel2 = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            # if ggs<2000:
            #     if level[i][j] == g1:
            #         level[i][j]=0.91
            #     if level[i][j] == g2:
            #         level[i][j]=0.92
            #     if level[i][j] == g4:
            #         level[i][j]=0.93
            #     if level[i][j] == 0.94:
            #         level[i][j]=g3
                if ggs<1500:
                    if level[i][j] == N:
                        level[i][j]=0.9
                    redmv(i,j,yel1,yel2,E,W,S)
                if ggs<2000 and ggs>=1500:
                    if level[i][j] == 0.9:
                        level[i][j] = N
                    yelmid(i,j,yel1,yel2,E,W,N,S,N)
            # if ggs<4000 and ggs>=2000:
            #     if level[i][j] == g1:
            #         level[i][j]=0.91
            #     if level[i][j] == 0.92:
            #         level[i][j]=g2
            #     if level[i][j] == g4:
            #         level[i][j]=0.93
            #     if level[i][j] == g3:
            #         level[i][j]=0.94
                if ggs<3500 and ggs>=2000:
                    if level[i][j] == W:
                        level[i][j]=0.9
                    redmh(i,j,yel1,yel2,E,S,N)
                if ggs<4000 and ggs>=3500:
                    if level[i][j] == 0.9:
                        level[i][j] = W
                    yelmid(i,j,yel1,yel2,E,W,N,S,W)
            # if ggs<6000 and ggs>=4000:
            #     if level[i][j] == g1:
            #         level[i][j]=0.91
            #     if level[i][j] == g2:
            #         level[i][j]=0.92
            #     if level[i][j] == 0.93:
            #         level[i][j]=g4
            #     if level[i][j] == g3:
            #         level[i][j]=0.94
                if ggs<5500 and ggs>=4000:
                    if level[i][j] == S:
                        level[i][j] = 0.9
                    redmv(i,j,yel1,yel2,E,W,N)
                if ggs<6000 and ggs>=5500:
                    if level[i][j] == 0.9:
                        level[i][j] = S
                    yelmid(i,j,yel1,yel2,E,W,N,S,S)
            # if ggs<=8000 and ggs>=6000:
            #     if level[i][j] == 0.91:
            #         level[i][j]=g1
            #     if level[i][j] == g2:
            #         level[i][j]=0.92
            #     if level[i][j] == 0.93:
            #         level[i][j]=g4
            #     if level[i][j] == 0.94:
            #         level[i][j]=g3
                if ggs<7500 and ggs>=6000:
                    if level[i][j] == E:
                        level[i][j] = 0.9
                    redmh(i,j,yel1,yel2,W,S,N)
                if ggs<=8000 and ggs>=7500:
                    if level[i][j] == 0.9:
                        level[i][j] = E
                    yelmid(i,j,yel1,yel2,E,W,N,S,E)
                if ggs==8000:
                    ggs=0

def yelvertnew(V,v,H,T,h,g1,g2,g3):
    global k
    global run
    R=k+T
    yel1 = ((HEIGHT) // 30)
    yel2 = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if R<1500:
                if level[i][j] == v:
                    level[i][j]=h
                redvh(i,j,yel1,yel2,V,H)
            if R<2000 and R>=1500:
                if level[i][j] == h:
                    level[i][j]=v
                yelvert(i,j,yel1,yel2,V,v,H,v)
            if R<3500 and R>=2000:
                if level[i][j] == V:
                    level[i][j]=h
                redvh(i,j,yel1,yel2,v,H)
            if R<4000 and R>=3500:
                if level[i][j] == h:
                    level[i][j]=V
                yelvert(i,j,yel1,yel2,V,v,H,V)
            if R<5500 and R>=4000:
                if level[i][j] == H:
                    level[i][j]=h
                redvv(i,j,yel1,yel2,V,v)
            if R<=6000 and R>=5500:
                if level[i][j] == h:
                    level[i][j]=H
                yelvert(i,j,yel1,yel2,V,v,H,H)
            if R==6000:
                k=0
                

def yelhorznew(V,H,h,T,f,g3,g1,g2):
    global r
    global run
    R=r+T
    yel1 = ((HEIGHT) // 30)
    yel2 = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            # if r <2000:
            #     if level[i][j] == g1:
            #         level[i][j]=0.61
            #     if level[i][j] == 0.62:
            #         level[i][j]=g2
            #     if level[i][j] == g3:
            #         level[i][j]=0.63
                if R<1500:
                    if level[i][j] == h:
                        level[i][j]=f
                    redvh(i,j,yel1,yel2,V,H)
                if R<2000 and R>=1500:
                    if level[i][j] == f:
                        level[i][j]=h
                    yelhorz(i,j,yel1,yel2,V,H,h,h)
            # if r <4000 and r>=2000:
            #     if level[i][j] == 0.61:
            #         level[i][j]=g1
            #     if level[i][j] == g2:
            #         level[i][j]=0.62
            #     if level[i][j] == g3:
            #         level[i][j]=0.63
                if R<3500 and R>=2000:
                    if level[i][j] == H:
                        level[i][j]=f
                    redvh(i,j,yel1,yel2,V,h)
                if R<4000 and R>=3500:
                    if level[i][j] == f:
                        level[i][j]=H
                    yelhorz(i,j,yel1,yel2,V,H,h,H)
            # if r <6000 and r>=4000:
            #     if level[i][j] == g1:
            #         level[i][j]=0.61
            #     if level[i][j] == g2:
            #         level[i][j]=0.62
            #     if level[i][j] == 0.63:
            #         level[i][j]=g3
                if R<5500 and R>=4000:
                    if level[i][j] == V:
                        level[i][j]=f
                    redhh(i,j,yel1,yel2,H,h)
                if R<=6000 and R>=5500:
                    if level[i][j] == f:
                        level[i][j]=V
                    yelhorz(i,j,yel1,yel2,V,H,h,V)
                if R==6000:
                    r=0

def draw_player():
    # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
    global turns_allowed
    global player_x
    global player_y
    global ggs
    global direction
    global direction_command
    if direction == 0:
        screen.blit(player_images[counter], (player_x, player_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter], True, False), (player_x, player_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter], 90), (player_x, player_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter], 270), (player_x, player_y))
    turns_allowed = check_position(center_x, center_y)

    player_x, player_y = move_player(player_x, player_y)
    if ggs%25==0:
        if turns_allowed[2]and turns_allowed[1]and turns_allowed[3]:
            l1=[3,1,2]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[0]and turns_allowed[1]and turns_allowed[3]:
            l1=[0,1,3]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[2]and turns_allowed[1]and turns_allowed[0]:
            l1=[0,1,2]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[2]and turns_allowed[3]and turns_allowed[0]:
            l1=[0,3,2]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[0]and turns_allowed[3]:
            l1=[0,3]
            M1=random.choice(l1)
            direction_command = M1          
        if turns_allowed[3]and turns_allowed[1]:
            l1=[3,1]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[0]and turns_allowed[1]:
            l1=[0,1]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[2]and turns_allowed[3]:
            l1=[2,3]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[2]and turns_allowed[0]:
            l1=[0,2]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[2]and turns_allowed[1]:
            l1=[2,1]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[3]:
            l1=[3]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[1]:
            l1=[1]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[2]:
            l1=[2]
            M1=random.choice(l1)
            direction_command = M1
        if turns_allowed[0]:
            l1=[0]
            M1=random.choice(l1)
            direction_command = M1
    if direction_command == 0 and turns_allowed[0]:
        direction = 0
    if direction_command == 1 and turns_allowed[1]:
        direction = 1
    if direction_command == 2 and turns_allowed[2]:
        direction = 2
    if direction_command == 3 and turns_allowed[3]:
        direction = 3


def check_position(centerx, centery):
    turns = [False, False, False, False]
    num1 = (HEIGHT ) // 30
    num2 = (WIDTH // 30)
    num3 = 15
    # pixel_color = player_images.get_at(())
    # check collisions based on center x and center y of player +/- fudge number
    if centerx // 30 < 29:
        if direction == 0:
            if level[centery // num1][(centerx - num3) // num2] < 1:
                turns[1] = False
        if direction == 1:
            if level[centery // num1][(centerx + num3) // num2] < 1:
                turns[0] = False
        if direction == 2:
            if level[(centery + num3) // num1][centerx // num2] < 1:
                turns[3] = False
        if direction == 3:
            if level[(centery - num3) // num1][centerx // num2] < 1:
                turns[2] = False

        if direction == 2:
            if 13 <= centerx % num2 <= 17:
                if level[(centery + num3) // num1][centerx // num2] < 1:
                    turns[3] = False
                if level[(centery - num3) // num1][centerx // num2] < 1:
                    turns[2] = True
            if 13 <= centery % num1 <= 17:
                if level[centery // num1][(centerx - num2) // num2] < 1:
                    turns[1] = True
                if level[centery // num1][(centerx + num2) // num2] < 1:
                    turns[0] = True
        if direction == 3:
            if 13 <= centerx % num2 <= 17:
                if level[(centery + num3) // num1][centerx // num2] < 1:
                    turns[3] = True
                if level[(centery - num3) // num1][centerx // num2] < 1:
                    turns[2] = False
            if 13 <= centery % num1 <= 17:
                if level[centery // num1][(centerx - num2) // num2] < 1:
                    turns[1] = True
                if level[centery // num1][(centerx + num2) // num2] < 1:
                    turns[0] = True
        if direction == 0:
            if 13 <= centerx % num2 <= 17:
                if level[(centery + num1) // num1][centerx // num2] < 1:
                    turns[3] = True
                if level[(centery - num1) // num1][centerx // num2] < 1:
                    turns[2] = True
            if 13 <= centery % num1 <= 17:
                if level[centery // num1][(centerx - num3) // num2] < 1:
                    turns[1] = False
                if level[centery // num1][(centerx + num3) // num2] < 1:
                    turns[0] = True
        if direction == 1:
            if 13 <= centerx % num2 <= 17:
                if level[(centery + num1) // num1][centerx // num2] < 1:
                    turns[3] = True
                if level[(centery - num1) // num1][centerx // num2] < 1:
                    turns[2] = True
            if 13 <= centery % num1 <= 17:
                if level[centery // num1][(centerx - num3) // num2] < 1:
                    turns[1] = True
                if level[centery // num1][(centerx + num3) // num2] < 1:
                    turns[0] = False



    return turns


def move_player(play_x, play_y):
    # r, l, u, d
    if direction == 0 and turns_allowed[0]:
        play_x += player_speed
    elif direction == 1 and turns_allowed[1]:
        play_x -= player_speed
    if direction == 2 and turns_allowed[2]:
        play_y -= player_speed
    elif direction == 3 and turns_allowed[3]:
        play_y += player_speed
    return play_x, play_y

ggs=0
ggk=0
k=3500
r=2000
NEXT=0
x2,y2=445,400

run = True
while run:


    screen.fill('black')
    draw_board()
    center_x = player_x + 23
    center_y = player_y + 24
    cx2 = x2 + 23
    cy2 = y2 + 24

    player_circle = pygame.draw.circle(screen, 'black', (center_x, center_y), 20, 2)
    draw_player()



    # turns_allowed = check_position(center_x, center_y)

    # player_x, player_y = move_player(player_x, player_y)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        NEXTTIMER=pygame.USEREVENT+1
        pygame.time.set_timer(NEXTTIMER, 1)
        if event.type==NEXTTIMER:
            ggs+=1
            k+=1
            r+=1
            # print(k)
            # print(ggs)
        # list1 = [0, 1, 2, 3]
        # M1=random.choice(list1)
        rednew(aam,aao,aap,aan,6.4,6.6,6.7,6.5)  
        yelvertnew(1.5,1.4,1.6,0,0.8,5.1,5.2,5.3)
        yelvertnew(2.1,2.3,2.2,0,0.7,6.1,6.3,6.2)
        yelhorznew(1.3,1.1,1.2,0,0.6,5.6,5.4,5.5)
        yelhorznew(1.9,1.8,1.7,0,0.5,5.9,5.8,5.7)

    pygame.display.flip()
pygame.quit()
