import pygame.mixer #biblioteca necess�ria para usar os comandos de som



#Para Sons a serem inseridos no jogo/Comandos para inicar e parar o som/Configurar volume do som:

Som = pygame.mixer.Sound("Arquivo")

Som.play()                          

Som.stop()

Som.set_volume(0)

#Outros comandos de som:



Som.fadeout #diminui o som gradativamente at� sumir
Som.get_volume()    #exibe o volume atual do som
Som.get_num_channels    #conta quantas vezes esse som est� tocando



#Para M�sicas de fundo dos cen�rios/Iniciar m�sica/Parar m�sica/Setar volume da m�sica:

pygame.mixer.music.load("Arquivo")              #n�o necessita criar uma vari�vel 

pygame.mixer.music.load (-1)

pygame.mixer.music.stop()

pygame.mixer.music.set_volume(0)