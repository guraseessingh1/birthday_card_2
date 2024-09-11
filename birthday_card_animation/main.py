import pygame
import time

pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("birthday greeting")
baloons = pygame.image.load("images/baloons.jpeg")
baloons = pygame.transform.scale(baloons,(WIDTH,HEIGHT))

while True:
    font = pygame.font.SysFont("Times New Roman",65)
    text_1 = font.render("HAPPY",True,(0,0,0))
    text_2 = font.render("BIRTHDAY",True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(baloons,(0,0))
    screen.blit(text_1,(210,180))
    screen.blit(text_2,(180,265))
    pygame.display.update()
    time.sleep(2)

    birthday_cake = pygame.image.load("images/cake.jpeg")
    screen.fill((255,255,255))
    screen.blit(birthday_cake,(0,0))
    pygame.display.update()
    time.sleep(2)

    glitter = pygame.image.load("images/glitter.jpeg")
    font2 = pygame.font.SysFont("Ariel",15)
    text_3 = font.render("wish you a bright future ahead",True,(0,255,0))
    screen.fill((255,255,255))
    screen.blit(glitter,(0,0))
    screen.blit(text_3,(10,30))
    pygame.display.update()
    time.sleep(2)


    

