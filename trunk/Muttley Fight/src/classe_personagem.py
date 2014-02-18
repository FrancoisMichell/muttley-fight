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

    def rectIdle(self):
        
        if self.nome == 'vitor':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 45, 100)
        
        elif self.nome == 'Matheus':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 35, 100)
       
        elif self.nome == 'Muttley':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 35, 100)
            
        elif self.nome == 'Igor':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 35, 100)
            
        elif self.nome == 'Alan':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 35, 100)
            
        elif self.nome == 'Lucas':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 35, 100)
            
        elif self.nome == 'Tulio':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 35, 100)
            
        elif self.nome == 'Francois':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 35, 100)
            
    def rectChute(self):
        
        if self.nome == 'vitor':
            chute = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return chute
        
        if self.nome == 'Matheus':
            chute = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return chute
        
        if self.nome == 'Muttley':
            chute = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return chute
        
        if self.nome == 'Igor':
            chute = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return chute
        
        if self.nome == 'Alan':
            chute = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return chute
        
        if self.nome == 'Lucas':
            chute = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return chute
        
        if self.nome == 'Tulio':
            chute = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return chute
        
        if self.nome == 'Francois':
            chute = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return chute
        
    def rectSoco(self):
        
        if self.nome == 'vitor':
            soco = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return soco
        
        if self.nome == 'Matheus':
            soco = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return soco
        
        if self.nome == 'Muttley':
            soco = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return soco
        
        if self.nome == 'Igor':
            soco = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return soco
        
        if self.nome == 'Alan':
            soco = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return soco
        
        if self.nome == 'Lucas':
            soco = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return soco
        
        if self.nome == 'Tulio':
            soco = pygame.Rect(self.pos_x, self.pos_y, 160,200)
            return soco
        
        if self.nome == 'Francois':
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