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

#CARREGANDO IMAGENS

fundo = pygame.image.load('imagens/fundos/fundoChesf.jpg').convert()

stoped = pygame.image.load('gameimages/crono_back.gif')

parado1 = pyganim.PygAnimation([('andandoPastor/1.png',0.1)])

parado2 = pyganim.PygAnimation([('gameimages/crono_back.gif',0.1)])

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

chronoDireita1 = pyganim.PygAnimation([('andandoPastor/1.png',0.12),
                                ('andandoPastor/2.png',0.12),
                                ('andandoPastor/3.png',0.12),
                                ('andandoPastor/4.png',0.12),
                                ('andandoPastor/5.png',0.12),
                                ('andandoPastor/6.png',0.12)])

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


#CRIANDO OBJETO PERSONAGEM 1 E 2

from classe_personagem import Personagem

x, y = 50,400
_x, _y = 600, 400

jogador = classe_personagem.Personagem('pastor',x, y,0)
jogador2 = classe_personagem.Personagem('teste',_x, _y,0)

jogador.rectIdle('pastor')
jogador2.rectIdle('teste')

direita = False
esquerda = False
chute1 = False


#PRINTANDO A ANIMAÇÃO DO BONECO PARADO

parado1.play()
parado2.play()
    

while True:
        
    #BLITANDO OS ELEMENTOS NO BUFF
    
    tela.blit(fundo, (0,0))
    
    chronoEsquerda1.blit(tela, (jogador.getx(),jogador.gety()))
    chronoDireita1.blit(tela, (jogador.getx(),jogador.gety()))

    chronoEsquerda2.blit(tela, (jogador2.getx(),jogador2.gety()))
    chronoDireita2.blit(tela, (jogador2.getx(),jogador2.gety()))

    parado1.blit(tela, (jogador.getx(),jogador.gety()))
    parado2.blit(tela, (jogador2.getx(),jogador2.gety()))

    chute.blit(tela,(x,y))
    
    #VERIFICANDO EVENTOS
    for event in pygame.event.get():
        
        #SE APERTAR NA TECLA
        if event.type == KEYDOWN:
            
            if event.key == K_e:
                chute1 = True
                parado1.stop()
                chute.play()
                jogador.rectChute() #RECUPERA A AREA DE COLISAO DO PERSONAGEM
                parado1.play()
        #SE SOLTAR A TECLA     
        if event.type == KEYUP:

            if event.key == K_LEFT:
                chronoEsquerda1.stop()
                esquerda = False
                parado1.play()
                
            if event.key == K_RIGHT:
                chronoDireita1.stop()
                direita = False
                parado1.play()

            if event.key == K_a:
                chronoEsquerda2.stop()
                esquerda = False
                
            if event.key == K_d:
                chronoDireita2.stop()
                direita = False

    teclaPressionada = pygame.key.get_pressed()
    

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

    if direita == True and esquerda == True: #NÃO DEIXA O BONECO IR A DIREITA E ESQUERDA AO MESMO TEMPO
        chronoDireita1.stop()
        chronoEsquerda1.stop()
        parado1.play()

    if esquerda == True and chute1 == True: #NAO DEIXA O BONECO CHUTAR E IR A ESQUERDA AO MESMO TEMPO
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
             
    if jogador.rectChute().colliderect(jogador2.rect) and chute1 == True: #VERIFICA COLISAO DO CHUTE E RETIRA 2 PONTOS DE VIDA DO PERSONAGEM 2
        jogador2.perdeVida(2)
        parado1.play()
        
    if jogador.rectChute() != jogador2.rect and chute1 == True: #SE NAO OCORRER COLISAO DO CHUTE
        chute1 = False
    
    
    
    pygame.display.update()
    mainClock.tick(30)
