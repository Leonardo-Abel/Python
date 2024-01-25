p = float(input('Digite o seu peso (Kg): '))
a = float(input('Digite a sua altura (m): '))
imc = p / (a ** 2)
if imc < 18.5:
    print('{:.1f} - Abaixo do peso.'.format(imc))
elif imc < 25:
    print('{:.1f} - Peso ideal.'.format(imc))
elif imc < 30:
    print('{:.1f} - Sobrepeso.'.format(imc))
elif imc < 40:
    print('{:.1f} - Obesidade.'.format(imc))
else:
    print('{:.1f} - Obesidade Mórbida.'.format(imc))
