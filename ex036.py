c= float(input('Qual o valor da casa: '))
s= float(input('Qual o seu salário: '))
a= int(input('Em quantos anos você vai pagar: '))

p= c/(a*12)
min= s * (30/100)

if p>= min:
    print('Parcelamento Negado !')
else:
    print(f'Parcelamento Aprovado ! Serão pagos em {a} anos com parcelas de {p:.2f} R$ por mês')
