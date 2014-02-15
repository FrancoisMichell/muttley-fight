# coding utf-8
# esboco da classe personagem, com atributos, vida, essas coisas.
import pygame

class Personagem:
    def __init__(self,nome, pos_x, pos_y,largura):
        self.vida = 100
        self.sprites={}
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.largura = largura
        self.nome = nome

    def rectIdle(self,nome):
        if self.nome == 'pastor':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 45, 100)
        elif self.nome == 'teste':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 35, 100)

    def rectChute(self):
        if self.nome == 'pastor':
            chute = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return chute
        if self.nome == 'teste':
            chute = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return chute
    def rectSoco(self):
        if self.nome == 'pastor':
            soco = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return soco
        if self.nome == 'teste':
            soco = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return soco
    def getx(self):
        return self.pos_x

    def gety(self):
        return self.pos_y
    
    def setx (self, x):
        self.pos_x = x
        self.andar(x)
         
    def andar(self,x):
        self.rect.x = x
        return self.rect.x
    
    def perdeVida(self, perdeu):
        self.vida -= perdeu
