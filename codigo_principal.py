import time
import random
from funcoes_iniciais import cria_mapa
from funcoes_iniciais import aloca_navios
from funcoes_iniciais import foi_derrotado
from funcoes_iniciais import posicao_suporta
from parametros import PAISES

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

print(PAISES)
pais=input('Selecione seu país:')

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
for i in range(len(mapa)):
    #print(''.join(mapa[i])) #assim seria string
    print(mapa[i])
#mapa criado como lista de listas



#print(mapa)

"""
print (u"\u001b[40m A \u001b[41m B \u001b[42m C \u001b[43m D \u001b[0m")
print (u"\u001b[44m A \u001b[45m B \u001b[46m C \u001b[47m D \u001b[0m")
print (u"\u001b[40;1m c \u001b[41;1m B \u001b[42;1m C \u001b[43;1m D \u001b[0m")
print (u"\u001b[44;1m A \u001b[45;1m B \u001b[46;1m C \u001b[47;1m D \u001b[0m")
print (u"\u001b[30m A \u001b[31m B \u001b[32m C \u001b[33m D \u001b[0m")
print (u"\u001b[34;1m E \u001b[35m F \u001b[36m G \u001b[37m H \u001b[0m")
"""