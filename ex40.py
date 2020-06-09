n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

if m < 5:
    print(f'REPROVADO, sua média foi {m:.2f}')
elif m>= 5 and m<=6.9:
    print(f'RECUPERAÇÃO, sua média foi {m:.2f}')
elif m>= 7:
    print(f'APROVADO, sua média foi {m:.2f}')


