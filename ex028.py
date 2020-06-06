import random
n = random.randrange(0,5)
d= int(input('Digite um valor entre 0 e 5: '))
if n==d:
    print('Você acertou! Parabéns')
else:
    print(f'Você perdeu! O número que você digitou é {d} e a maquina escolheu {n}')

