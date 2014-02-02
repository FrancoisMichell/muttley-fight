import pygame.mixer #biblioteca necessária para usar os comandos de som



#Para Sons a serem inseridos no jogo/Comandos para inicar e parar o som/Configurar volume do som:

Som = pygame.mixer.Sound("Arquivo")

Som.play()                          

Som.stop()

Som.set_volume(0)

#Outros comandos de som:



Som.fadeout #diminui o som gradativamente até sumir
Som.get_volume()    #exibe o volume atual do som
Som.get_num_channels    #conta quantas vezes esse som está tocando



#Para Músicas de fundo dos cenários/Iniciar música/Parar música/Setar volume da música:

pygame.mixer.music.load("Arquivo")              #não necessita criar uma variável 

pygame.mixer.music.load (-1)

pygame.mixer.music.stop()

pygame.mixer.music.set_volume(0)