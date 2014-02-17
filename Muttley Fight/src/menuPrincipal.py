import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from FixTk import ver
import animacao
largura, altura = 800,600

pygame.init()

screen = pygame.display.set_mode((largura,altura),0,32)
pygame.display.set_caption  ("Muttley Fight")

fundo = pygame.image.load('imagens/fundos/inicio_Jogo.png')
botaoVoltar = pygame.image.load("imagens/botoes/voltar.png").convert_alpha()

def verificaMouse(img_botao,pos_botao,pos_mouse):
    img_x, img_y = pos_botao 
    img_w, img_h = img_botao.get_size() 
    varia_x = img_x + img_w 
    varia_y = img_y + img_h 
    if pos_mouse[0] > img_x and pos_mouse[0] < varia_x and pos_mouse[1] > img_y and pos_mouse[1] < varia_y: 
        return True
    return False

def Instrucoes():
    
    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    
        xy = pygame.mouse.get_pos() #Recupera a posicao do mouse

        screen.blit(fundo,(0,0))
        screen.blit(botaoVoltar,(40,523))
        
        if verificaMouse(botaoVoltar,(30,505),xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                MenuInicial()
         
        pygame.display.flip()

def Creditos():
    
    
    fundoCreditos = pygame.image.load("imagens/fundos/creditos.png")
    posBotaoVoltar = (41,525)
    
    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    
        xy = pygame.mouse.get_pos() #Recupera a posicao do mouse

        screen.blit(fundoCreditos,(0,0))
        screen.blit(botaoVoltar,posBotaoVoltar)


        
        if verificaMouse(botaoVoltar,posBotaoVoltar,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                MenuInicial()
         
        pygame.display.update()

def Cenarios():
    
    
    botaoIniciar = pygame.image.load("imagens/botoes/iniciar.png").convert_alpha()
    fundoCenarios = pygame.image.load("imagens/fundos/cenario.png").convert_alpha()
    botaoSeguinte = pygame.image.load('imagens/botoes/setaDireita.png').convert_alpha()
    botaoAnterior = pygame.image.load('imagens/botoes/setaEsquerda.png').convert_alpha()
    
    cenario1 = pygame.image.load('imagens/fundos/imagemfundo1.jpg').convert_alpha()
    cenario2 = pygame.image.load('imagens/fundos/imagemfundo2.jpg').convert_alpha()
    cenario3 = pygame.image.load('imagens/fundos/imagemChesf.jpg').convert_alpha()
    
    posBotaoIniciar = (651,525)
    posBotaoVoltar = (39,525)
    
    cont = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        xy = pygame.mouse.get_pos()
        
        screen.blit(fundoCenarios,(0,0))
        screen.blit(botaoIniciar, posBotaoIniciar)
        screen.blit(botaoVoltar, posBotaoVoltar)
        screen.blit(botaoSeguinte,(705,280))
        screen.blit(botaoAnterior,(20,280))
            
        if cont == 0:
            screen.blit(cenario1,(112,151))
            if verificaMouse(botaoSeguinte,(705,280),xy) == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cont += 1
                    sleep(0.5)
            elif verificaMouse(botaoAnterior,(20,280),xy) == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cont = 2
                    sleep(0.5)
        else:
            if cont == 1:
                screen.blit(cenario2,(112,151))
                if verificaMouse(botaoSeguinte,(705,280),xy) == True:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        cont += 1
                        sleep(0.5)
                if verificaMouse(botaoAnterior,(20,280),xy) == True:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        cont -= 1
                        sleep(0.5)
            else:
                if cont == 2:
                    screen.blit(cenario3,(112,151))
                    if verificaMouse(botaoSeguinte,(705,280),xy) == True:
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            cont = 0 
                            sleep(0.5)
                    if verificaMouse(botaoAnterior,(20,280),xy) == True:
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            cont -= 1
                            sleep(0.5)
        
        if verificaMouse(botaoVoltar,(30,505),xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                NovoJogo()
                sleep(0.1)
        if verificaMouse(botaoIniciar, (651,525),xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if cont == 0:
                    animacao.fundo = pygame.image.load('imagens/fundos/mesa2.jpg').convert_alpha()
                elif cont == 1:
                    animacao.fundo = pygame.image.load('imagens/fundos/mesa1.jpg').convert_alpha()
                elif cont == 2:
                    animacao.fundo = pygame.image.load('imagens/fundos/fundoChesf.jpg').convert_alpha()
                
                animacao.jogo()
        pygame.display.flip()

def NovoJogo():
    
    botaoAvancar = pygame.image.load("imagens/Botoes/avancar.png").convert_alpha()
    
    jogador1 = pygame.image.load("imagens/fundos/jogador1.png").convert_alpha()
    jogador2 = pygame.image.load("imagens/fundos/jogador2.png").convert_alpha()
    
    janelaVermelha = pygame.image.load('imagens/molduraVermelha.png').convert_alpha()
    janelaBranca = pygame.image.load('imagens/molduraAmarela.png').convert_alpha()
    
    matheus = pygame.image.load('imagens/imagensPersonagens/matheus.jpg')
    igor = pygame.image.load('imagens/imagensPersonagens/igor.png')
    muttley = pygame.image.load('imagens/imagensPersonagens/muttley.png')
    lucas = pygame.image.load('imagens/imagensPersonagens/lucas.png')
    tulio = pygame.image.load('imagens/imagensPersonagens/tulio.png')
    alan = pygame.image.load('imagens/imagensPersonagens/alan.png')
    francois = pygame.image.load('imagens/imagensPersonagens/matheus.jpg')
    pastor = pygame.image.load('imagens/imagensPersonagens/pastor.jpg')
    
    cont = 0
    
    coluna = [130,280,430,580]
    linha = [200,350]
    
    coordenadas = []
    selecionado = False
             
    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        
        xy = pygame.mouse.get_pos() #Recupera a posicao do mouse
        
        screen.blit(fundo,(0,0))
    
        janelas = {}
        
        
        def imagensPersonagens():
            screen.blit(matheus,(143,217))
            screen.blit(lucas,(143,367))
            screen.blit(muttley,(293,217))
            screen.blit(pastor,(293,367))
            screen.blit(francois,(443,217))
            screen.blit(alan,(443,367))
            screen.blit(igor,(593,217))
            screen.blit(tulio,(593,367))
        
        def quadroVermelho():
            k = 0
            for i in coluna:
                for j in linha:
                    k = k+1
                    screen.blit(janelaVermelha,(i,j))
                    coordenadas.append((i,j))
                    janelas[k] = (i,j)
                    
        
        if cont == 0:
            screen.blit(jogador1,(0,0))
            screen.blit(botaoVoltar,(30,505))
            quadroVermelho()
            imagensPersonagens()
    
            if verificaMouse(janelaVermelha, janelas[1], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player1 = 'Matheus'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[2], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player1 = 'Lucas'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[3], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player1 = 'Muttley'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[4], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player1 = 'Vitor'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[5], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player1 = 'Francois'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[6], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player1 = 'Alan'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[7], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player1 = 'Igor'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[8], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player1 = 'Tulio'
                    cont += 1
                    sleep(0.1)
        
            if verificaMouse(botaoVoltar,(30,505),xy) == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    MenuInicial()
       
        elif cont == 1:
            
            screen.blit(jogador2,(0,0))
            screen.blit(botaoVoltar,(30,505))
            screen.blit(botaoAvancar,(570,505))
            quadroVermelho()
            imagensPersonagens()
            
            if verificaMouse(janelaVermelha, janelas[1], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player2 = 'Matheus'
                    selecionado = True
                    
            if verificaMouse(janelaVermelha, janelas[2], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player2 = 'Lucas'
                    selecionado = True
                    
            if verificaMouse(janelaVermelha, janelas[3], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player2 = 'Muttley'
                    selecionado = True
                    
            if verificaMouse(janelaVermelha, janelas[4], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player2 = 'vitor'
                    selecionado = True
                    
            if verificaMouse(janelaVermelha, janelas[5], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player2 = 'Francois'
                    selecionado = True

            if verificaMouse(janelaVermelha, janelas[6], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player2 = 'Alan'
                    selecionado = True
                    
            if verificaMouse(janelaVermelha, janelas[7], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player2 = 'Igor'
                    selecionado = True
                
            if verificaMouse(janelaVermelha, janelas[8], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    animacao.player2 = 'Tulio'
                    selecionado = True
                    
            if verificaMouse(botaoVoltar,(30,505),xy) == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cont -= 1
                    sleep(0.1)
                    
            elif verificaMouse(botaoAvancar,(570,505),xy) == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if selecionado == True:
                        Cenarios()
                    
        pygame.display.flip()

def MenuInicial():
    
    botaoNovoJogo = pygame.image.load("imagens/Botoes/novojogo.png").convert_alpha()
    botaoInstrucoes = pygame.image.load("imagens/Botoes/instrucoes.png").convert_alpha()
    botaoCreditos = pygame.image.load("imagens/Botoes/creditos.png").convert_alpha()
    botaoSair = pygame.image.load("imagens/Botoes/sairNovo.png").convert_alpha()
    
    fundo = pygame.image.load("imagens/fundos/inicio_Jogo.png").convert()
    
    posBotaoNovoJogo = (552,221)
    posBotaoInstrucoes = (550,300)
    posBotaoCreditos = (565,371)
    posBotaoSair = (602,443)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                
        xy = pygame.mouse.get_pos() #retorna a posicao do mouse
        
        screen.blit(fundo,(0,0))
        screen.blit(botaoNovoJogo, posBotaoNovoJogo)
        screen.blit(botaoInstrucoes, posBotaoInstrucoes)
        screen.blit(botaoCreditos, posBotaoCreditos)
        screen.blit(botaoSair, posBotaoSair)
        
        if verificaMouse(botaoNovoJogo,posBotaoNovoJogo,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                NovoJogo()
        elif verificaMouse(botaoInstrucoes,posBotaoInstrucoes,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Instrucoes()
        elif verificaMouse(botaoCreditos,posBotaoCreditos,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Creditos()
        elif verificaMouse(botaoSair,posBotaoSair,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                exit()  
        pygame.display.flip()