from datetime import date
ano= date.today().year
a= int(input('Qual o ano do seu nascimento: '))
i= ano - a
if i <= 9:
    print(f'O atleta tem {i} anos, Categoria: MIRIM ')
elif i >=10 and i<=14:
    print(f'O atleta tem {i} anos, Categoria: INFATIL')
elif i >=15 and i<=19:
    print(f'O atleta tem {i} anos, Categoria: JUNIOR')
elif i>=20 and i<=25:
    print(f'O atleta tem {i} anos, Categoria: SÊNIOR')
else:
    print(f'O atleta tem {i} anos, Categoria: MASTER')