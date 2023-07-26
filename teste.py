posiçoes = [[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],  
            [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6)], 
            [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)], 
            [(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 
            [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)],
            [(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]]

linha = coluna = 0
velocidade = 1
pos = posiçoes[linha][coluna]

rodada = 0

i = 0
while i < 20:

    if i%2 == 0 :
        if coluna == 5 or coluna == -1:
            coluna -= velocidade
            print(posiçoes[linha][coluna])
            print(linha, coluna)
        else:
            coluna += velocidade
            print(posiçoes[linha][coluna])
            print(linha,coluna)
            

    else:
        if linha == 5 or linha == -1:
            linha -= velocidade
            print(posiçoes[linha][coluna])
            print(linha,coluna)
        else:
            linha += velocidade
            print(posiçoes[linha][coluna])
            print(linha,coluna)

    i += 1