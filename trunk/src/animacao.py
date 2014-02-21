# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import time
import pyganim
import classe_personagem
from time import sleep
import menuPrincipal

player1 = ""
player2 = ""
fundo = ""

def jogo():
    
    pygame.init()
    tela = pygame.display.set_mode((800,600),0,32)
    print player1
    mainClock = pygame.time.Clock()
    
    #imagens player 1:

    idleP1 = pyganim.PygAnimation([('imagens/player1/imagens%s/idle/1.png'%(player1),0.1),
                                   ('imagens/player1/imagens%s/idle/2.png'%(player1),0.1),
                                   ('imagens/player1/imagens%s/idle/3.png'%(player1),0.1),
                                   ('imagens/player1/imagens%s/idle/4.png'%(player1),0.1),
                                   ('imagens/player1/imagens%s/idle/5.png'%(player1),0.1),
                                   ('imagens/player1/imagens%s/idle/6.png'%(player1),0.1),
                                   ('imagens/player1/imagens%s/idle/7.png'%(player1),0.1)])
    
    defesaP1 = pyganim.PygAnimation([('imagens/player1/imagens%s/defesa.png'%(player1),0.1)])
    
    chuteP1 = pyganim.PygAnimation([('imagens/player1/imagens%s/chute/1.png'%(player1),0.1),
                                  ('imagens/player1/imagens%s/chute/2.png'%(player1),0.1),
                                  ('imagens/player1/imagens%s/chute/3.png'%(player1),0.1),
                                  ('imagens/player1/imagens%s/chute/4.png'%(player1),0.1),
                                  ('imagens/player1/imagens%s/chute/5.png'%(player1),0.1),
                                  ('imagens/player1/imagens%s/chute/6.png'%(player1),0.1)], loop = False)
    
    socoP1 = pyganim.PygAnimation([('imagens/player1/imagens%s/soco/1.png'%(player1),0.1),
                                  ('imagens/player1/imagens%s/soco/2.png'%(player1),0.1),
                                  ('imagens/player1/imagens%s/soco/3.png'%(player1),0.1),
                                  ('imagens/player1/imagens%s/soco/2.png'%(player1),0.1),
                                  ('imagens/player1/imagens%s/soco/1.png'%(player1),0.1)], loop = False)
    
    esquerdaP1 = pyganim.PygAnimation([('imagens/player1/imagens%s/andando/6.png'%(player1),0.12),
                                       ('imagens/player1/imagens%s/andando/5.png'%(player1),0.12),
                                       ('imagens/player1/imagens%s/andando/4.png'%(player1),0.12),
                                       ('imagens/player1/imagens%s/andando/3.png'%(player1),0.12),
                                       ('imagens/player1/imagens%s/andando/2.png'%(player1),0.12),
                                       ('imagens/player1/imagens%s/andando/1.png'%(player1),0.12)])
    
    direitaP1 = pyganim.PygAnimation([('imagens/player1/imagens%s/andando/1.png'%(player1),0.12),
                                      ('imagens/player1/imagens%s/andando/2.png'%(player1),0.12),
                                      ('imagens/player1/imagens%s/andando/3.png'%(player1),0.12),
                                      ('imagens/player1/imagens%s/andando/4.png'%(player1),0.12),
                                      ('imagens/player1/imagens%s/andando/5.png'%(player1),0.12),
                                      ('imagens/player1/imagens%s/andando/6.png'%(player1),0.12)])
           
    morreuP1 = pyganim.PygAnimation([("imagens/player1/imagens%s/morte/1.png"%(player1), 0.1),
                                   ("imagens/player1/imagens%s/morte/2.png"%(player1), 0.1),
                                   ("imagens/player1/imagens%s/morte/3.png"%(player1), 0.1),
                                   ("imagens/player1/imagens%s/morte/4.png"%(player1), 0.1),
                                   ("imagens/player1/imagens%s/morte/5.png"%(player1), 0.1)],loop = False)
    
    
    #Audios 
    pygame.mixer.init()
    DefesaSom = pygame.mixer.Sound('Audios/SonsGerais/Defesa.wav')
    DanoSom = pygame.mixer.Sound('Audios/SonsGerais/SocoChute.wav')
    lutaSom = pygame.mixer.Sound('Audios/SonsGerais/InicioLuta.wav')
    somCombate = pygame.mixer.Sound("Audios/SonsGerais/musicacombate.wav")
    errou = pygame.mixer.Sound("Audios/SonsGerais/socoerrou.wav")
    
    #Audios P1
    levando1 = pygame.mixer.Sound("Audios/%saudio/levandoSoco.wav"%(player1))
    
    
    #Audios P2
    levando2 = pygame.mixer.Sound("Audios/%saudio/levandoSoco.wav"%(player2))
    
    
    #imagens jogador 2
    
    idleP2 = pyganim.PygAnimation([('imagens/player2/imagens%s/idle/1.png'%(player2),0.1),
                                   ('imagens/player2/imagens%s/idle/2.png'%(player2),0.1),
                                   ('imagens/player2/imagens%s/idle/3.png'%(player2),0.1),
                                   ('imagens/player2/imagens%s/idle/4.png'%(player2),0.1),
                                   ('imagens/player2/imagens%s/idle/5.png'%(player2),0.1),
                                   ('imagens/player2/imagens%s/idle/6.png'%(player2),0.1),
                                   ('imagens/player2/imagens%s/idle/7.png'%(player2),0.1)])
    
    
    defesaP2 = pyganim.PygAnimation([('imagens/player2/imagens%s/defesa.png'%(player2),0.1)])
    
    chuteP2 = pyganim.PygAnimation([('imagens/player2/imagens%s/chute/1.png'%(player2),0.1),
                                  ('imagens/player2/imagens%s/chute/2.png'%(player2),0.1),
                                  ('imagens/player2/imagens%s/chute/3.png'%(player2),0.1),
                                  ('imagens/player2/imagens%s/chute/4.png'%(player2),0.1),
                                  ('imagens/player2/imagens%s/chute/5.png'%(player2),0.1),
                                  ('imagens/player2/imagens%s/chute/6.png'%(player2),0.1)], loop = False)
    
    socoP2 = pyganim.PygAnimation([('imagens/player2/imagens%s/soco/1.png'%(player2),0.1),
                                  ('imagens/player2/imagens%s/soco/2.png'%(player2),0.1),
                                  ('imagens/player2/imagens%s/soco/3.png'%(player2),0.1),
                                  ('imagens/player2/imagens%s/soco/2.png'%(player2),0.1),
                                  ('imagens/player2/imagens%s/soco/1.png'%(player2),0.1)], loop = False)
    
    esquerdaP2 = pyganim.PygAnimation([('imagens/player2/imagens%s/andando/1.png'%(player2),0.12),
                                       ('imagens/player2/imagens%s/andando/2.png'%(player2),0.12),
                                       ('imagens/player2/imagens%s/andando/3.png'%(player2),0.12),
                                       ('imagens/player2/imagens%s/andando/4.png'%(player2),0.12),
                                       ('imagens/player2/imagens%s/andando/5.png'%(player2),0.12),
                                       ('imagens/player2/imagens%s/andando/6.png'%(player2),0.12)])
    
    direitaP2 = pyganim.PygAnimation([('imagens/player2/imagens%s/andando/6.png'%(player2),0.12),
                                      ('imagens/player2/imagens%s/andando/5.png'%(player2),0.12),
                                      ('imagens/player2/imagens%s/andando/4.png'%(player2),0.12),
                                      ('imagens/player2/imagens%s/andando/3.png'%(player2),0.12),
                                      ('imagens/player2/imagens%s/andando/2.png'%(player2),0.12),
                                      ('imagens/player2/imagens%s/andando/1.png'%(player2),0.12)])
       
    morreuP2 = pyganim.PygAnimation([("imagens/player2/imagens%s/morte/1.png"%(player2), 0.1),
                                   ("imagens/player2/imagens%s/morte/2.png"%(player2), 0.1),
                                   ("imagens/player2/imagens%s/morte/3.png"%(player2), 0.1),
                                   ("imagens/player2/imagens%s/morte/4.png"%(player2), 0.1),
                                   ("imagens/player2/imagens%s/morte/5.png"%(player2), 0.1)],loop = False)    
    
    
    
    from classe_personagem import Personagem
    
    #===============================================================================
    # CRIANDO PERSONAGEM 1
    #===============================================================================
    
    if player1 == "Matheus" or player1 == "Igor" or player1 == "Lucas":
        x, y = 50,370
    elif player1 == "Tulio":
        x, y = 50,380
    else:
        x, y = 50,400
    jogador = classe_personagem.Personagem(player1,x, y,0)
    jogador.rectIdle()
    
    chute1 = False
    defesa1 = False
    soco1 = False
    
    idleP1.play()
    
    #===============================================================================
    # CRIANDO PERSONAGEM 2
    #===============================================================================
    
    if player2 == "Matheus" or player2 == "Igor" or player2 == "Lucas":
        _x, _y = 600,370
    elif player2 == "Tulio":
        _x,_y = 600,380
    else:
        _x, _y = 600,400
    jogador2 = classe_personagem.Personagem(player2,_x, _y,0)
    jogador2.rectIdle()

    chute2 = False
    defesa2 = False
    soco2 = False
    
    idleP2.play()
              
    sair = False        
    
    aux = 0
    
    somCombate.play()
    
    sleep(0.2)
    lutaSom.play()
    
    while sair != True:
        
        #BLITANDO OS ELEMENTOS NO BUFF
    
        tela.blit(fundo, (0,0))
        
        #=======================================================================
        # BARRA DE HP
        #=======================================================================
        
        hp = pygame.image.load("imagens/life.png")
        
        for i in range(jogador.vida/2):
            tela.blit(hp,((20+i*5),100))
        
        for i in range(jogador2.vida/2):
            tela.blit(hp,((780-i*5),100))    
            
        #===============================================================================
        # BLITAR IMAGENS PLAYER 1
        #===============================================================================
        if(chuteP1._propGetElapsed()==0 and socoP1._propGetElapsed() == 0):
            
            esquerdaP1.blit(tela, (jogador.getx(),jogador.gety()))
            direitaP1.blit(tela, (jogador.getx(),jogador.gety()))
            idleP1.blit(tela, (jogador.getx(),jogador.gety()))
            defesaP1.blit(tela, (jogador.getx(),jogador.gety()))
        
        chuteP1.blit(tela,(x,y))
        socoP1.blit(tela, (x,y))
        morreuP1.blit(tela, (jogador.getx(),jogador.gety()))
        #===============================================================================
        # BLITAR IMAGENS PLAYER 2
        #===============================================================================
        if(chuteP2._propGetElapsed()==0 and socoP2._propGetElapsed() == 0):
            
            defesaP2.blit(tela, (jogador2.getx(),jogador2.gety()))
            esquerdaP2.blit(tela, (jogador2.getx(),jogador2.gety()))
            direitaP2.blit(tela, (jogador2.getx(),jogador2.gety()))
            idleP2.blit(tela, (jogador2.getx(),jogador2.gety()))
        
        
        chuteP2.blit(tela,(jogador2.getx(),jogador2.gety()))
        socoP2.blit(tela, (jogador2.getx(),jogador2.gety()))
        
        morreuP2.blit(tela, (jogador2.getx(),jogador2.gety()))
    #==========================================================================
    # MOVIMENTOS
    #==========================================================================
        #VERIFICANDO EVENTOS
        for event in pygame.event.get():
            
            #SE APERTAR NA TECLA
            if event.type == KEYDOWN:
                
                # PLAYER 1
                if event.key == K_c and chuteP1._propGetElapsed() == 0 and socoP1._propGetElapsed() == 0:
                    chute1 = True
                    
                    idleP1.stop()
                    chuteP1.play()
                    jogador.rectChute() #RECUPERA A AREA DE COLISAO DO PERSONAGEM
                    idleP1.play()
                
                if event.key == K_v and socoP1._propGetElapsed() == 0 and chuteP1._propGetElapsed() == 0:
                    soco1 = True
                    
                    idleP1.stop()
                    socoP1.play()
                    idleP1.play()
                
                #PLAYER 2
                if event.key == K_u and chuteP2._propGetElapsed() == 0 and socoP2._propGetElapsed() == 0:
                    chute2 = True
                    
                    idleP2.stop()
                    chuteP2.play()
                    jogador2.rectChute() #RECUPERA A AREA DE COLISAO DO PERSONAGEM
                    idleP2.play()
                
                if event.key == K_i and socoP2._propGetElapsed() == 0 and chuteP2._propGetElapsed() == 0:
                    soco2 = True
                    
                    idleP2.stop()
                    socoP2.play()
                    idleP2.play()        
        
        # SE SEGURAR NA TECLA
              
        teclaPressionada = pygame.key.get_pressed()
        # PLAYER 1
        if teclaPressionada[K_b]:
            defesa1 = True
            idleP1.stop()
            defesaP1.play()
        
        if teclaPressionada[K_a]:
            if defesa1 == False and chuteP1._propGetElapsed() == 0 and socoP1._propGetElapsed() == 0:
                idleP1.stop()
                esquerdaP1.play()
                if x > 0 :
                    x -= 5 
                jogador.setx(x)
            
        if teclaPressionada[K_d]:
            if defesa1 == False and chuteP1._propGetElapsed() == 0 and socoP1._propGetElapsed() == 0:
                idleP1.stop()
                direitaP1.play()
                if x <= 700:
                    x += 5
            jogador.setx(x)
            
        if teclaPressionada[K_a] and teclaPressionada[K_d]:
            esquerdaP1.stop()
            direitaP1.stop()
            idleP1.play()
        
        # PLAYER 2
            
        if teclaPressionada[K_o]:
            defesa2 = True
            idleP2.stop()
            defesaP2.play()
        
        if teclaPressionada[K_LEFT]:
            if defesa2 == False and chuteP2._propGetElapsed() == 0 and socoP2._propGetElapsed() == 0:
                idleP2.stop()
                esquerdaP2.play()
                if _x > 0 :
                    _x -= 5
            jogador2.setx(_x)
            
        if teclaPressionada[K_RIGHT]:
            if defesa2 == False and chuteP2._propGetElapsed() == 0 and socoP2._propGetElapsed() == 0:
                idleP2.stop()
                direitaP2.play()
                if _x <= 700:
                    _x += 5
            jogador2.setx(_x)
        
        if teclaPressionada[K_LEFT] and teclaPressionada[K_RIGHT]:
            esquerdaP2.stop()
            direitaP2.stop()
            idleP2.play()
            
            #SE SOLTAR A TECLA
                 
        if event.type == KEYUP:
            
            #player 1
            if event.key == K_b:
                defesaP1.stop()
                defesa1 = False
                idleP1.play()
            
            if event.key == K_a:
                esquerdaP1.stop()
                defesaP1.stop()
                idleP1.play()
                
            if event.key == K_d:
                direitaP1.stop()
                defesaP1.stop()
                idleP1.play()
            
            #player 2
            
            if event.key == K_o:
                defesaP2.stop()
                defesa2 = False
                idleP2.play()
            
            if event.key == K_LEFT:
                esquerdaP2.stop()
                defesaP2.stop()
                idleP2.play()
                
            if event.key == K_RIGHT:
                direitaP2.stop()
                defesaP2.stop()
                idleP2.play()

    #==================================================================
    # COLISOES
    #==================================================================
        
        # PLAYER 1
        
        if jogador.rectChute().colliderect(jogador2.rect) and chute1: #VERIFICA COLISAO DO CHUTE E RETIRA 2 PONTOS DE VIDA DO PERSONAGEM 2
            if defesa2:
                jogador2.perdeVida(1)
                DefesaSom.play()
            else:
                levando2.play()
                jogador2.perdeVida(2)
                DanoSom.play()
            idleP1.play()
            
        if jogador.rectChute() != jogador2.rect and chute1: #SE NAO OCORRER COLISAO DO CHUTE
            chute1 = False
            errou.play()
        
        if jogador.rectSoco().colliderect(jogador2.rect) and soco1: #VERIFICA COLISAO DO SOCO E RETIRA 2 PONTOS DE VIDA DO PERSONAGEM 2
            if defesa2:
                jogador2.perdeVida(1)
                DefesaSom.play()
            else:
                levando2.play()
                jogador2.perdeVida(50)
                DanoSom.play()
            idleP1.play()
            
        if jogador.rectSoco() != jogador2.rect and soco1: #SE NAO OCORRER COLISAO DO SOCO
            soco1 = False
            errou.play()
    
        # PLAYER 2
        
        if jogador2.rectChute().colliderect(jogador.rect) and chute2: #VERIFICA COLISAO DO CHUTE E RETIRA 2 PONTOS DE VIDA DO PERSONAGEM 2
            if defesa1:
                jogador.perdeVida(1)
                DefesaSom.play()
            else:
                levando1.play()
                jogador.perdeVida(5)
                DanoSom.play()
            idleP2.play()
            
        if jogador2.rectChute() != jogador.rect and chute2: #SE NAO OCORRER COLISAO DO CHUTE
            chute2 = False
            errou.play()
        
        if jogador2.rectSoco().colliderect(jogador.rect) and soco2: #VERIFICA COLISAO DO SOCO E RETIRA 2 PONTOS DE VIDA DO PERSONAGEM 2
            if defesa1:
                jogador.perdeVida(1)
                DefesaSom.play()
            else:
                levando1.play()
                jogador.perdeVida(5)
                DanoSom.play()
            idleP2.play()
            
        if jogador2.rectSoco() != jogador.rect and soco2: #SE NAO OCORRER COLISAO DO SOCO
            soco2 = False
            errou.play()
 
        pygame.display.update()
        mainClock.tick(30)
        
        #=======================================================================
        # VERIFICA MORTE
        #=======================================================================
        if jogador.vida <= 0:
            somCombate.stop()
            idleP1.stop()
            morreuP1.play()
            aux += morreuP1.currentFrameNum
            if aux == 30:
                sleep(0.5)
                sair = True
                menuPrincipal.telaGanhou('player2')
        elif jogador2.vida <= 0:
            idleP2.stop()
            morreuP2.play()
            aux += morreuP2.currentFrameNum
            if aux == 30:
                somCombate.stop()    
                sair = True
                menuPrincipal.telaGanhou('player1')
            
            