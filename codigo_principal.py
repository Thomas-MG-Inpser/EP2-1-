import time
import random
from funcoes_iniciais import cria_mapa
from funcoes_iniciais import aloca_navios
from funcoes_iniciais import foi_derrotado
from funcoes_iniciais import posicao_suporta
from parametros import PAISES
from parametros import CONFIGURACAO

from funcoes_iniciais import tiro_player
from funcoes_iniciais import tiro_pc

print(' ===================================== ')
print('|                                     |')
print('| Bem-vindo ao INSPER - Batalha Naval |')
print('|                                     |')
print(' =======   xxxxxxxxxxxxxxxxx   ======= ')

"""
#esta parte é um temporizador e um icicializador pra ficar dahorinha
print('digite qualquer coisa para continuar')
u=input('')
print('Jogo iniciando...')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
"""

#aqui começa o ferro
mapa_ori=cria_mapa(12)


alfabeto=[' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' ']
numeros=[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ' ']

for i in range(len(mapa_ori[0])):
    mapa_ori[0][i]=alfabeto[i]
    mapa_ori[len(mapa_ori)-1][i]=alfabeto[i]
for i in range(len(mapa_ori)):
    mapa_ori[i][0]=numeros[i]
    mapa_ori[i][len(mapa_ori)-1]=numeros[i]
#for i in range(len(mapa_ori)):
    #print(''.join(mapa_ori[i])) #assim seria string
    #print(mapa_ori[i])
#mapa criado como lista de listas

mapa_branco=mapa_ori

#pc seleciona pais aleatório
paispc = []
for p, navios in PAISES.items():
    paispc.append(p)
r = random.choice(paispc)
print(f'COMPUTADOR - {r}')

blocos_pc = []
for navios_pc, n in PAISES[r].items():
    for i in range(n):
        blocos_pc.append(CONFIGURACAO[navios_pc])

mapa_pc = aloca_navios(mapa_ori, blocos_pc)


#imprime o mapa do pc
"""
for i in mapa_pc:
    print(i)
"""


opa = []
for i in PAISES:
    opa.append(i)

conta = 1
for pais, navios in PAISES.items():
    dic = {pais: navios}
    print(f'{conta}: {dic}')
    conta += 1

mapa_ori=cria_mapa(12)

alfabeto=[' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' ']
numeros=[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ' ']

for i in range(len(mapa_ori[0])):
    mapa_ori[0][i]=alfabeto[i]
    mapa_ori[len(mapa_ori)-1][i]=alfabeto[i]
for i in range(len(mapa_ori)):
    mapa_ori[i][0]=numeros[i]
    mapa_ori[i][len(mapa_ori)-1]=numeros[i]


index_pais_player = int(input("Escolha o número da sua nação: "))-1
pais_player = opa[index_pais_player]
print(pais_player)

blocos_player = []
for navios_player, n in PAISES[pais_player].items():
    for i in range(n):
        blocos_player.append(CONFIGURACAO[navios_player])


for blocos in blocos_player:
    f=True
    while f:
        coluna_let = input('Informe a Letra: ').upper()
        for i in range(len(alfabeto)):
            if alfabeto[i] == coluna_let:
                coluna = i
        linha = int(input('Informe a Número: '))
        orientacao = input('Informe a Orientação(v/h): ')
        for i in range(blocos):
            if orientacao=='v':
                if (linha+(blocos-1))>=len(mapa_ori) or mapa_ori[linha+i][coluna]!=' ':
                    f=True
                    print("Opção Inválida")
                    break
            elif orientacao=='h':
                if (coluna+(blocos-1))>=len(mapa_ori) or mapa_ori[linha][coluna+i]!=' ':
                    f=True
                    print("Opção Inválida")
                    break
            elif orientacao not in ['h', 'v'] or linha > len(mapa_ori)-2 or coluna > len(mapa_ori)-2:
                    f=True
                    print("Opção Inválida")
                    break
            
            f=False
    if orientacao=='v':
        for i in range(blocos):
            mapa_ori[linha+i][coluna]='N'
    elif orientacao=='h':
        for i in range(blocos):
            mapa_ori[linha][coluna+i]='N'
    for i in mapa_pc:
        print(i)
    for i in mapa_ori:
        print(i)

# comecar os tiros

jogo_continua=True # vai ser definido pela funcao foi_derrotado
while jogo_continua: 
    coluna_player= input('Qual letra?')
    coluna_player=coluna_player.upper()
    if coluna_player not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
        print('Coordenada inválida(linha 152)')
        continue
    for i in range(len(alfabeto)):
            if alfabeto[i] == coluna_player:
                coluna_player = i
    linha_player= input('Qual número?')
    if linha_player not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print('Coordenada inválida(linha 159)')
        continue
    coordenada=[coluna_player, linha_player]
    mapa_pc= tiro_player(mapa_pc,coordenada)

    mapa_ori= tiro_pc(mapa_ori)
    for i in mapa_pc:
        print(i)
    for i in mapa_ori:
        print(i)
    player= foi_derrotado(mapa_ori)
    pc= foi_derrotado(mapa_pc)
    if (player or pc)==True:
        jogo_continua=False

if player:
    print('Computador venceu!')
if pc:
    print('Você venceu!!!')

#escrevi qualquer coisa

x=0