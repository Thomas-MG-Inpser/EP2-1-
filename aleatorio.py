'''
mapa =''
for blocos in navios:
    f=True
    while f:
        coluna = input('Informe a Letra: ')
        linha = input('Informe a Número: ')
        orientacao = input('Informe a Orientação(v/h): ')
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
'''
letra = 'C'
numero = 1
ori= 'v'
posicao=[letra, numero]