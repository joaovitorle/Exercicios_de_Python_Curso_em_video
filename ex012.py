p1 = float(input('Qual o preço do produto? '))
d = float(input('Qual o desconto aplicado pela loja? '))

p = p1*((100-d)*0.01)


print(f'O produto que custava {p1}, na promoção com desconto de {d}%, vai custar {p:.2f} reais ')
