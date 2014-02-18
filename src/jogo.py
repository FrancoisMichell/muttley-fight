'''
Created on 31/01/2014

@author: françois
'''
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
    
    
    
    #===============================================================================
    # MOVIMENTOS PLAYER 2:
    #===============================================================================
    #VERIFICANDO EVENTOS
        for event in pygame.event.get():
            
            #SE APERTAR NA TECLA
            if event.type == KEYDOWN:
                
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
    #===========================================================================
    # COLISAO PLAYER 2
    #===========================================================================
        if jogador.rectChute().colliderect(jogador2.rect) and chute1 == True: #VERIFICA COLISAO DO CHUTE E RETIRA 2 PONTOS DE VIDA DO PERSONAGEM 2
            jogador2.perdeVida(2)
            paradoP1.play()
            
        if jogador.rectChute() != jogador2.rect and chute1 == True: #SE NAO OCORRER COLISAO DO CHUTE
            chute1 = False
    
        pygame.display.update()
        mainClock.tick(30)