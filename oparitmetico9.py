s = float(input('Digite o salário atual: R$'))
# n = s * 0.15
# r = s + n
r = s + (s * 15 / 100)
print('O seu salário atual é de R${:.2f}.'.format(r))
