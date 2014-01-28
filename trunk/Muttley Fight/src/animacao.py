import pygame
from pygame.locals import *
import sys
import time
import pyganim

pygame.init()
tela = pygame.display.set_mode((800,600),0,32)

mainClock = pygame.time.Clock()

fundo = pygame.image.load('imagens/fundo3.jpg').convert()

parado = pyganim.PygAnimation([('gameimages/crono_back.gif',0.1)])

chronoEsquerda = pyganim.PygAnimation([('imagens/mutt1.gif',0.1),
                                       ('imagens/mutt2.gif',0.1),
                                       ('imagens/mutt3.gif',0.1),
                                       ('imagens/mutt3.gif',0.1),
                                       ('imagens/mutt2.gif',0.1),
                                       ('imagens/mutt1.gif',0.1)])

chronoDireita = pyganim.PygAnimation([('gameimages/crono_back_walk.000.gif',0.1),
                                       ('gameimages/crono_back_walk.001.gif',0.1),
                                       ('gameimages/crono_back_walk.002.gif',0.1),
                                       ('gameimages/crono_back_walk.003.gif',0.1),
                                       ('gameimages/crono_back_walk.004.gif',0.1),
                                       ('gameimages/crono_back_walk.005.gif',0.1)])


parado.play()

y = 200

while True:
    
    movimentaCima = False    
    
    tela.blit(fundo, (0,0))
    
    parado.blit(tela, (400,y))
    chronoEsquerda.blit(tela, (400,y))
    chronoDireita.blit(tela, (400,y))
    
    
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            movimentaCima = True
            if event.key == K_a:
                parado.stop()
                chronoEsquerda.play()
            elif event.key == K_b:
                parado.stop()
                chronoDireita.play()
            if movimentaCima == True:
                print "mopa"
        
        if event.type == KEYUP:
            if event.key == K_b:
                chronoDireita.stop()
                parado.play()
            elif event.key == K_a:
                chronoEsquerda.stop()
                parado.play()
    
    pygame.display.update()
    mainClock.tick(30)