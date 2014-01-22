import pygame
from pygame.locals import *
from sys import exit
largura, altura = 800,600


pygame.init()

screen = pygame.display.set_mode((largura,altura),0,32)
pygame.display.set_caption  ("Muttley Fight")


def verificaMouse(img_botao,pos_botao,pos_mouse):
    img_x, img_y = pos_botao 
    img_w, img_h = img_botao.get_size() 
    varia_x = img_x + img_w 
    varia_y = img_y + img_h 
    if pos_mouse[0] > img_x and pos_mouse[0] < varia_x and pos_mouse[1] > img_y and pos_mouse[1] < varia_y: 
        return True
    return False

def Opcoes():
    
    fundoOpcoes = pygame.image.load("imagens/fundos/fundoPreto.png").convert()
    botaoVoltar = pygame.image.load("imagens/botoes/voltar.png").convert()
    
    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    
    
        
        xy = pygame.mouse.get_pos() #Recupera a posicao do mouse

        screen.blit(fundoOpcoes,(0,0))
        screen.blit(botaoVoltar,(30,505))
        
        if verificaMouse(botaoVoltar,(30,505),xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                MenuInicial()
         
        pygame.display.flip()

def Creditos():
    fundoCreditos = pygame.image.load("Imagens/Fundos/telaCreditos.jpg").convert()
    botaoVoltar = pygame.image.load("imagens/Botoes/voltar.png").convert()
    
    posBotaoVoltar = (30,505)
    
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
    
    fundoCenarios = pygame.image.load("imagens/fundos/fundoPreto.png").convert()
    botaoIniciar = pygame.image.load("imagens/botoes/iniciar.png").convert()
    botaoVoltar = pygame.image.load("imagens/botoes/voltar.png").convert()
    
    img1 = pygame.image.load("imagens/20140116_103314.jpg").convert()
    img2 = pygame.image.load("imagens/20140116_103338.jpg").convert()
    img3 = pygame.image.load("imagens/fundoChesf.jpg").convert() 
     
        
    posBotaoIniciar = (570,505)
    posBotaoVoltar = (30,505)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        xy = pygame.mouse.get_pos()
        
        screen.blit(fundoCenarios,(0,0))
        screen.blit(botaoIniciar, posBotaoIniciar)
        screen.blit(botaoVoltar, posBotaoVoltar)
        screen.blit(img1,(30,70))
        screen.blit(img2,(300,250))
        screen.blit(img3,(570,70))

        if verificaMouse(botaoVoltar,posBotaoVoltar,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                MenuInicial()
                
        pygame.display.flip

def NovoJogo():
    
    
    fundoNovoJogo = pygame.image.load("imagens/fundos/fundoPreto.png").convert()
    botaoVoltar = pygame.image.load("imagens/Botoes/voltar.png").convert()
    botaoAvancar = pygame.image.load("imagens/Botoes/avancar.png").convert()
    nomePersonagem = pygame.image.load("imagens/personagens.png").convert()
    jogador1 = pygame.image.load("imagens/jogador1.png").convert()
        
    cont = 0
    
    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        
        xy = pygame.mouse.get_pos() #Recupera a posicao do mouse

        screen.blit(fundoNovoJogo,(0,0))
        screen.blit(botaoVoltar,(30,505))
        screen.blit(botaoAvancar,(570,505))
        screen.blit(nomePersonagem,(270,0))
        screen.blit(jogador1,(300,105))
   
##### MUDAR ALGO NO DISPLAY SEM MUDAR O TODO: USAR CONTADOR, CHAMANDO UMA FUNCAO COM O BLIT ####   
        
        if cont == 0:
            screen.blit(botaoVoltar,(30,505))
            TROCAR VOLTAR POR PERSONAGEM!!!
        elif cont == 1:
            screen.blit(botaoVoltar,(300,505))  
        
            
        if verificaMouse(botaoVoltar,(30,505),xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                MenuInicial()
                               
            
        elif verificaMouse(botaoAvancar,(570,505),xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Cenarios()
      
        pygame.display.flip()


def MenuInicial():
    
    fundoMenuInicial = pygame.image.load("imagens/fundos/fundoPreto.png").convert
    botaoNovoJogo = pygame.image.load("imagens/Botoes/novojogo.png").convert()
    botaoOpcoes = pygame.image.load("imagens/Botoes/opcoes.png").convert()
    botaoCreditos = pygame.image.load("imagens/Botoes/creditos.png").convert()
    botaoSair = pygame.image.load("imagens/Botoes/sair.png").convert()
    logo = pygame.image.load("imagens/logo.png").convert()
    
    posBotaoNovoJogo = (550,200)
    posBotaoOpcoes = (550,300)
    posBotaoCreditos = (550,400)
    posBotaoSair = (550,500)
    posLogo = (10,10)
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                
        xy = pygame.mouse.get_pos() #retorna a posicao do mouse
        
#        screen.blit(fundoMenuInicial,(0,0))
        screen.blit(logo,posLogo)
        screen.blit(botaoNovoJogo, posBotaoNovoJogo)
        screen.blit(botaoOpcoes, posBotaoOpcoes)
        screen.blit(botaoCreditos, posBotaoCreditos)
        screen.blit(botaoSair, posBotaoSair)
        
        if verificaMouse(botaoNovoJogo,posBotaoNovoJogo,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                NovoJogo()
        elif verificaMouse(botaoOpcoes,posBotaoOpcoes,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Opcoes()
        elif verificaMouse(botaoCreditos,posBotaoCreditos,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Creditos()
        elif verificaMouse(botaoSair,posBotaoSair,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                exit()  
        pygame.display.flip()