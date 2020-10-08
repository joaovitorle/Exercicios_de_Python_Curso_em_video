n = int(input('Digite um número: '))
tot = 0
for c in range (1, n +1):
    if n % c == 0:
        print ('\033[34m', end=' ')
        tot +=1
    else:
        print ('\33[m', end=' ')
    print(f'{c}', end=' ')
print (f'\nO número {n} foi divisível {tot} vezes' )
if tot > 2: 
    print(f'{n} NÃO É UM NÚMERO PRIMO!')
else: 
    print(f'{n} É UM NÚMERO PRIMO!')
