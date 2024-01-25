d = float(input('Digite a distância da viagem: '))
# p = d * 0.5 if d <= 200 else d * 0.45
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('Sua viagem custará R${:.2f}.'.format(p))
