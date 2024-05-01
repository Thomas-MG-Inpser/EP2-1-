def cria_mapa(n):
    mapa = []
    for i in range(n):
        mapa.append([' ']*n)
    return mapa

import random
def aloca_navios(mapa, navios):
    n=len(mapa)
    for blocos in navios:
        f=True
        while f:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            for i in range(blocos):
                if orientacao=='v':
                  if (linha+(blocos-1))>=len(mapa) or mapa[linha+i][coluna]!=' ':
                        f=True
                        break
                elif orientacao=='h':
                    if (coluna+(blocos-1))>=len(mapa) or mapa[linha][coluna+i]!=' ':
                        f=True
                        break
                f=False
        if orientacao=='v':
            for i in range(blocos):
                mapa[linha+i][coluna]='N'
        elif orientacao=='h':
            for i in range(blocos):
                mapa[linha][coluna+i]='N'
    return mapa

def posicao_suporta(mapa, blocos, linha, coluna, ori):
    for i in range(blocos):
        if ori=='v':
            if (linha+(blocos-1))>=len(mapa) or mapa[linha+i][coluna]=='N':
                return False
        elif ori=='h':
            if (coluna+(blocos-1))>=len(mapa) or mapa[linha][coluna+i]=='N':
                return False
    return True

def foi_derrotado(mapa):
    for i in mapa:
        for j in i:
            if j == 'N':
                return False
    return True

def tiro_player(mapa, posicao):
    coluna= posicao[0]
    linha=int(posicao[1])
    if mapa[linha][coluna]== ' ':
        mapa[linha][coluna]= 'o'
    elif mapa[linha][coluna]== 'N':
         mapa[linha][coluna]= 'X'
    else:
         print('Coordenada inválida(linha 41)')
         return mapa
    return mapa