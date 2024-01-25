from math import cos, radians, sin, tan

a = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(a))
print('O ângulo de {} tem o seno de {:.2f}.'.format(a, s))
c = cos(radians(a))
print('O ângulo de {} tem o cosseno de {:.2f}.'.format(a, c))
t = tan(radians(a))
print('O ângulo de {} tem a tangente de {:.2f}.'.format(a, t))
