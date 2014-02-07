import pygame
from pygame.locals import *
import sys
import time
import pyganim
import classe_personagem
from time import sleep

pygame.init()
tela = pygame.display.set_mode((800,600),0,32)

mainClock = pygame.time.Clock()

fundo = pygame.image.load('imagens/fundos/fundoChesf.jpg').convert()

stoped = pygame.image.load('gameimages/crono_back.gif')

parado1 = pyganim.PygAnimation([('imagens/semTitulo.png',0.1)])

parado2 = pyganim.PygAnimation([('gameimages/crono_back.gif',0.1)])

chronoEsquerda = pyganim.PygAnimation([('imagens/mutt1.gif',0.1),
                                       ('imagens/mutt2.gif',0.1),
                                       ('imagens/mutt3.gif',0.1),
                                       ('imagens/mutt3.gif',0.1),
                                       ('imagens/mutt2.gif',0.1),
                                       ('imagens/mutt1.gif',0.1)])

chute = pyganim.PygAnimation([('chute/chute1.png',0.1),
                              ('chute/chute2.png',0.1),
                              ('chute/chute3.png',0.1),
                              ('chute/chute4.png',0.1),
                              ('chute/chute5.png',0.1),
                              ('chute/chute6.png',0.1)], loop = False)
pasta = 'esquerda'

chronoEsquerda1 = pyganim.PygAnimation([('%s/crono_left_run.000.gif'%(pasta),0.1),
                                       ('%s/crono_left_run.001.gif'%(pasta),0.1),
                                       ('%s/crono_left_run.002.gif'%(pasta),0.1),
                                       ('%s/crono_left_run.003.gif'%(pasta),0.1),
                                       ('%s/crono_left_run.004.gif'%(pasta),0.1),
                                       ('%s/crono_left_run.005.gif'%(pasta),0.1)])

chronoDireita1 = pyganim.PygAnimation([('direita/crono_right_run.000.gif',0.1),
                                       ('direita/crono_right_run.001.gif',0.1),
                                       ('direita/crono_right_run.002.gif',0.1),
                                       ('direita/crono_right_run.003.gif',0.1),
                                       ('direita/crono_right_run.004.gif',0.1),
                                       ('direita/crono_right_run.005.gif',0.1)])

chronoEsquerda2 = pyganim.PygAnimation([('esquerda/crono_left_run.000.gif',0.1),
                                       ('esquerda/crono_left_run.001.gif',0.1),
                                       ('esquerda/crono_left_run.002.gif',0.1),
                                       ('esquerda/crono_left_run.003.gif',0.1),
                                       ('esquerda/crono_left_run.004.gif',0.1),
                                       ('esquerda/crono_left_run.005.gif',0.1)])

chronoDireita2 = pyganim.PygAnimation([('direita/crono_right_run.000.gif',0.1),
                                       ('direita/crono_right_run.001.gif',0.1),
                                       ('direita/crono_right_run.002.gif',0.1),
                                       ('direita/crono_right_run.003.gif',0.1),
                                       ('direita/crono_right_run.004.gif',0.1),
                                       ('direita/crono_right_run.005.gif',0.1)])

parado1.play()
parado2.play()

x = 200

from classe_personagem import Personagem

x, y = 50,400
_x, _y = 600, 400

jogador = classe_personagem.Personagem(x, y)
jogador2 = classe_personagem.Personagem(_x, _y)

acao = False
direita = False
esquerda = False
chute1 = False

while True:
    
    movimentaCima = False    
    
    tela.blit(fundo, (0,0))
    
    chronoEsquerda1.blit(tela, (jogador.getx(),jogador.gety()))
    chronoDireita1.blit(tela, (jogador.getx(),jogador.gety()))

    chronoEsquerda2.blit(tela, (jogador2.getx(),jogador2.gety()))
    chronoDireita2.blit(tela, (jogador2.getx(),jogador2.gety()))

    parado1.blit(tela, (jogador.getx(),jogador.gety()))
    parado2.blit(tela, (jogador2.getx(),jogador2.gety()))

    chute.blit(tela,(x,y))

    for event in pygame.event.get():
        
        if event.type == KEYDOWN:
            
            if event.key == K_e:
                chute1 = True
                parado1.stop()
                chute.play()

        if event.type == KEYUP:

            if event.key == K_LEFT:
                chronoEsquerda1.stop()
                esquerda = False
                
            if event.key == K_RIGHT:
                chronoDireita1.stop()
                direita = False

            if event.key == K_a:
                chronoEsquerda2.stop()
                esquerda = False
                
            if event.key == K_d:
                chronoDireita2.stop()
                direita = False

    teclaPressionada = pygame.key.get_pressed()
    
    parado1.play()
    parado2.play()
    
    if teclaPressionada[K_LEFT]:
        
        parado1.stop()
        esquerda = True
        chronoEsquerda1.play()
        if x > 0 :
            x -= 5
        jogador.setx(x)
        
    if teclaPressionada[K_RIGHT]:
        direita = True
        parado1.stop()
        chronoDireita1.play()
        if x <= 700:
            x += 5
        jogador.setx(x)

    if direita == True and esquerda == True:
        chronoDireita1.stop()
        chronoEsquerda1.stop()
        parado1.play()

    if esquerda == True and chute1 == True:
        chronoEsquerda1.stop()
        chute.play()
        jogador.setx(x)
    
    if teclaPressionada[K_a]:
        parado2.stop()
        chronoEsquerda2.play()
        if _x > 0 :
            _x -= 5
        jogador2.setx(_x)
        
    if teclaPressionada[K_d]:
        parado2.stop()
        chronoDireita2.play()
        if _x <= 700:
            _x += 5
        jogador2.setx(_x)
    
    pygame.display.update()
    mainClock.tick(30)
