import pygame
from pygame import mixer
from pygame.sprite import Sprite
from superCasses import *
from subClasses import *
from random import choice

#criando a janela do jogo
size = [600, 600]
display = pygame.display.set_mode(size)
pygame.display.set_caption('floresta dos animais')

passe = True
posicao_jogador = [0, 0]

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
a2 = Giraffe("fernando", "amarelo", "m", 3, 200, 0, 100)
a3 = Lion("leo", "golden", "m", 3, 200, 0, 200)
a4 = Monkey("jorge", "marrom", "m", 3, 200, 0, 300)
a5 = Rhino("rino", "cinza", "m", 3, 200, 0, 400)
a6 = Zebra("", "cinza", "f", 3, 200, 0, 500)

s = Savannah([a1, a2, a3, a4, a5, a6])

#select the animal
animal = a3

linha = 2
coluna = 0

#positions
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
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                coluna += 1
                posicao_jogador = posiçoes[linha][coluna]
                s.andar(animal, posicao_jogador)

            if event.key == pygame.K_LEFT:
                coluna -= 1
                posicao_jogador = posiçoes[linha][coluna]
                s.andar(animal, posicao_jogador)
            
            if event.key == pygame.K_UP:
                linha -= 1
                posicao_jogador = posiçoes[linha][coluna]
                s.andar(animal, posicao_jogador)

            if event.key == pygame.K_DOWN:
                linha += 1
                posicao_jogador = posiçoes[linha][coluna]
                s.andar(animal, posicao_jogador)
            
            if animal != a1:
                if event.key == pygame.K_1:
                    i = choice(range(0, 6))
                    j = choice(range(0, 6))
                    s.andar(a1, posiçoes[i][j])

            if animal != a2:
                if event.key == pygame.K_2:
                    i = choice(range(0, 6))
                    j = choice(range(0, 6))
                    s.andar(a2, posiçoes[i][j])
            
            if animal != a3:
                if event.key == pygame.K_3:
                    i = choice(range(0, 6))
                    j = choice(range(0, 6))
                    s.andar(a3, posiçoes[i][j])

            if animal != a4:
                if event.key == pygame.K_4:
                    i = choice(range(0, 6))
                    j = choice(range(0, 6))
                    s.andar(a4, posiçoes[i][j])
            
            if animal != a5:
                if event.key == pygame.K_5:
                    i = choice(range(0, 6))
                    j = choice(range(0, 6))
                    s.andar(a5, posiçoes[i][j])

            if animal != a6:
                if event.key == pygame.K_6:
                    i = choice(range(0, 6))
                    j = choice(range(0, 6))
                    s.andar(a6, posiçoes[i][j])
                
    
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
    a2.show_on_screen(display)
    a3.show_on_screen(display)
    a4.show_on_screen(display)
    a5.show_on_screen(display)
    a6.show_on_screen(display)
    
    colisoes = s.checar_colisao()
    for posicao, animais in colisoes:
        for animal in animais:
            animal.make_sound()
    

    fps.tick(30)
    pygame.display.update()