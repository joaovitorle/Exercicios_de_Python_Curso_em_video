from math import radians,sin,cos,tan
a= int(input('Digite o ângulo que você deseja: '))
sen= sin(radians(a))
cose= cos(radians(a))
tang= tan(radians(a))
print(f'O ângulo de {a} graus tem seno igual a {sen:.2f} \n O ângulo de {a} graus tem cosseno igual a {cose:.2f} \n O ângulo de {a} graus tem tangente igual a {tang:.2f}')
