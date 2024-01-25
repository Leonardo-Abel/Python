s = float(input('Digite o salário do funcionário: '))
if s >= 1250:
    a = (s * 0.1) + s
else:
    a = (s * 0.15) + s
print('O novo salário será de R${:.2f}.'.format(a))
