def foi_derrotado(mapa):
    for i in mapa:
        for j in i:
            if j == 'N':
                return False
    return True