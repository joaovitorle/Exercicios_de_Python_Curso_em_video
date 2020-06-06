s= int(input('Digite o atual salário para calcular o valor do aumento: '))
s1= s*1.10
a1= s1-s
s2= s*1.15
a2= s2-s
if s>1250:
    print(f'O novo salário será de {s1} R$ com um aumento de {a1}R$')
else:
    print(f'O novo salário será de {s2} R$ com um aumento de {a2}R$')

