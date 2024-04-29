import time
from funcoes_iniciais import cria_mapa
from funcoes_iniciais import aloca_navios
from funcoes_iniciais import foi_derrotado
from funcoes_iniciais import posicao_suporta

print(' ===================================== ')
print('|                                     |')
print('| Bem-vindo ao INSPER - Batalha Naval |')
print('|                                     |')
print(' =======   xxxxxxxxxxxxxxxxx   ======= ')
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

mapa=cria_mapa(10)
for i in mapa:
    print(i)

