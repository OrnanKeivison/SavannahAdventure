import pygame
from pygame import mixer
from pygame.sprite import Sprite
from random import choice
from superCasses import *
from subClasses import *

#criando a janela do jogo
size = [600, 600]
display = pygame.display.set_mode(size)
pygame.display.set_caption('floresta dos animais')

#load image tela inicial
init = pygame.image.load('data/image/screen_init.png')
init = pygame.transform.scale(init, (600, 600))

#load image tela de vitória
win = pygame.image.load('data/image/ganhou.png')
win = pygame.transform.scale(win, (600, 600))

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

#definindo os animais
a1 = Elephant("ella", "cinza", "f", 3, 200, 0, 0)
a2 = Giraffe("fernando", "amarelo", "m", 3, 200, 0, 100)
a3 = Lion("leo", "golden", "m", 3, 200, 0, 200)
a4 = Monkey("jorge", "marrom", "m", 3, 200, 0, 300)
a5 = Rhino("rino", "cinza", "m", 3, 200, 0, 400)
a6 = Zebra("zoe", "cinza", "f", 3, 200, 0, 500)

#definindo a savana
s = Savannah([a1, a2, a3, a4, a5, a6])

#movimenta animais 
def mov_animals():
    if a1.getPosX() != 1000000:
        i = choice(range(0, 6))
        j = choice(range(0, 6))
        s.andar(a1, posiçoes[i][j])

    if a2.getPosX() != 1000000:
        i = choice(range(0, 6))
        j = choice(range(0, 6))
        s.andar(a2, posiçoes[i][j])

    if a4.getPosX() != 1000000:
        i = choice(range(0, 6))
        j = choice(range(0, 6))
        s.andar(a4, posiçoes[i][j])

    if a5.getPosX() != 1000000:
        i = choice(range(0, 6))
        j = choice(range(0, 6))
        s.andar(a5, posiçoes[i][j])

    if a6.getPosX() != 1000000:
        i = choice(range(0, 6))
        j = choice(range(0, 6))
        s.andar(a6, posiçoes[i][j])

#iniciando variaveis
passe = True
go = True
gameloop = True

posicao_jogador = [0, 0]
linha = 2
coluna = 0

mortes = 0

move_um = 1

animal = a3 
#positions
posiçoes = [[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],  
            [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6)], 
            [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)], 
            [(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 
            [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)],
            [(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]]

# iniciando fps do jogo
fps = pygame.time.Clock()

#iniciando loop do jogo
while gameloop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        
        elif event.type == pygame.KEYDOWN:

            #eventos do jogador principal (movimentação)
            if event.key == pygame.K_RIGHT:
                coluna += 1
                posicao_jogador = posiçoes[linha][coluna]
                s.andar(a3, posicao_jogador)
                mov_animals()

            if event.key == pygame.K_LEFT:
                coluna -= 1
                posicao_jogador = posiçoes[linha][coluna]
                s.andar(a3, posicao_jogador)
                mov_animals()
            
            if event.key == pygame.K_UP:
                linha -= 1
                posicao_jogador = posiçoes[linha][coluna]
                s.andar(a3, posicao_jogador)
                mov_animals()

            if event.key == pygame.K_DOWN:
                linha += 1
                posicao_jogador = posiçoes[linha][coluna]
                s.andar(a3, posicao_jogador)
                mov_animals()
                
    #loop para página inicial
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

    #função de init  
    draw()

    #desenha os animais no tabuleiro 
    a1.show_on_screen(display)
    a2.show_on_screen(display)
    a3.show_on_screen(display)
    a4.show_on_screen(display)
    a5.show_on_screen(display)
    a6.show_on_screen(display)
    
    if move_um == 1:
        mov_animals()
        move_um = 2

    colisoes = s.checar_colisao()
    for posicao, animais in colisoes:
        if 1000000 in posicao: 
            animais.clear()
        if len(animais) == 2:
            if animais[0] == a3:
                animais[0].make_sound()
                animais[1].make_sound()
                animais[1].matar() 
                animais.clear()
                mortes += 1
            elif animais[1] == a3:
                animais[0].make_sound()
                animais[1].make_sound()
                animais[0].matar()
                animais.clear()
                mortes += 1

        else:
            continue

        if mortes == 5:
            print('ganhou')
            a3.matar()
            while go: 
                display.blit(win, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameloop = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            go = False 
                fps.tick(60)
                pygame.display.update()

            

    
    

    fps.tick(30)
    pygame.display.update()