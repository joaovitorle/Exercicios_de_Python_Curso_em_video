import random
from time import sleep
m= random.randrange(0,3)
itens = ('Pedra', 'Papel', 'Tesoura')

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

j= int(input('Qual será sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-='*11)
print(f'Maquina jogou {(itens)[m]}')
print(f'Jogador jogou {(itens)[j]}')
print('-='*11)

#EMPATE
if m==j:
    print('EMPATE')
else:
#PEDRA E PAPEL
    if m==0 and j==1:
        print('Jogador VENCEU!!')
    elif m==1 and j==0:
        print('Maquina VENCEU!!')

    else:
#PEDRA E TESOURA
        if m==0 and j==2:
            print('Maquina VENCEU!!')
        elif m==2 and j==0:
            print('Jogador VENCEU!!')

        else:
#TESOURA E PAPEL
            if m==1 and j==2:
                print('Jogador VENCEU!!')
            elif m==2 and j==1:
                print('Maquina VENCEU!!')
            else:
                print('Erro, tente novamente!!')

