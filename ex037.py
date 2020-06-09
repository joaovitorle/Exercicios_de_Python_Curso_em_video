num = int(input('Digite um número inteiro: '))
print('''Escolha um número das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
op = int(input('Escolha sua opção: '))
bin = bin(num) [2:]
oct= oct(num) [2:]
hex= hex(num) [2:]


if op == 1:
    print(f'{op} convertido para Binário é igual a {bin}')

elif op ==2:
    print(f'{op} convertido para Octal é igual a {oct}')
elif op ==3:
    print(f'{op} convertido para Hexadecimal é igual a {hex}')
else:
    print('Opção invalida, tente novamente!!')
