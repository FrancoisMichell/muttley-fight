



from FixTk import ver
from pygame.locals import *
from sys import exit
from time import sleep
import pygame
import pygame.mixer


largura, altura = 800,600


pygame.init()

screen = pygame.display.set_mode((largura,altura),0,32)
pygame.display.set_caption  ("Muttley Fight")

fundo = pygame.image.load('imagens/fundos/background.jpg')
botaoVoltar = pygame.image.load("imagens/botoes/voltar.png").convert_alpha()


#Para Sons a serem inseridos no jogo/Comandos para inicar e parar o som/Configurar volume do som/Configurar volume do som:

Som = pygame.mixer.Sound("Arquivo")

Som.play()                          

Som.stop()

Som.set_volume(0)



#Para Músicas de fundo dos cenários/Iniciar música/Parar música/Setar volume da música:

pygame.mixer.music.load("Arquivo")

pygame.mixer.music.load (-1)

pygame.mixer.music.stop()

pygame.mixer.music.set_volume(0)