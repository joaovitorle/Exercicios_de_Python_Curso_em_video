n= (input('Informe um número: ')).strip()
cont= len(n)
u= n[cont-1:cont]
d= n[cont-2:cont-1]
c= n[cont-3:cont-2]
m= n[cont-4:cont-3]

print(f'Analisando o número {n}\n Unidade: {u}\n Dezena: {d}\n Centena: {c}\n Milhar: {m} ')



