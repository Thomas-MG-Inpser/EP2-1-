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

from aleatorio import cores_player

print(' ===================================== ')
print('|         Design de Software          |')
print('|   Batalha Naval - Thomas e Theron   |')
print('|              Turma B                |')
print(' =======   xxxxxxxxxxxxxxxxx   ======= ')
print('\n')

"""
#esta parte é um temporizador e um icicializador pra ficar dahorinha
print('digite qualquer coisa para continuar')
u=input('')
"""
reinicia=True
while reinicia:
    print('Jogo iniciando...')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('\n')

    mapa_ori=cria_mapa(12)


    alfabeto=[' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' ']
    numeros=[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ' ']

    for i in range(len(mapa_ori[0])):
        mapa_ori[0][i]=alfabeto[i]
        mapa_ori[len(mapa_ori)-1][i]=alfabeto[i]
    for i in range(len(mapa_ori)):
        mapa_ori[i][0]=numeros[i]
        mapa_ori[i][len(mapa_ori)-1]=numeros[i]

    mapa_branco=cria_mapa(12)

    for i in range(len(mapa_branco[0])):
        mapa_branco[0][i]=alfabeto[i]
        mapa_branco[len(mapa_branco)-1][i]=alfabeto[i]
    for i in range(len(mapa_branco)):
        mapa_branco[i][0]=numeros[i]
        mapa_branco[i][len(mapa_branco)-1]=numeros[i]

        
    #pc seleciona pais aleatório
    paispc = []
    for p, navios in PAISES.items():
        paispc.append(p)
    r = random.choice(paispc)

    blocos_pc = []
    for navios_pc, n in PAISES[r].items():
        for i in range(n):
            blocos_pc.append(CONFIGURACAO[navios_pc])

    mapa_pc = aloca_navios(mapa_ori, blocos_pc)

    #opa é a lista de paises
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

    #alfabeto_join = '    '.join(alfabeto)
    #print(f'\u001b[30m{'    '.join(alfabeto)}\u001b[0m')

    for i in range(len(mapa_ori[0])):
        mapa_ori[0][i]=alfabeto[i]
        mapa_ori[len(mapa_ori)-1][i]=alfabeto[i]
    for i in range(len(mapa_ori)):
        mapa_ori[i][0]=numeros[i]
        mapa_ori[i][len(mapa_ori)-1]=numeros[i]


    index_pais_player = int(input("Escolha o número da sua nação: "))-1
    pais_player = opa[index_pais_player]
    print(pais_player)
    print('\n')
    print(f'COMPUTADOR - {r}                                       JOGADOR - {pais_player}')

    #print(cores_player(mapa_branco), end = ' ')
    #print(cores_player(mapa_branco))

    for i in range(len(mapa_branco)):
        print(mapa_branco[i], end = ' ')
        print(mapa_ori[i])

    blocos_player = []
    for navios_player, n in PAISES[pais_player].items():
        for i in range(n):
            blocos_player.append(CONFIGURACAO[navios_player])


    for blocos in blocos_player:
        f=True
        while f:
            print('\n')
            coluna_let = input('Informe a Letra: ').upper()
            if coluna_let not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                print("Opção Inválida")
                continue
            for i in range(len(alfabeto)):
                if alfabeto[i] == coluna_let:
                    coluna = i
            linha0=input('Informe o Número: ')
            if linha0 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                print("Opção Inválida")
                continue
            linha = int(linha0)
            orientacao = input('Informe a Orientação(v/h): ')
            for i in range(blocos):
                if orientacao=='v':
                    if (linha+(blocos-1))>=len(mapa_ori) or mapa_ori[linha+i][coluna]!=' ':
                        f=True
                        print("Não é possível alocar nesta posição.")
                        break
                elif orientacao=='h':
                    if (coluna+(blocos-1))>=len(mapa_ori) or mapa_ori[linha][coluna+i]!=' ':
                        f=True
                        print("Não é possível alocar nesta posição.")
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
        print(f'COMPUTADOR - {r}                                          JOGADOR - {pais_player}')
        for i in range(len(mapa_pc)):
            print(mapa_branco[i], end = ' ')
            print(mapa_ori[i])
    
    print('\n')

    # comecar os tiros
    print('Hora de atacar!')
    print('As coordenadas são compostas por letras e números.')
    jogo_continua=True # vai ser definido pela funcao foi_derrotado
    while jogo_continua:

        coluna_player= input('Qual letra? ')
        coluna_player=coluna_player.upper()
        if coluna_player not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
            print('Coordenada inválida.')
            continue
        for i in range(len(alfabeto)):
                if alfabeto[i] == coluna_player:
                    coluna_player = i
        linha_player= input('Qual número? ')
        if linha_player not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            print('Coordenada inválida.')
            continue
        coordenada=[coluna_player, linha_player]
        mapa_pc= tiro_player(mapa_pc,coordenada)

        mapa_ori= tiro_pc(mapa_ori)

        for i in range(len(mapa_pc)):
            for j in range(len(mapa_pc)):
                if mapa_pc[i][j]=='o':
                    mapa_branco[i][j]='o'
                elif mapa_pc[i][j]=='X':
                    mapa_branco[i][j]='X'

        print('\n')
        print(f'COMPUTADOR - {r}                                          JOGADOR - {pais_player}')
        
        print(cores_player(mapa_branco), end = ' ')
        print(cores_player(mapa_ori))
        player= foi_derrotado(mapa_ori)
        pc= foi_derrotado(mapa_pc)
        if (player or pc)==True:
            jogo_continua=False

    if pc:
        print('Você venceu!!!')
    elif player:
        print('Computador venceu!')

    x=True
    while x:
        cond=input('Jogar novamente?(S/N) ').upper()
        if cond =='S':
            reinicia=True
            break
        elif cond =='N':
            reinicia=False
            break
        print('Opção inválida!')