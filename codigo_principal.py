import time
import random
from funcoes_iniciais import cria_mapa
from funcoes_iniciais import aloca_navios
from funcoes_iniciais import foi_derrotado
from funcoes_iniciais import posicao_suporta
from parametros import PAISES
from parametros import CONFIGURACAO

print(' ===================================== ')
print('|                                     |')
print('| Bem-vindo ao INSPER - Batalha Naval |')
print('|                                     |')
print(' =======   xxxxxxxxxxxxxxxxx   ======= ')

#esta parte é um temporizador e um icicializador pra ficar dahorinha
"""
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

#print(PAISES)
#pais=input('Selecione seu país:')

#aqui começa o ferro
mapa=cria_mapa(12)

alfabeto=[' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' ']
numeros=[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ' ']

for i in range(len(mapa[0])):
    mapa[0][i]=alfabeto[i]
    mapa[len(mapa)-1][i]=alfabeto[i]
for i in range(len(mapa)):
    mapa[i][0]=numeros[i]
    mapa[i][len(mapa)-1]=numeros[i]
#for i in range(len(mapa)):
    #print(''.join(mapa[i])) #assim seria string
    #print(mapa[i])
#mapa criado como lista de listas




#print(mapa)

#pc seleciona pais aleatório
paispc = []
for p, navios in PAISES.items():
    paispc.append(p)
r = random.choice(paispc)
print(r)

blocos = []
for navios, n in PAISES[r].items():
    for i in range(n):
        blocos.append(CONFIGURACAO[navios])

mapa_pc = aloca_navios(mapa, blocos)
for i in mapa_pc:
    print(i)

#pais_pc=(aloca_navios(mapa, random.choice(PAISES)))

