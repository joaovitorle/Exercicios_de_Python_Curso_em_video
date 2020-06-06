d= int(input('Qual a distância da viagem, em KM: '))
v1= 0.50*d
v2= 0.45*d
print(f'O valor da passagem será {v1} R$' if d<=200 else f'O valor da passagem será {v2} R$')

