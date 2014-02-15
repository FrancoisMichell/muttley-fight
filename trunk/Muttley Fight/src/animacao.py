# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import time
import pyganim
import classe_personagem
from time import sleep

player1 = ""
player2 = ""
TEXTCOLOR = (255, 255, 255)
def drawText(text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

def jogo():
    
    
    
    
    pygame.init()
    tela = pygame.display.set_mode((800,600),0,32)
    font = pygame.font.SysFont(None, 48)

    drawText('score:', font, tela, 10, 0)
    
    mainClock = pygame.time.Clock()
    
    #CARREGANDO IMAGENS
    
    fundo = pygame.image.load('imagens/fundos/fundoChesf.jpg').convert()
    
    #imagens player 1:
    
    paradoP1 = pyganim.PygAnimation([('imagensPastor/andandoPastor/1.png',0.1)])
    
    defesaP1 = pyganim.PygAnimation([('defesaMatheus.png',0.1)])
    
    chuteP1 = pyganim.PygAnimation([('imagensPastor/chute/chute1.png',0.1),
                                  ('imagensPastor/chute/chute2.png',0.1),
                                  ('imagensPastor/chute/chute3.png',0.1),
                                  ('imagensPastor/chute/chute4.png',0.1),
                                  ('imagensPastor/chute/chute5.png',0.1),
                                  ('imagensPastor/chute/chute6.png',0.1)], loop = False)
    
    socoP1 = pyganim.PygAnimation([('imagensPastor/soco/1.png',0.1),
                                  ('imagensPastor/soco/2.png',0.1),
                                  ('imagensPastor/soco/3.png',0.1),
                                  ('imagensPastor/soco/2.png',0.1),
                                  ('imagensPastor/soco/1.png',0.1)], loop = False)
    
    EsquerdaP1 = pyganim.PygAnimation([('imagensPastor/andandoPastor/6.png',0.12),
                                       ('imagensPastor/andandoPastor/5.png',0.12),
                                       ('imagensPastor/andandoPastor/4.png',0.12),
                                       ('imagensPastor/andandoPastor/3.png',0.12),
                                       ('imagensPastor/andandoPastor/2.png',0.12),
                                       ('imagensPastor/andandoPastor/1.png',0.12)])
    
    direitaP1 = pyganim.PygAnimation([('imagensPastor/andandoPastor/1.png',0.12),
                                      ('imagensPastor/andandoPastor/2.png',0.12),
                                      ('imagensPastor/andandoPastor/3.png',0.12),
                                      ('imagensPastor/andandoPastor/4.png',0.12),
                                      ('imagensPastor/andandoPastor/5.png',0.12),
                                      ('imagensPastor/andandoPastor/6.png',0.12)])
    
    #imagens jogador 2
    
    paradoP2 = pyganim.PygAnimation([('imagensMatheus/andando/1.png',0.1)])
    
    defesaP2 = pyganim.PygAnimation([('def.png',0.1)])
    
    chuteP2 = pyganim.PygAnimation([('imagensMatheus/chute/1.png',0.1),
                                    ('imagensMatheus/chute/2.png',0.1),
                                    ('imagensMatheus/chute/3.png',0.1),
                                    ('imagensMatheus/chute/2.png',0.1),
                                    ('imagensMatheus/chute/1.png',0.1)], loop = False)
    
    socoP2 = pyganim.PygAnimation([('imagensMatheus/soco/1.png',0.1),
                                  ('imagensMatheus/soco/2.png',0.1),
                                  ('imagensMatheus/soco/3.png',0.1),
                                  ('imagensMatheus/soco/2.png',0.1),
                                  ('imagensMatheus/soco/1.png',0.1)], loop = False)
    
    esquerdaP2 = pyganim.PygAnimation([('imagensMatheus/andando/1.png',0.12),
                                       ('imagensMatheus/andando/2.png',0.12),
                                       ('imagensMatheus/andando/3.png',0.12),
                                       ('imagensMatheus/andando/4.png',0.12)])
    
    direitaP2 = pyganim.PygAnimation([('imagensmatheus/andando/4.png',0.12),
                                      ('imagensMatheus/andando/3.png',0.12),
                                      ('imagensMatheus/andando/2.png',0.12),
                                      ('imagensMatheus/andando/1.png',0.12)])
    
    from classe_personagem import Personagem
    
    #===============================================================================
    # CRIANDO PERSONAGEM 1
    #===============================================================================
    x, y = 50,400
    jogador = classe_personagem.Personagem('pastor',x, y,0)
    jogador.rectIdle('pastor')
    
    direita1 = False
    esquerda1 = False
    chute1 = False
    defesa1 = False
    soco1 = False
    
    paradoP1.play()
    #===============================================================================
    # CRIANDO PERSONAGEM 2
    #===============================================================================
    _x, _y = 600, 400
    jogador2 = classe_personagem.Personagem('teste',_x, _y,0)
    jogador2.rectIdle('teste')
    
    direita2 = False
    esquerda2 = False
    chute2 = False
    defesa2 = False
    soco2 = False
    
    paradoP2.play()
            
    while True:
        
        #BLITANDO OS ELEMENTOS NO BUFF
    
        tela.blit(fundo, (0,0))
    #===============================================================================
    # BLITAR IMAGENS PLAYER 1
    #===============================================================================
        if(chuteP1._propGetElapsed()==0 and socoP1._propGetElapsed() == 0):
            
            EsquerdaP1.blit(tela, (jogador.getx(),jogador.gety()))
            direitaP1.blit(tela, (jogador.getx(),jogador.gety()))
            paradoP1.blit(tela, (jogador.getx(),jogador.gety()))
            defesaP1.blit(tela, (jogador.getx(),jogador.gety()))
        
        chuteP1.blit(tela,(x,y))
        socoP1.blit(tela, (x,y))
    #===============================================================================
    # BLITAR IMAGENS PLAYER 2
    #===============================================================================
        if(chuteP2._propGetElapsed()==0 and socoP2._propGetElapsed() == 0):
            
            esquerdaP2.blit(tela, (jogador2.getx(),jogador2.gety()))
            direitaP2.blit(tela, (jogador2.getx(),jogador2.gety()))
            paradoP2.blit(tela, (jogador2.getx(),jogador2.gety()))
            defesaP2.blit(tela, (jogador2.getx(),jogador2.gety()))
        
        chuteP2.blit(tela,(jogador2.getx(),jogador2.gety()))
        socoP2.blit(tela, (jogador2.getx(),jogador2.gety()))
    #==========================================================================
    # MOVIMENTOS
    #==========================================================================
        #VERIFICANDO EVENTOS
        for event in pygame.event.get():
            
            #SE APERTAR NA TECLA
            if event.type == KEYDOWN:
                
                # PLAYER 1
                if event.key == K_u:
                    chute1 = True
                    paradoP1.stop()
                    chuteP1.play()
                    jogador.rectChute() #RECUPERA A AREA DE COLISAO DO PERSONAGEM
                    paradoP1.play()
                
                if event.key == K_i:
                    soco1 = True
                    paradoP1.stop()
                    socoP1.play()
                    paradoP1.play()
                
                #PLAYER 2
                if event.key == K_c:
                    chute2 = True
                    paradoP2.stop()
                    chuteP2.play()
                    jogador2.rectChute() #RECUPERA A AREA DE COLISAO DO PERSONAGEM
                    paradoP2.play()
                
                if event.key == K_v:
                    soco2 = True
                    paradoP2.stop()
                    socoP2.play()
                    paradoP2.play()        
              
            #SE SOLTAR A TECLA     
            if event.type == KEYUP:
                
                #player 1
                if event.key == K_o:
                    defesaP1.stop()
                    defesa1 = False
                    paradoP1.play()
                
                if event.key == K_LEFT:
                    EsquerdaP1.stop()
                    esquerda1 = False
                    paradoP1.play()
                    
                if event.key == K_RIGHT:
                    direitaP1.stop()
                    direita1 = False
                    paradoP1.play()
                
                #player 2
                
                if event.key == K_b:
                    defesaP2.stop()
                    defesa2 = False
                    paradoP2.play()
                
                if event.key == K_a:
                    esquerdaP2.stop()
                    esquerda2 = False
                    paradoP2.play()
                    
                if event.key == K_d:
                    direitaP2.stop()
                    direita2 = False
                    paradoP2.play()
    
        teclaPressionada = pygame.key.get_pressed()
        # PLAYER 1
        if teclaPressionada[K_o]:
            defesa1 = True
            paradoP1.stop()
            defesaP1.play()
        
        if teclaPressionada[K_LEFT]:
            paradoP1.stop()
            esquerda1 = True
            EsquerdaP1.play()
            if defesa1 == False and chuteP1._propGetElapsed() == 0:
                if x > 0 :
                    x -= 5 
            jogador.setx(x)
            
        if teclaPressionada[K_RIGHT]:
            direita = True
            paradoP1.stop()
            direitaP1.play()
            if defesa1 == False and chuteP1._propGetElapsed() == 0:
                if x <= 700:
                    x += 5
            jogador.setx(x)
        
        # PLAYER 2
            
        if teclaPressionada[K_b]:
            defesa2 = True
            paradoP2.stop()
            defesaP2.play()
        
        if teclaPressionada[K_a]:
            paradoP2.stop()
            esquerdaP2.play()
            if _x > 0 :
                _x -= 5
            jogador2.setx(_x)
            
        if teclaPressionada[K_d]:
            paradoP2.stop()
            direitaP2.play()
            if _x <= 700:
                _x += 5
            jogador2.setx(_x)
        
    #===========================================================================
    # CONDICAO PARA OS CONTROLES 
    #===========================================================================
        # PLAYER 1         
        if direita1 == True and esquerda1 == True: #N�O DEIXA O BONECO IR A DIREITA E ESQUERDA AO MESMO TEMPO
            direitaP1.stop()
            EsquerdaP1.stop()
            paradoP1.play()
    
        if esquerda1 == True and chute1 == True: #NAO DEIXA O BONECO CHUTAR E IR A ESQUERDA AO MESMO TEMPO
            EsquerdaP1.stop()
            chuteP1.play()
            jogador.setx(x)
        
        if defesa1 == True:
            direitaP1.stop()
            EsquerdaP1.stop()
        
        # PLAYER 2
        
        if direita2 == True and esquerda2 == True: #N�O DEIXA O BONECO IR A DIREITA E ESQUERDA AO MESMO TEMPO
            direitaP2.stop()
            esquerdaP2.stop()
            paradoP2.play()
    
        if esquerda2 == True and chute2 == True: #NAO DEIXA O BONECO CHUTAR E IR A ESQUERDA AO MESMO TEMPO
            esquerdaP2.stop()
            chuteP2.play()
            jogador2.setx(_x)
        
        if defesa2 == True:
            direitaP2.stop()
            esquerdaP2.stop()
                 
    #==================================================================
    # COLISOES
    #==================================================================
        
        # PLAYER 1
        
        if jogador.rectChute().colliderect(jogador2.rect) and chute1 == True: #VERIFICA COLISAO DO CHUTE E RETIRA 2 PONTOS DE VIDA DO PERSONAGEM 2
            if defesa2:
                jogador2.perdeVida(1)
            else:
                jogador2.perdeVida(2)
            print jogador2.vida
            paradoP1.play()
            
        if jogador.rectChute() != jogador2.rect and chute1 == True: #SE NAO OCORRER COLISAO DO CHUTE
            chute1 = False
        
        if jogador.rectSoco().colliderect(jogador2.rect) and soco1 == True: #VERIFICA COLISAO DO SOCO E RETIRA 2 PONTOS DE VIDA DO PERSONAGEM 2
            if defesa2:
                jogador2.perdeVida(1)
            else:
                jogador2.perdeVida(2)
            paradoP1.play()
            print jogador2.vida
            
        if jogador.rectSoco() != jogador2.rect and soco1 == True: #SE NAO OCORRER COLISAO DO SOCO
            soco1 = False
    
        # PLAYER 2
        
        if jogador2.rectChute().colliderect(jogador.rect) and chute2 == True: #VERIFICA COLISAO DO CHUTE E RETIRA 2 PONTOS DE VIDA DO PERSONAGEM 2
            if defesa1:
                jogador.perdeVida(1)
            else:
                jogador.perdeVida(5)
            verificaMorte()
            print jogador.vida
            paradoP2.play()
            
        if jogador2.rectChute() != jogador.rect and chute2 == True: #SE NAO OCORRER COLISAO DO CHUTE
            chute2 = False
        
        if jogador2.rectSoco().colliderect(jogador.rect) and soco2 == True: #VERIFICA COLISAO DO SOCO E RETIRA 2 PONTOS DE VIDA DO PERSONAGEM 2
            if defesa1:
                jogador.perdeVida(1)
            else:
                jogador.perdeVida(5)
            verificaMorte()
            paradoP2.play()
            print jogador.vida
            
        if jogador2.rectSoco() != jogador.rect and soco2 == True: #SE NAO OCORRER COLISAO DO SOCO
            soco2 = False
    
        #=======================================================================
        # VERIFICA MORTE
        #=======================================================================
        def verificaMorte():
            if jogador.vida == 0:
                print "jogador 2 wins!!"
            elif jogador2.vida == 0:
                print "jogador 1 wins!!"
    
        pygame.display.update()
        mainClock.tick(30)
