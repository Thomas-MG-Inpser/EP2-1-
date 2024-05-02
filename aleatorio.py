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

'''
lista = ["'a", "'b", "'c"]
lista2 = ["'"]
listaj = "".join(lista)
for i in range(len(listaj)):
    if listaj[i] in lista2:
        print(f'\u001b[30m{listaj[i]}\u001b[0m', end = ' ')
'''

mapa_branco = [
[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' '],
['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
['2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2'],
['3', ' ', ' ', ' ', ' ', 'N', ' ', ' ', ' ', ' ', ' ', '3'],
['4', ' ', ' ', ' ', ' ', 'N', ' ', ' ', ' ', ' ', ' ', '4'],
['5', ' ', ' ', ' ', ' ', 'N', ' ', ' ', ' ', ' ', ' ', '5'],
['6', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '6'],
['7', ' ', 'o', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', '7'],
['8', ' ', 'o', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', '8'],
['9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '9'],
['10', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '10'], 
[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' ']
]

conta = 1
def cores_player(mapa_branco):
    conta = 1
    for i in range(len(mapa_branco)):
        print('\u001b[0m')
        for j in range(len(mapa_branco)):
            if conta != len(mapa_branco):
                if mapa_branco[i][j] == 'N':
                    print('\u001b[42m    ', end = ' ')
                    conta += 1
                elif mapa_branco[i][j] == 'o':
                    print('\u001b[44m    ', end = ' ')
                    conta += 1
                elif mapa_branco[i][j] == 'X':
                    print('\u001b[41m    ', end = ' ')
                    conta += 1
                elif mapa_branco[i][j] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                    print(f'\u001b[40m  {mapa_branco[i][j]} ', end = ' ')
                    conta += 1
                elif mapa_branco[i][j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                    print(f'\u001b[40m  {mapa_branco[i][j]} ', end = ' ')
                    conta += 1
                else:
                    print('\u001b[40m    ', end = ' ')
                    conta += 1
            else:
                conta = 1
                if mapa_branco[i][j] == 'N':
                    print('\u001b[42m    ')
                elif mapa_branco[i][j] == 'o':
                    print('\u001b[44m    ')
                elif mapa_branco[i][j] == 'X':
                    print('\u001b[41m    ')
                elif mapa_branco[i][j] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                    print(f'\u001b[40m  {mapa_branco[i][j]} ')
                elif mapa_branco[i][j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                    print(f'\u001b[40m  {mapa_branco[i][j]} ')
                else:
                    print('\u001b[40m    ')
        #if len(mapa_branco[i]) == 12:
            #print('\u001b[0m', end = '')
    return ''   

#print(cores_player(mapa_branco))