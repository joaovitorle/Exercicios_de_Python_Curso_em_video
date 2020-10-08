soma = 0
cont = 0 
for c in range (1,7):
    n= int (input ('Digete um número: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont +1
print(f'Você informou {cont} valores e a soma deles é = {soma}')
