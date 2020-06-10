p= float(input('Digite seu peso: '))
h= float(input('Digite sua altura: '))

imc= p/(h*h)
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc <18.5:
    print('Você está abaixo do peso ideal')
elif imc <25:
    print('VocÊ está no peso ideal')
elif imc <30:
    print('Você está acima do peso ideal, ou seja, está com sobrepeso')
elif imc <40:
    print('Você está acima do peso ideal, além disso está com obesidade!')
else:
    print('Obesidade mórbida')
