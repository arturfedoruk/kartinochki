import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

pygame.draw.rect(screen, (128,128,128), (0,0,400,400)) ## фон
pygame.draw.circle(screen, (255, 255, 0), (200,200), 150) ## рожа
pygame.draw.circle(screen, (178,34,34), (145,155), 30) ## левый глаз
pygame.draw.circle(screen, (0,0,0), (145,155), 30, 3)
pygame.draw.circle(screen, (178,34,34), (255,155), 30) ## правый глаз
pygame.draw.circle(screen, (0,0,0), (255,155), 30, 3)
pygame.draw.circle(screen, (0,0,0), (145,155), 10) ## левый зрачок
pygame.draw.circle(screen, (0,0,0), (255,155), 10) ## правый зрачок
pygame.draw.rect(screen, (0,0,0), (120,245,160,40)) ## рот
pygame.draw.polygon(screen, (0,0,0), ((180,140), (180,120), (50,0), (50,20))) ## левая бров
pygame.draw.polygon(screen, (0,0,0), ((220,140), (220,120), (350,0), (350,20))) ## правая бров

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()