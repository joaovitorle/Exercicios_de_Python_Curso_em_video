s = float(input('Qual o salário do funcionário?R$ '))
a = int(input('Quantos % irá receber de aumento? '))
d = s*((100+a)*0.01)

print(f'Um funcionário que ganhava {s} R$, com {a} % de aumento, passará a receber R$ {d}')
