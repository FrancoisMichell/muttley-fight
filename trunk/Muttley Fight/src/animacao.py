import pygame
from pygame.locals import *
import sys
import time
import pyganim

pygame.init()
tela = pygame.display.set_mode((800,600),0,32)

mainClock = pygame.time.Clock()

fundo = pygame.image.load("imagens/fundos/fundoPreto.png").convert()

chronoEsquerda = pyganim.PygAnimation([('gameimages/crono_back_run.000.gif',0.1),
                                       ('gameimages/crono_back_run.001.gif',0.1),
                                       ('gameimages/crono_back_run.002.gif',0.1),
                                       ('gameimages/crono_back_run.003.gif',0.1),
                                       ('gameimages/crono_back_run.004.gif',0.1),
                                       ('gameimages/crono_back_run.005.gif',0.1)])

chronoDireita = pyganim.PygAnimation([('gameimages/crono_back_walk.000.gif',0.1),
                                       ('gameimages/crono_back_walk.001.gif',0.1),
                                       ('gameimages/crono_back_walk.002.gif',0.1),
                                       ('gameimages/crono_back_walk.003.gif',0.1),
                                       ('gameimages/crono_back_walk.004.gif',0.1),
                                       ('gameimages/crono_back_walk.005.gif',0.1)])


while True:
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                chronoEsquerda.play()
            elif event.key == K_b:
                chronoDireita.play()
        
        if event.type == KEYUP:
            if event.key == K_b:
                chronoDireita.stop()
            elif event.key == K_a:
                chronoEsquerda.stop()
                
            
            
    
    tela.blit(fundo,(0,0))
    chronoEsquerda.blit(tela, (400,200))
    chronoDireita.blit(tela, (300,200))
    
    pygame.display.update()
    mainClock.tick(30)