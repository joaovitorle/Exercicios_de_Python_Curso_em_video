from random import sample
n0 = input('Digite um nome: ')
n1 = input('Digite outro nome: ')
n2 = input('Digite novamente outro nome: ')
n3 = input('Por último, digite outro nome: ')
s= sample([n0,n1,n2,n3],k=4)
print(f'O ordem de apresentação será {s}')