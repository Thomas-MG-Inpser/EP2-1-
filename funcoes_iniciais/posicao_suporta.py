def posicao_suporta(mapa, blocos, linha, coluna, ori):
    for i in range(blocos):
        if ori=='v':
            if (linha+(blocos-1))>=len(mapa) or mapa[linha+i][coluna]=='N':
                return False
        elif ori=='h':
            if (coluna+(blocos-1))>=len(mapa) or mapa[linha][coluna+i]=='N':
                return False
    return True