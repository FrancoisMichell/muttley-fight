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
                #animação de salto do personagem
            self.PosicaoX += 5
            sleep(0.1)
            self.PosicaoX += 5
            sleep(0.1)                      #Personagem salta aos poucos e desce aos poucos, não testei
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
                #retorna a animação idle
            if tecla[pygame.K_LEFT]:
                if self.PosicaoX > 0: #garante que o personagem não ultrapasse o limite da tela.
                    self.PosicaoX -= 5
                    #animação de movimentação
            if tecla[pygame.K_RIGHT]:
                if self.PosicaoX < 780: #se a tela for 800x600, 780 seria um valor que garantiria que o personagem não saia da tela
                    self.PosicaoX += 5
                    #animação de movimentação
                    
    def Golpe(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_x]:               #Supondo X como tecla de soco
            #personagem modifica seu Hitbox para hitbox de soco
            #animação do personagem se modifica para animação de soco
        if tecla[pygame.K_z]:               #Supondo Z como tecla de chute
            #personagem modifica seu hitbox para hitbox de chute
            #animação do personagem se modifica para animação de chute
        if tecla[pygame.K_c]:               #Supondo C como tecla de defesa
            #personagem modifica seu hitbox para hitbox de defesa
            #animação do personagem se modifica para animação de defesa
                
    def Dano(self):                
    #classe reservada ao cálculo de dano e interações de hitbox de personagens.
    
    
    
    
    #falta fazer a outra classe personagem.
         
        
        
        
                    
             

'''
Created on 01/02/2014

@author: Neto
'''
