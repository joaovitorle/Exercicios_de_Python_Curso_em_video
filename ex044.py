print('='*5,'LOJA DO SEU JOÃO','='*5)

p= float(input('Qual foi o valor da compra: '))
a= p*0.90
ac= p*0.95
c3= p*1.20

print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão de crédito
[ 4 ] 3x ou mais no cartão de crédito''')

o=int(input('Qual a opção de pagamento: '))

if o == 1:
    print(f'Você ganhou um desconto de 10% por pagar à vista! O valor da compra ficará de {a} R$')
elif o ==2:
    print(f'Você ganhou um desconto de 5% por pagar à vista no cartão de crédito! O valor da compra ficará de {ac} R$')
elif o ==3:
    print(f'O valor da compra é de {p} R$, parcelado 2x no cartão a primeira parcela será de {p/2} R$')
elif o==4:
    v= int(input('Em quantas vezes você quer fazer: '))
    print(f'Você pagará um juros de 20% na compra, o valor total da compra é de {c3} R$, parcelado em {v}x no cartão a primeira parcela será de {p/v} R$')
else:
    print('Valor invalido! Tente novamente')
