import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from FixTk import ver


class PersonagemGeral:
    PosicaoX = "?"
    PosicaoY = "?"
    PontosDeVida = 200
    PontosDeEspecial = 0
    def Movimentacao(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_UP]:
                #anima��o de salto do personagem
            self.PosicaoX += 5
            sleep(0.1)
            self.PosicaoX += 5
            sleep(0.1)                      #Personagem salta aos poucos e desce aos poucos, n�o testei
            self.PosicaoX += 5
            sleep(0.1)
            self.PosicaoX += 5
            sleep(0.1)
            self.PosicaoX -= 5                   
            sleep(0.1)
            self.PosicaoX -= 5
            sleep(0.1)
            self.PosicaoX -= 5
            sleep(0.1)
            self.PosicaoX -= 5
            sleep(0.1)
                #retorna a anima��o idle
            if tecla[pygame.K_LEFT]:
                if self.PosicaoX > 0: #garante que o personagem n�o ultrapasse o limite da tela.
                    self.PosicaoX -= 5
                    #anima��o de movimenta��o
            if tecla[pygame.K_RIGHT]:
                if self.PosicaoX < 780: #se a tela for 800x600, 780 seria um valor que garantiria que o personagem n�o saia da tela
                    self.PosicaoX += 5
                    #anima��o de movimenta��o
                    
    def Golpe(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_x]:               #Supondo X como tecla de soco
            #personagem modifica seu Hitbox para hitbox de soco
            #anima��o do personagem se modifica para anima��o de soco
        if tecla[pygame.K_z]:               #Supondo Z como tecla de chute
            #personagem modifica seu hitbox para hitbox de chute
            #anima��o do personagem se modifica para anima��o de chute
        if tecla[pygame.K_c]:               #Supondo C como tecla de defesa
            #personagem modifica seu hitbox para hitbox de defesa
            #anima��o do personagem se modifica para anima��o de defesa
                
    def Dano(self):                
    #classe reservada ao c�lculo de dano e intera��es de hitbox de personagens.
    
    
    
    
    #falta fazer a outra classe personagem.
         
        
        
        
                    
             

'''
Created on 01/02/2014

@author: Neto
'''
