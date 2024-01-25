from math import hypot

co = float(input('Comprimeto do cateto oposto: '))
ca = float(input('Comprimeto do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(h))
