d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))
t = (d * 60) + (k * 0.15)
print('O valor total a se pagar é R${:.2f}.'.format(t))
