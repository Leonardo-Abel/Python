v = float(input('Digite a velocidade do carro: '))
if v > 80:
    m = (v - 80) * 7
    print('Você foi multado! Você deverá pagar R${:.2f}.'.format(m))
print('Dirija com segurança! Tenha um bom dia.')
