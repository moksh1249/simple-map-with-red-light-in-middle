
import copy
from board import boards
import pygame
import math
import time

pygame.init()

WIDTH = 850
HEIGHT = 850
screen = pygame.display.set_mode([WIDTH, HEIGHT],pygame.RESIZABLE)
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = copy.deepcopy(boards)
color1 = 'teal'
color2 = 'teal'
PI = math.pi
TIMEREVENT=pygame.USEREVENT+1
pygame.time.set_timer(TIMEREVENT, 1000)
player_images = []



def draw_board():
    num1 = ((HEIGHT) // 48)
    num2 = (WIDTH // 48)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1.0:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2.0:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3.0:
                pygame.draw.line(screen, color1, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if level[i][j] == 4.0:
                pygame.draw.line(screen, color1, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5.0:
                pygame.draw.arc(screen, color2, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if level[i][j] == 6.0:
                pygame.draw.arc(screen, color2,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if level[i][j] == 7.0:
                pygame.draw.arc(screen, color2, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if level[i][j] == 8.0:
                pygame.draw.arc(screen, color2,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if level[i][j] == 9.0:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                
def yelvert(v,V,h,yel):
    yel1 = ((HEIGHT) // 48)
    yel2 = (WIDTH // 48)
    for i in range(len(level)):
        for j in range(len(level[i])):
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
                
                
def yelhorz(v,h,H,yel):
    yel1 = ((HEIGHT) // 48)
    yel2 = (WIDTH // 48)
    for i in range(len(level)):
        for j in range(len(level[i])):
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
                
                
def yelmid(v,V,h,H,yel):
    yel1 = ((HEIGHT) // 48)
    yel2 = (WIDTH // 48)
    for i in range(len(level)):
        for j in range(len(level[i])):
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

            
def redvh(v,H):
    yel1 = ((HEIGHT) // 48)
    yel2 = (WIDTH // 48)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            
            
            if level[i][j] == H:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)

def refvv(v,V):
    yel1 = ((HEIGHT) // 48)
    yel2 = (WIDTH // 48)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            if level[i][j] == V:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            
def redhh(h,H):
    yel1 = ((HEIGHT) // 48)
    yel2 = (WIDTH // 48)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == h:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            if level[i][j] == H:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)

def redmh(v,h,H):
    yel1 = ((HEIGHT) // 48)
    yel2 = (WIDTH // 48)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)


            if level[i][j] == h:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
            if level[i][j] == H:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
                
def redmv(v,V,h):
    yel1 = ((HEIGHT) // 48)
    yel2 = (WIDTH // 48)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == v:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)
            if level[i][j] == V:
                pygame.draw.line(screen, 'red', (j * yel2 + (0.5 * yel2), i * yel1),
                                 (j * yel2 + (0.5 * yel2), i * yel1 + yel1), 3)


            if level[i][j] == h:
                pygame.draw.line(screen, 'red', (j * yel2, i * yel1 + (0.5 * yel1)),
                                 (j * yel2 + yel2, i * yel1 + (0.5 * yel1)), 3)
        
        
def rednew(E,W,N,S):
    global ggs
    global run
    for event in pygame.event.get():            
            NEXTTIMER=pygame.USEREVENT+1
            pygame.time.set_timer(NEXTTIMER, 1000)
            if event.type==NEXTTIMER:
                ggs+=1
                print(ggs)
            if ggs<15:
                redmv(E,W,S)
            if ggs<20 and ggs>=15:
                yelmid(E,W,N,S,N)
            if ggs<35 and ggs>=20:
                redmh(E,S,N)
            if ggs<40 and ggs>=35:
                yelmid(E,W,N,S,W)
            if ggs<55 and ggs>=40:
                redmv(E,W,N)
            if ggs<60 and ggs>=55:
                yelmid(E,W,N,S,S)
            if ggs<75 and ggs>=60:
                redmh(W,S,N)
            if ggs<=80 and ggs>=75:
                yelmid(E,W,N,S,E)
            if ggs==80:
                ggs=0
            if event.type == pygame.QUIT:
                run = False
            pygame.display.flip()

ggs=0
run = True
while run:
            
    timer.tick(fps)
    screen.fill('black')
    draw_board()
    rednew(2.4,2.6,2.7,2.5,)
pygame.quit()



