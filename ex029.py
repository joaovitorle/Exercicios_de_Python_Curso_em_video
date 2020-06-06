v= int(input('Qual a velocidade do seu carro: '))
m= (v-80)*7
if v>80:
    print(f'Você ultrapassou o limite de velocidade! O valor da multa será de {m} R$')
else:
    print(f'Você está dentro do limite de velocidade')


