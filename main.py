import pygame
from pygame import mixer
from pygame.sprite import Sprite
from superCasses import *
from subClasses import *

#criando a janela do jogo
size = [600, 600]
display = pygame.display.set_mode(size)
pygame.display.set_caption('floresta dos animais')
passe = True
go = True
num = 0

#load image tela inicial
init = pygame.image.load('data/image/screen_init.png')
init = pygame.transform.scale(init, (600, 600))

#função para desenhar o fundo
def draw():
    fundo = pygame.image.load('data/image/tabuleiro.png')
    fundo = pygame.transform.scale(fundo, (600, 600))
    display.blit(fundo, (0, 0))

#função para iniciar a music
def music():
    pygame.mixer.init()
    pygame.mixer.music.load('data/music/music.wav')
    pygame.mixer.music.play(-1)

#music()

#definindo os animais
a1 = Elephant("ella", "cinza", "f", 3, 200, 0, 0)

s = Savannah([a1])

posiçoes = [[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],  
            [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6)], 
            [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)], 
            [(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 
            [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)],
            [(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]]

fps = pygame.time.Clock()
gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_l:
        #         if num <= len(posiçoes):
        #             num+=1
        #             s.andar(a1, posiçoes[num])

        #         else:
        #             num-=1
        #             s.andar(a1, posiçoes[num])

    
    while passe: 
        display.blit(init, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    passe = False 
        fps.tick(60)
        pygame.display.update()    

      
    draw()
    a1.show_on_screen(display)
    linha = coluna = 0
    velocidade = 1
    pos = posiçoes[linha][coluna]

    rodada = 0
    i = 0
    while i < 20:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:

                    if i%2 == 0 :
                        if coluna == 5 or coluna == -1:
                            coluna -= velocidade
                            s.andar(a1, (posiçoes[linha][coluna]))
                        else:
                            coluna += velocidade
                            
                            s.andar(a1, (posiçoes[linha][coluna]))
                            

                    else:
                        if linha == 5 or linha == -1:
                            linha -= velocidade
                            s.andar(a1, (posiçoes[linha][coluna]))
                        else:
                            linha += velocidade
                            s.andar(a1, (posiçoes[linha][coluna]))

        i += 1
        

    fps.tick(30)
    pygame.display.update()